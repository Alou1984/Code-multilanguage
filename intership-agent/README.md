# alternance-agent-ai

Agent Python gratuit exécuté avec GitHub Actions.

Il recherche chaque jour des offres de :

- stage
- internship / intership
- graduate program
- alternance
- apprentissage

pour un poste comme :

- expert cybersécurité
- ingénieur cybersécurité
- chef de projet cybersécurité

et envoie les liens par email à :

```text
papalassane2003@yahoo.fr
```

## Zones ciblées

France :

- Île-de-France
- Centre-Val de Loire
- Bourgogne-Franche-Comté
- Aube

Suisse :

- Suisse romande
- Genève
- Lausanne
- Vaud
- Neuchâtel
- Fribourg
- Valais
- Jura

## Formation cible

```text
Mastère Spécialisé® Expert en Cybersécurité
Rentrée : septembre 2026
Rythme : 1 semaine par mois en cours / 3 semaines en entreprise
```

## Arborescence à copier dans ton dépôt Code-multilanguage

```text
.github/
└─ workflows/
   └─ alternance-agent-ai.yml

alternance-agent-ai/
├─ requirements.txt
├─ src/
│  └─ job_agent.py
└─ data/
   └─ seen_jobs.json
```

## Secrets GitHub à créer

Dans ton dépôt GitHub :

```text
Settings → Secrets and variables → Actions → New repository secret
```

Crée ces secrets :

```text
EMAIL_USER = papalassane2003@yahoo.fr
EMAIL_PASSWORD = mot_de_passe_application_yahoo
EMAIL_TO = papalassane2003@yahoo.fr
```

Important : `EMAIL_PASSWORD` doit être un mot de passe d'application Yahoo, pas ton mot de passe Yahoo normal.

## Lancer manuellement

Va dans :

```text
Actions → Daily Alternance Cyber Agent → Run workflow
```

## Fonctionnement horaire

GitHub Actions utilise UTC.

Le workflow se lance à :

```text
06:00 UTC
07:00 UTC
```

Le script Python vérifie ensuite l'heure locale `Europe/Paris` et envoie seulement à 08h00.

Cela permet de gérer l'heure d'été et l'heure d'hiver.

## Limites

LinkedIn, Glassdoor et certains sites bloquent souvent le scraping automatique.
Le script utilise donc :

- flux publics Google News RSS
- liens de recherche directe
- score automatique par mots-clés

Cela évite les blocages et garde le projet gratuit.
