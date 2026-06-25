# agent_alternance_IA_data

Projet Python prêt pour VS Code + GitHub Actions.  
Objectif : recevoir chaque jour à **08h00 Europe/Paris** un email avec des liens d'offres pour :

- stage, internship/intership, graduate program, alternance, apprentissage ;
- postes Expert Big Data Engineer, Data Engineer, Ingénieur IA, MLOps, chef de projet data, logiciel, systèmes embarqués, intégration système ;
- France : Île-de-France, Centre-Val de Loire, Bourgogne-Franche-Comté, Aube ;
- Suisse romande : Genève, Vaud, Lausanne, Neuchâtel, Fribourg, Valais ;
- sites ciblés : LinkedIn, Glassdoor, Indeed, APEC, HelloWork, Teamtailor, Jobup, France Travail, Randstad, TotalEnergies, Safran, Framatome.

## 1. Ouvrir dans VS Code

```bash
cd agent_alternance_IA_data
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Copier l'exemple d'environnement :

```bash
cp .env.example .env
```

Puis renseigner les valeurs SMTP dans `.env` si tu testes en local.

## 2. Test local sans envoyer d'email

```bash
export PYTHONPATH=src
export FORCE_RUN=true
export DRY_RUN=true
python -m agent_jobs.main
```

Dans VS Code, tu peux aussi lancer la configuration : **Lancer agent alternance IA data**.

## 3. Configuration GitHub

Créer un dépôt GitHub, puis pousser ce projet :

```bash
git init
git add .
git commit -m "Initial agent alternance IA data"
git branch -M main
git remote add origin https://github.com/TON_COMPTE/agent_alternance_IA_data.git
git push -u origin main
```

Ensuite, dans GitHub :

`Settings > Secrets and variables > Actions > New repository secret`

Créer ces secrets :

| Secret | Exemple |
|---|---|
| `SMTP_HOST` | `smtp.mail.yahoo.com` |
| `SMTP_PORT` | `465` |
| `SMTP_USER` | ton adresse Yahoo ou l'adresse expéditrice |
| `SMTP_PASSWORD` | mot de passe d'application Yahoo |
| `EMAIL_FROM` | ton adresse expéditrice |
| `SERPAPI_API_KEY` | optionnel |

Le destinataire est déjà défini dans le workflow : `papalassane2003@yahoo.fr`.

## 4. Important pour Yahoo Mail

Yahoo demande généralement un **mot de passe d'application** pour autoriser l'envoi SMTP depuis un script.  
Ne mets jamais ton mot de passe Yahoo principal dans le dépôt GitHub.

## 5. Fonctionnement des recherches

Deux modes existent :

### Mode sans clé SerpApi

Le programme envoie des **liens de recherche ciblés** par site. C'est le mode gratuit et immédiat.

### Mode avec `SERPAPI_API_KEY`

Le programme interroge SerpApi pour récupérer des résultats Google ciblés par site, puis envoie des offres individuelles.  
Ce mode évite de scraper directement LinkedIn, Indeed, Glassdoor, etc., qui bloquent souvent les robots et peuvent limiter l'automatisation.

## 6. Planification

Le fichier `.github/workflows/agent_alternance_IA_data.yml` lance le workflow à :

- `06:00 UTC`
- `07:00 UTC`

Le script vérifie ensuite l'heure `Europe/Paris` et n'envoie l'email que lorsqu'il est réellement **08h00 à Paris**. Cela gère le changement d'heure été/hiver.

## 7. Modifier les critères

Les critères sont dans `config.yml` :

- `contracts`
- `roles`
- `skills`
- `locations`
- `sources`

Tu peux ajouter d'autres entreprises ou régions en complétant la section `sources`.
