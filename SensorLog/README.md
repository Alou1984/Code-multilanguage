# agent_alternance_IA_data

Agent GitHub Actions qui recherche chaque jour des offres ciblées : IA, data, nouvelles technologies, énergie, oil & gas, secteur minier, systèmes embarqués, logiciel, robotique, HVAC.

Priorité géographique : offres situées à moins de 80 km de Sens 89100, puis France / Suisse romande.

## Secrets GitHub requis

Dans `Settings → Secrets and variables → Actions` :

```text
SERPAPI_API_KEY=clé SerpApi
SMTP_HOST=smtp.mail.yahoo.com
SMTP_PORT=465
SMTP_USER=papalassane2003@yahoo.fr
SMTP_PASSWORD=mot_de_passe_application_yahoo
EMAIL_FROM=papalassane2003@yahoo.fr
EMAIL_TO=papalassane2003@yahoo.fr
```

Sans `SERPAPI_API_KEY`, l'agent n'envoie plus de liens vides : il enverra un message indiquant qu'aucune offre exploitable n'a été trouvée.

## Test local

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:PYTHONPATH="src"
python -m agent_jobs.main
```
