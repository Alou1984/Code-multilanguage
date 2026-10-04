import json
import os
import time

import mysql.connector
from kafka import KafkaConsumer


# =========================================================
# Configuration
# =========================================================

KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "kafka:9092"
)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "sensorlog"),
    "password": os.getenv("DB_PASSWORD", "sensorlog"),
    "database": os.getenv("DB_NAME", "sensorlog"),
}


# Nombre maximum de mesures conservées
MAX_READINGS = 1000


# =========================================================
# Connexion MySQL
# =========================================================

def get_connection():

    return mysql.connector.connect(
        **DB_CONFIG
    )


# =========================================================
# Connexion à Kafka
# =========================================================

print("Connexion à Kafka...")

consumer = None

while consumer is None:

    try:

        consumer = KafkaConsumer(
            "sensor-readings",
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_deserializer=lambda value:
                json.loads(value.decode("utf-8")),
            auto_offset_reset="latest",
            enable_auto_commit=True,
            group_id="sensorlog-consumer"
        )

        print("Connexion Kafka OK.")

    except Exception as error:

        print(
            "Kafka indisponible :",
            error
        )

        time.sleep(5)


# =========================================================
# Connexion à MySQL
# =========================================================

connection = None

while connection is None:

    try:

        connection = get_connection()

        print(
            "Connexion MySQL OK."
        )

    except mysql.connector.Error as error:

        print(
            "MySQL indisponible :",
            error
        )

        time.sleep(5)


# =========================================================
# Fonction de nettoyage
# =========================================================

def cleanup_database(connection):

    cursor = connection.cursor()

    try:

        # Compte le nombre total de relevés.

        cursor.execute(
            "SELECT COUNT(*) FROM readings"
        )

        total = cursor.fetchone()[0]


        # Nettoyage uniquement à partir de 1000 mesures.

        if total >= MAX_READINGS:

            print(
                f"{total} mesures présentes. "
                "Nettoyage de la base..."
            )


            # On conserve les 1000 mesures
            # ayant les ID les plus élevés.

            cursor.execute(
                """
                DELETE FROM readings
                WHERE id NOT IN (
                    SELECT id
                    FROM (
                        SELECT id
                        FROM readings
                        ORDER BY id DESC
                        LIMIT %s
                    ) AS recent_readings
                )
                """,
                (MAX_READINGS,)
            )


            deleted = cursor.rowcount

            connection.commit()


            print(
                f"Nettoyage terminé : "
                f"{deleted} ancienne(s) mesure(s) supprimée(s)."
            )


    except mysql.connector.Error as error:

        connection.rollback()

        print(
            "Erreur pendant le nettoyage MySQL :",
            error
        )


    finally:

        cursor.close()


# =========================================================
# Réception des mesures Kafka
# =========================================================

print(
    "Consumer en attente de mesures..."
)


for message in consumer:

    try:

        data = message.value

        sensor = data["sensor"]
        value = float(data["value"])


        # -------------------------------------------------
        # Enregistrement dans MySQL
        # -------------------------------------------------

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

        cursor.close()


        print(
            f"Mesure reçue : "
            f"{sensor} = {value}"
        )

        print(
            "Mesure enregistrée dans MySQL."
        )


        # -------------------------------------------------
        # Vérification du nettoyage
        # -------------------------------------------------

        cleanup_database(
            connection
        )


    except mysql.connector.Error as error:

        print(
            "Erreur MySQL :",
            error
        )

        try:

            connection.close()

        except Exception:
            pass


        connection = None


        # Tentative de reconnexion.

        while connection is None:

            try:

                connection = get_connection()

                print(
                    "Reconnexion MySQL réussie."
                )

            except mysql.connector.Error as reconnect_error:

                print(
                    "Reconnexion MySQL impossible :",
                    reconnect_error
                )

                time.sleep(5)


    except Exception as error:

        print(
            "Erreur lors du traitement :",
            error
        )