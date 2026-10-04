# Lecture des fichiers CSV
import csv

# Variables d'environnement
import os

# Gestion des délais entre les tentatives de connexion
import time

# Communication avec MySQL
import mysql.connector

# Framework web Flask
from flask import Flask, jsonify, render_template, request


# Création de l'application Flask
app = Flask(__name__)


# ---------------------------------------------------------
# Configuration MySQL
# ---------------------------------------------------------

# "db" est le nom du service MySQL dans Docker Compose.
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "sensorlog"),
    "password": os.getenv("DB_PASSWORD", "sensorlog"),
    "database": os.getenv("DB_NAME", "sensorlog"),
}


# ---------------------------------------------------------
# Types de capteurs autorisés
# ---------------------------------------------------------

ALLOWED_SENSORS = {
    "temperature",
    "hygro",
    "co2",
    "cov",
    "wind_speed",
    "uv",
}


# ---------------------------------------------------------
# Connexion à MySQL
# ---------------------------------------------------------

def get_connection():
    """
    Ouvre une connexion vers MySQL.
    """
    return mysql.connector.connect(**DB_CONFIG)


# ---------------------------------------------------------
# Initialisation de la base de données
# ---------------------------------------------------------

def init_db():
    """
    Vérifie que MySQL est disponible et crée la table
    readings si elle n'existe pas.
    """

    for attempt in range(10):

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS readings (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    sensor VARCHAR(100) NOT NULL,
                    value FLOAT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            connection.commit()

            cursor.close()
            connection.close()

            print("Connexion MySQL OK - table readings prête.")

            return

        except mysql.connector.Error as error:

            print(
                f"MySQL indisponible "
                f"(tentative {attempt + 1}/10) : {error}"
            )

            time.sleep(3)

    raise RuntimeError(
        "Impossible de se connecter à MySQL."
    )


# ---------------------------------------------------------
# Page principale
# ---------------------------------------------------------

@app.route("/")
def home():
    """
    Affiche le dashboard SensorLog.
    """

    return render_template("index.html")


# ---------------------------------------------------------
# API : récupérer les relevés
# ---------------------------------------------------------

@app.route("/api/readings", methods=["GET"])
def get_readings():
    """
    Retourne tous les relevés présents dans MySQL.
    """

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, sensor, value, created_at
        FROM readings
        ORDER BY id DESC
    """)

    readings = cursor.fetchall()

    cursor.close()
    connection.close()

    # Conversion des dates MySQL en texte.
    for reading in readings:
        reading["created_at"] = (
            reading["created_at"].isoformat()
        )

    return jsonify(readings)


# ---------------------------------------------------------
# API : ajouter manuellement un relevé
# ---------------------------------------------------------

@app.route("/api/readings", methods=["POST"])
def create_reading():
    """
    Ajoute manuellement une mesure reçue en JSON.
    """

    data = request.get_json()

    # Vérification des champs obligatoires.
    if not data or "sensor" not in data or "value" not in data:

        return jsonify({
            "error": (
                "Les champs 'sensor' et 'value' "
                "sont obligatoires."
            )
        }), 400

    sensor = str(
        data["sensor"]
    ).strip().lower()

    # Vérification du type de capteur.
    if sensor not in ALLOWED_SENSORS:

        return jsonify({
            "error": (
                "Type de capteur non reconnu. "
                "Types autorisés : "
                "temperature, hygro, co2, cov, "
                "wind_speed, uv."
            )
        }), 400

    # Conversion de la valeur en nombre.
    try:
        value = float(data["value"])

    except (TypeError, ValueError):

        return jsonify({
            "error": (
                "La valeur du capteur "
                "doit être numérique."
            )
        }), 400

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO readings (
            sensor,
            value
        )
        VALUES (%s, %s)
        """,
        (
            sensor,
            value
        )
    )

    connection.commit()

    reading_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Relevé enregistré",
        "id": reading_id
    }), 201


# ---------------------------------------------------------
# Import d'un fichier CSV
# ---------------------------------------------------------

@app.route("/upload", methods=["POST"])
def upload_file():
    """
    Reçoit un fichier CSV depuis le dashboard.

    Format attendu :

    timestamp,sensor,value

    Exemple :

    2026-10-04 13:00:00,temperature,23.5
    2026-10-04 13:00:00,uv,4.2
    """

    # Vérifie qu'un fichier est présent.
    if "file" not in request.files:

        return jsonify({
            "error": "Aucun fichier envoyé."
        }), 400

    file = request.files["file"]

    # Vérifie qu'un fichier a été sélectionné.
    if file.filename == "":

        return jsonify({
            "error": "Aucun fichier sélectionné."
        }), 400

    # Vérifie l'extension.
    if not file.filename.lower().endswith(".csv"):

        return jsonify({
            "error": "Le fichier doit être au format CSV."
        }), 400

    try:

        # Lecture du fichier UTF-8.
        content = (
            file.stream
            .read()
            .decode("utf-8-sig")
        )

        lines = content.splitlines()

        # Lecture du CSV.
        reader = csv.DictReader(lines)

        # Colonnes obligatoires.
        required_columns = {
            "timestamp",
            "sensor",
            "value"
        }

        # Vérification des colonnes.
        if not required_columns.issubset(
            reader.fieldnames or []
        ):

            return jsonify({
                "error": (
                    "Le CSV doit contenir les colonnes "
                    "timestamp, sensor et value."
                )
            }), 400

        connection = get_connection()

        cursor = connection.cursor()

        count = 0

        # Parcours des lignes du fichier.
        for row in reader:

            sensor = (
                row["sensor"]
                .strip()
                .lower()
            )

            value = float(
                row["value"]
            )

            timestamp = (
                row["timestamp"]
                .strip()
            )

            # Ignore les capteurs inconnus.
            if sensor not in ALLOWED_SENSORS:
                continue

            # Enregistrement dans MySQL.
            cursor.execute(
                """
                INSERT INTO readings (
                    sensor,
                    value,
                    created_at
                )
                VALUES (%s, %s, %s)
                """,
                (
                    sensor,
                    value,
                    timestamp
                )
            )

            count += 1

        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            "message": "Fichier chargé avec succès",
            "count": count
        })

    except Exception as error:

        return jsonify({
            "error": (
                "Erreur lors du traitement du fichier : "
                f"{error}"
            )
        }), 400


# ---------------------------------------------------------
# Démarrage de l'application
# ---------------------------------------------------------

if __name__ == "__main__":

    # Vérification de MySQL.
    init_db()

    # Serveur Flask.
    app.run(
        host="0.0.0.0",
        port=5000
    )