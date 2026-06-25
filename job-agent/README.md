# 🔍 Agent Veille Emploi — GitHub Actions (100% Gratuit)

Envoi automatique chaque matin à 8h d'un digest d'offres d'emploi ciblé.

## ✅ Ce que fait ce workflow
- Scrape **9 plateformes** : LinkedIn, Indeed, APEC, France Travail, HelloWork, Randstad, Glassdoor, Teamtailor, JobUp
- Filtre par **zone géographique** (France, Suisse, Luxembourg, EAU, Arabie Saoudite, Sénégal)
- Filtre par **poste** (Chef de projet technique, Directeur technique…)
- **Score les offres avec Claude IA** (0-100) selon votre profil
- Envoie un **email HTML** à `papalassane2003@yahoo.fr` à 8h00

---

## 🚀 Installation (15 minutes)

### Étape 1 — Créer le dépôt GitHub

1. Aller sur [github.com/new](https://github.com/new)
2. Créer un dépôt privé : `job-alert`
3. Uploader tous les fichiers de ce projet dans le dépôt

### Étape 2 — Obtenir une clé API Anthropic (gratuit au départ)

1. Aller sur [console.anthropic.com](https://console.anthropic.com)
2. Créer un compte → API Keys → New Key
3. Copier la clé (commence par `sk-ant-...`)

> 💡 Coût estimé : ~0.01$ par jour avec claude-haiku (très économique)

### Étape 3 — Configurer l'email expéditeur (Gmail recommandé)

**Option A — Gmail (recommandé)**
1. Activer la validation en 2 étapes sur votre compte Google
2. Aller dans Compte Google → Sécurité → Mots de passe des applications
3. Créer un mot de passe pour "Autre application" → nommer "job-agent"
4. Copier le mot de passe à 16 caractères généré

**Option B — Yahoo**
1. Compte Yahoo → Sécurité → Mot de passe d'application
2. Générer un mot de passe pour "Autre application"
3. Dans `job_agent.py`, changer `smtp_host` en `smtp.mail.yahoo.com`

### Étape 4 — Ajouter les Secrets GitHub

Dans votre dépôt GitHub :
→ **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Ajouter ces 3 secrets :

| Nom du secret | Valeur |
|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-api03-xxxxx` |
| `SMTP_USER` | `votreemail@gmail.com` |
| `SMTP_PASSWORD` | `xxxx xxxx xxxx xxxx` (mot de passe app) |
| `EMAIL_DEST` | `papalassane2003@yahoo.fr` |

### Étape 5 — Activer les Actions GitHub

1. Aller dans l'onglet **Actions** de votre dépôt
2. Cliquer **"I understand my workflows, go ahead and enable them"**
3. Le workflow se déclenchera automatiquement chaque jour à 6h UTC (= 8h Paris)

### Étape 6 — Tester manuellement

1. Onglet **Actions** → **Veille Emploi Quotidienne**
2. Cliquer **"Run workflow"** → **"Run workflow"**
3. Vérifier que le job passe au vert ✅
4. Vérifier votre boîte mail dans les 2 minutes

---

## 📁 Structure du projet

```
job-alert/
├── .github/
│   └── workflows/
│       └── job_alert.yml      ← Planification GitHub Actions
├── src/
│   └── job_agent.py           ← Code principal de l'agent
├── requirements.txt           ← Dépendances Python
└── README.md
```

---

## ⚙️ Personnaliser les critères

Ouvrir `src/job_agent.py` et modifier la section `CONFIG` :

```python
CONFIG = {
    "postes": ["chef de projet technique", ...],   # Modifier les titres
    "salaire_min_eur": 60000,                      # Seuil de salaire
    "score_min_ia": 40,                            # Score minimum IA (0-100)
    ...
}
```

---

## 🕐 Heure d'envoi

Le fichier `.github/workflows/job_alert.yml` contient :
```yaml
- cron: '0 6 * * *'   # 6h UTC = 8h Paris (hiver) / 8h Paris (été)
```
Pour changer l'heure, modifier le cron (en UTC) :
- 8h Paris hiver (UTC+1) = `0 7 * * *`
- 8h Paris été (UTC+2) = `0 6 * * *`

---

## 💰 Coûts

| Service | Coût |
|---|---|
| GitHub Actions | **Gratuit** (2 000 min/mois) |
| Claude Haiku (scoring) | ~0.01$/jour ≈ 0.30$/mois |
| Gmail SMTP | **Gratuit** |
| Hébergement | **Gratuit** |

**Total : ~0.30$/mois** (quasi gratuit)

---

## ❓ Problèmes fréquents

**Le workflow ne se déclenche pas ?**
→ Vérifier que les Actions sont activées dans l'onglet Actions du dépôt.

**Erreur SMTP Authentication ?**
→ Vérifier que vous utilisez un "mot de passe d'application" et non votre vrai mot de passe.

**Pas d'offres dans le mail ?**
→ Les scrapers peuvent être bloqués temporairement. Relancer manuellement le lendemain.

**Erreur Anthropic API ?**
→ Vérifier que le secret `ANTHROPIC_API_KEY` est bien configuré et que votre compte a des crédits.
