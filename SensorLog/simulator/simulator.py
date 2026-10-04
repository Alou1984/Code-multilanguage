import json
import os
import random
import time
from datetime import datetime

from kafka import KafkaProducer


# ---------------------------------------------------------
# Configuration Kafka
# ---------------------------------------------------------

KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "kafka:9092"
)

KAFKA_TOPIC = "sensor-readings"


# ---------------------------------------------------------
# Connexion à Kafka
# ---------------------------------------------------------

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda value:
        json.dumps(value).encode("utf-8")
)


# ---------------------------------------------------------
# Génération d'une mesure
# ---------------------------------------------------------

def generate_readings():

    timestamp = datetime.now().isoformat()

    return [

        {
            "timestamp": timestamp,
            "sensor": "temperature",
            "value": round(
                random.uniform(18, 30),
                2
            )
        },

        {
            "timestamp": timestamp,
            "sensor": "hygro",
            "value": round(
                random.uniform(35, 75),
                2
            )
        },

        {
            "timestamp": timestamp,
            "sensor": "co2",
            "value": round(
                random.uniform(400, 1200),
                2
            )
        },

        {
            "timestamp": timestamp,
            "sensor": "cov",
            "value": round(
                random.uniform(0.1, 2.0),
                2
            )
        },

        {
            "timestamp": timestamp,
            "sensor": "wind_speed",
            "value": round(
                random.uniform(0, 15),
                2
            )
        },

        {
            "timestamp": timestamp,
            "sensor": "uv",
            "value": round(
                random.uniform(0, 11),
                2
            )
        }

    ]


# ---------------------------------------------------------
# Boucle principale
# ---------------------------------------------------------

print("Simulateur SensorLog démarré.")

while True:

    readings = generate_readings()

    for reading in readings:

        producer.send(
            KAFKA_TOPIC,
            reading
        )

        print(
            "Mesure envoyée :",
            reading
        )

    producer.flush()

    # Nouvelle série de mesures toutes les 5 secondes.

    time.sleep(5)