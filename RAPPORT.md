# Rapport — Mini-projet Docker : SensorLog

## 1. Présentation du projet

SensorLog est une application de supervision de capteurs développée avec Flask, Docker Compose, Apache Kafka et MySQL.

L'application permet de simuler des mesures de plusieurs capteurs, de les transmettre avec Kafka, de les enregistrer dans MySQL et de les visualiser depuis une interface web.

Le projet est composé de six services Docker :

- `web` : application Flask et interface web ;
- `db` : base de données MySQL ;
- `zookeeper` : service de coordination utilisé par Kafka ;
- `kafka` : système de transmission des mesures ;
- `simulator` : génération automatique des mesures ;
- `consumer` : récupération des mesures Kafka et enregistrement dans MySQL.

L'architecture générale est la suivante :

```text
Simulateur
    ↓
  Kafka
    ↓
 Consumer
    ↓
  MySQL
    ↓
API Flask
    ↓
Interface web