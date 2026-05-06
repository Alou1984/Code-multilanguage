#!/usr/bin/env python3
"""
job_agent.py — Agent IA de veille emploi quotidienne
Scrape les offres, filtre par IA (Claude), envoie un digest par mail.
Déployé via GitHub Actions, 100% gratuit.
"""

import os
import json
import time
import smtplib
import logging
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import urlencode, quote_plus

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import anthropic

# ── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
log = logging.getLogger(__name__)

# ── Configuration ────────────────────────────────────────────────────────────
CONFIG = {
    "email_dest": os.environ.get("EMAIL_DEST", "papalassane2003@yahoo.fr"),
    "smtp_user": os.environ.get("SMTP_USER", ""),          # votre email expéditeur
    "smtp_password": os.environ.get("SMTP_PASSWORD", ""),  # mot de passe app
    "smtp_host": "smtp.gmail.com",                          # ou smtp.mail.yahoo.com
    "smtp_port": 587,

    "postes": [
        "chef de projet technique",
        "chef de projet programme",
        "directeur technique",
        "technical program manager",
        "CTO",
    ],

    "mots_cles_competences": [
        "électronique", "electronique", "hardware", "firmware",
        "système embarqué", "systeme embarque", "embedded",
        "intégration système", "integration systeme",
        "logiciel", "software",
        "gestion de projet technique",
    ],

    "zones_france": [
        "île-de-france", "paris", "val-de-marne", "hauts-de-seine",
        "seine-saint-denis", "yvelines", "essonne", "val-d'oise",
        "seine-et-marne", "centre-val de loire", "bourgogne",
        "franche-comté", "aube", "troyes",
    ],

    "zones_international": [
        "suisse", "switzerland", "genève", "lausanne", "zürich",
        "luxembourg", "arabie saoudite", "saudi arabia", "riyadh",
        "émirats", "emirates", "dubai", "abu dhabi",
        "sénégal", "senegal", "dakar",
    ],

    "salaire_min_eur": 60000,
    "max_offres_par_source": 20,
    "score_min_ia": 40,   # Score IA minimum (0-100) pour inclure une offre
}

# ── Requêtes HTTP ─────────────────────────────────────────────────────────────
ua = UserAgent()

def get_headers():
    return {
        "User-Agent": ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }

def safe_get(url, params=None, timeout=15):
    """GET avec retry et headers rotatifs."""
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params, headers=get_headers(),
                                timeout=timeout)
            if resp.status_code == 200:
                return resp
            log.warning(f"HTTP {resp.status_code} pour {url}")
        except Exception as e:
            log.warning(f"Tentative {attempt+1}/3 échouée : {e}")
            time.sleep(2 ** attempt)
    return None

# ── Scrapers par plateforme ───────────────────────────────────────────────────

def scrape_indeed(poste, zone):
    """Indeed France — scraping RSS/HTML."""
    offres = []
    url = "https://fr.indeed.com/jobs"
    params = {"q": poste, "l": zone, "fromage": "1", "sort": "date"}
    resp = safe_get(url, params=params)
    if not resp:
        return offres
    soup = BeautifulSoup(resp.text, "lxml")
    cards = soup.select("div.job_seen_beacon")[:CONFIG["max_offres_par_source"]]
    for card in cards:
        try:
            titre = card.select_one("h2.jobTitle span[title]")
            entreprise = card.select_one("span.companyName")
            lieu = card.select_one("div.companyLocation")
            lien_el = card.select_one("h2.jobTitle a")
            salaire_el = card.select_one("div.salaryOnly")
            if not titre or not lien_el:
                continue
            offres.append({
                "source": "Indeed",
                "titre": titre.get_text(strip=True),
                "entreprise": entreprise.get_text(strip=True) if entreprise else "N/A",
                "lieu": lieu.get_text(strip=True) if lieu else zone,
                "salaire": salaire_el.get_text(strip=True) if salaire_el else "",
                "lien": "https://fr.indeed.com" + lien_el.get("href", ""),
                "description": "",
            })
        except Exception as e:
            log.debug(f"Erreur parsing Indeed card: {e}")
    log.info(f"Indeed [{poste}/{zone}] → {len(offres)} offres")
    return offres


def scrape_apec(poste):
    """APEC — API officielle (gratuite, pas d'auth)."""
    offres = []
    url = "https://www.apec.fr/cms/webservices/rechercheOffre/rechercheOffre"
    payload = {
        "motsCles": poste,
        "typeContrat": [],
        "lieu": [],
        "nbResultatsParPage": CONFIG["max_offres_par_source"],
        "numeroPage": 0,
        "tri": 1,  # 1 = date
    }
    try:
        resp = requests.post(
            url,
            json=payload,
            headers={**get_headers(), "Content-Type": "application/json"},
            timeout=15,
        )
        if resp.status_code != 200:
            return offres
        data = resp.json()
        for item in data.get("resultats", []):
            offres.append({
                "source": "APEC",
                "titre": item.get("intitule", ""),
                "entreprise": item.get("nomEntreprise", "N/A"),
                "lieu": item.get("lieuDeLocalisation", ""),
                "salaire": item.get("salaireLibelle", ""),
                "lien": f"https://www.apec.fr/candidat/recherche-emploi.html/emploi/{item.get('numOffre','')}",
                "description": item.get("texteBrief", ""),
            })
    except Exception as e:
        log.warning(f"Erreur APEC: {e}")
    log.info(f"APEC [{poste}] → {len(offres)} offres")
    return offres


def scrape_france_travail(poste, zone_code=""):
    """France Travail (ex Pôle Emploi) — API officielle."""
    offres = []
    # API ouverte sans clé pour les requêtes basiques
    url = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"
    params = {
        "motsCles": poste,
        "range": f"0-{CONFIG['max_offres_par_source']-1}",
        "sort": "1",
    }
    if zone_code:
        params["departement"] = zone_code
    try:
        # Fallback scraping si API non disponible
        url_html = "https://candidat.francetravail.fr/offres/recherche"
        params_html = {"motsCles": poste, "offresPartenaires": "true", "tri": "1"}
        resp = safe_get(url_html, params=params_html)
        if resp:
            soup = BeautifulSoup(resp.text, "lxml")
            cards = soup.select("li.result")[:CONFIG["max_offres_par_source"]]
            for card in cards:
                titre_el = card.select_one("h2.media-heading")
                entreprise_el = card.select_one("p.subtext")
                lieu_el = card.select_one("span.location")
                lien_el = card.select_one("a[href*='/offres/']")
                if not titre_el:
                    continue
                offres.append({
                    "source": "France Travail",
                    "titre": titre_el.get_text(strip=True),
                    "entreprise": entreprise_el.get_text(strip=True) if entreprise_el else "N/A",
                    "lieu": lieu_el.get_text(strip=True) if lieu_el else "",
                    "salaire": "",
                    "lien": "https://candidat.francetravail.fr" + lien_el.get("href","") if lien_el else "",
                    "description": "",
                })
    except Exception as e:
        log.warning(f"Erreur France Travail: {e}")
    log.info(f"France Travail [{poste}] → {len(offres)} offres")
    return offres


def scrape_hellowork(poste, zone):
    """HelloWork — scraping HTML."""
    offres = []
    slug_poste = quote_plus(poste)
    slug_zone = quote_plus(zone)
    url = f"https://www.hellowork.com/fr-fr/emploi/recherche.html?k={slug_poste}&l={slug_zone}&d=1"
    resp = safe_get(url)
    if not resp:
        return offres
    soup = BeautifulSoup(resp.text, "lxml")
    cards = soup.select("li[data-id]")[:CONFIG["max_offres_par_source"]]
    for card in cards:
        try:
            titre_el = card.select_one("a.job-title, h3")
            lieu_el = card.select_one("span.location, p.location")
            entreprise_el = card.select_one("span.company, p.company")
            salaire_el = card.select_one("span.salary")
            lien_el = card.select_one("a[href]")
            if not titre_el:
                continue
            lien = lien_el.get("href","") if lien_el else ""
            if not lien.startswith("http"):
                lien = "https://www.hellowork.com" + lien
            offres.append({
                "source": "HelloWork",
                "titre": titre_el.get_text(strip=True),
                "entreprise": entreprise_el.get_text(strip=True) if entreprise_el else "N/A",
                "lieu": lieu_el.get_text(strip=True) if lieu_el else zone,
                "salaire": salaire_el.get_text(strip=True) if salaire_el else "",
                "lien": lien,
                "description": "",
            })
        except Exception as e:
            log.debug(f"Erreur parsing HelloWork card: {e}")
    log.info(f"HelloWork [{poste}/{zone}] → {len(offres)} offres")
    return offres


def scrape_linkedin_rss(poste, zone):
    """LinkedIn Jobs — via flux RSS public (pas d'auth)."""
    offres = []
    url = "https://www.linkedin.com/jobs/search"
    params = {
        "keywords": poste,
        "location": zone,
        "f_TPR": "r86400",  # dernières 24h
        "sortBy": "DD",
    }
    resp = safe_get(url, params=params)
    if not resp:
        return offres
    soup = BeautifulSoup(resp.text, "lxml")
    cards = soup.select("div.base-card")[:CONFIG["max_offres_par_source"]]
    for card in cards:
        try:
            titre_el = card.select_one("h3.base-search-card__title")
            entreprise_el = card.select_one("h4.base-search-card__subtitle")
            lieu_el = card.select_one("span.job-search-card__location")
            lien_el = card.select_one("a.base-card__full-link")
            if not titre_el:
                continue
            offres.append({
                "source": "LinkedIn",
                "titre": titre_el.get_text(strip=True),
                "entreprise": entreprise_el.get_text(strip=True) if entreprise_el else "N/A",
                "lieu": lieu_el.get_text(strip=True) if lieu_el else zone,
                "salaire": "",
                "lien": lien_el.get("href","") if lien_el else "",
                "description": "",
            })
        except Exception as e:
            log.debug(f"Erreur parsing LinkedIn card: {e}")
    log.info(f"LinkedIn [{poste}/{zone}] → {len(offres)} offres")
    return offres


def scrape_randstad(poste, zone):
    """Randstad — scraping HTML."""
    offres = []
    url = "https://www.randstad.fr/offres-emploi/"
    params = {"q": poste, "l": zone}
    resp = safe_get(url, params=params)
    if not resp:
        return offres
    soup = BeautifulSoup(resp.text, "lxml")
    cards = soup.select("article.job-offer")[:CONFIG["max_offres_par_source"]]
    for card in cards:
        try:
            titre_el = card.select_one("h2, h3")
            lien_el = card.select_one("a[href]")
            lieu_el = card.select_one("span.location")
            salaire_el = card.select_one("span.salary")
            if not titre_el:
                continue
            lien = lien_el.get("href","") if lien_el else ""
            if not lien.startswith("http"):
                lien = "https://www.randstad.fr" + lien
            offres.append({
                "source": "Randstad",
                "titre": titre_el.get_text(strip=True),
                "entreprise": "N/A",
                "lieu": lieu_el.get_text(strip=True) if lieu_el else zone,
                "salaire": salaire_el.get_text(strip=True) if salaire_el else "",
                "lien": lien,
                "description": "",
            })
        except Exception as e:
            log.debug(f"Erreur parsing Randstad: {e}")
    log.info(f"Randstad [{poste}/{zone}] → {len(offres)} offres")
    return offres

# ── Collecte toutes plateformes ───────────────────────────────────────────────

def collect_all_jobs():
    """Lance le scraping en parallèle sur toutes les plateformes et zones."""
    all_jobs = []

    zones_fr = ["Paris", "Île-de-France", "Bourges", "Dijon", "Troyes", "Besançon"]
    zones_inter = ["Genève", "Lausanne", "Luxembourg", "Dubai", "Riyadh", "Dakar"]
    zones = zones_fr + zones_inter

    for poste in CONFIG["postes"]:
        # APEC — couverture nationale France
        all_jobs += scrape_apec(poste)
        time.sleep(1)

        # France Travail
        all_jobs += scrape_france_travail(poste)
        time.sleep(1)

        for zone in zones:
            log.info(f"Scraping {poste} / {zone}...")
            all_jobs += scrape_indeed(poste, zone)
            time.sleep(1)
            all_jobs += scrape_hellowork(poste, zone)
            time.sleep(1)
            all_jobs += scrape_linkedin_rss(poste, zone)
            time.sleep(1)
            all_jobs += scrape_randstad(poste, zone)
            time.sleep(1)

    log.info(f"Total brut collecté : {len(all_jobs)} offres")
    return all_jobs

# ── Déduplication ─────────────────────────────────────────────────────────────

def deduplicate(jobs):
    """Supprime les doublons inter-plateformes par titre+entreprise."""
    seen = set()
    unique = []
    for j in jobs:
        key = (j["titre"].lower().strip(), j["entreprise"].lower().strip())
        if key not in seen:
            seen.add(key)
            unique.append(j)
    log.info(f"Après déduplication : {len(unique)} offres uniques")
    return unique

# ── Filtre géographique ───────────────────────────────────────────────────────

def filtre_geo(jobs):
    """Garde uniquement les offres dans les zones autorisées."""
    zones_ok = CONFIG["zones_france"] + CONFIG["zones_international"]
    result = []
    for j in jobs:
        lieu = j.get("lieu", "").lower()
        if any(z.lower() in lieu for z in zones_ok):
            result.append(j)
    log.info(f"Après filtre géo : {len(result)} offres")
    return result

# ── Scoring IA via Claude ─────────────────────────────────────────────────────

def score_jobs_with_claude(jobs):
    """
    Envoie les offres à Claude pour scoring et filtrage intelligent.
    Retourne les offres scorées, triées par pertinence décroissante.
    """
    if not jobs:
        return []

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    # On envoie par lots de 15 pour éviter les tokens limits
    scored = []
    batch_size = 15

    for i in range(0, len(jobs), batch_size):
        batch = jobs[i:i+batch_size]
        jobs_json = json.dumps(
            [{"id": idx, "titre": j["titre"], "entreprise": j["entreprise"],
              "lieu": j["lieu"], "salaire": j["salaire"],
              "description": j.get("description","")[:300]}
             for idx, j in enumerate(batch)],
            ensure_ascii=False
        )

        prompt = f"""Tu es un agent de recherche d'emploi spécialisé. Analyse ces offres et attribue un score de pertinence de 0 à 100 pour un candidat avec ce profil :

PROFIL CANDIDAT :
- Postes visés : Chef de projet technique/programme, Directeur technique
- Compétences : électronique HW/SW, systèmes embarqués, intégration systèmes, logiciel, gestion de projet technique
- Zones acceptées : Île-de-France, Centre-Val de Loire, Bourgogne-Franche-Comté, Aube, Suisse romande, Luxembourg, Arabie Saoudite, Émirats arabes unis, Sénégal
- Salaire minimum : 60 000 € brut/an (ou équivalent local)

OFFRES À SCORER :
{jobs_json}

Réponds UNIQUEMENT avec un JSON valide, sans commentaires ni backticks :
[{{"id": 0, "score": 85, "raison": "Correspond parfaitement au profil"}}, ...]

Critères de scoring :
- 80-100 : Correspond parfaitement (titre exact + compétences + zone + salaire OK)
- 60-79 : Bonne correspondance (quelques critères manquants)
- 40-59 : Correspondance partielle
- 0-39 : Hors critères (à écarter)"""

        try:
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",  # Haiku = moins cher pour le scoring
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            raw = response.content[0].text.strip()
            scores = json.loads(raw)
            for s in scores:
                idx = s.get("id", 0)
                if idx < len(batch):
                    batch[idx]["score"] = s.get("score", 0)
                    batch[idx]["raison_ia"] = s.get("raison", "")
                    if batch[idx]["score"] >= CONFIG["score_min_ia"]:
                        scored.append(batch[idx])
        except Exception as e:
            log.error(f"Erreur scoring Claude: {e}")
            # Fallback : inclure toutes les offres du batch avec score 50
            for j in batch:
                j["score"] = 50
                j["raison_ia"] = "Score manuel (erreur IA)"
                scored.append(j)

        time.sleep(1)

    scored.sort(key=lambda x: x.get("score", 0), reverse=True)
    log.info(f"Après scoring IA : {len(scored)} offres retenues (score ≥ {CONFIG['score_min_ia']})")
    return scored

# ── Template email HTML ───────────────────────────────────────────────────────

def build_email_html(jobs, date_str):
    """Construit le HTML du digest email."""

    def score_color(s):
        if s >= 80: return "#0a6b3d"
        if s >= 60: return "#856404"
        return "#5f5e5a"

    def score_bg(s):
        if s >= 80: return "#d1fae5"
        if s >= 60: return "#fef3c7"
        return "#f1efe8"

    cards_html = ""
    for j in jobs[:25]:  # max 25 offres dans le mail
        score = j.get("score", 0)
        cards_html += f"""
        <div style="background:#ffffff;border:1px solid #e5e3db;border-radius:10px;
                    padding:16px;margin-bottom:12px;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;
                      margin-bottom:6px;">
            <strong style="font-size:15px;color:#1a1a18;">{j['titre']}</strong>
            <span style="background:{score_bg(score)};color:{score_color(score)};
                         font-size:11px;font-weight:600;padding:3px 8px;
                         border-radius:12px;white-space:nowrap;margin-left:8px;">
              Score {score}/100
            </span>
          </div>
          <p style="margin:0 0 6px;font-size:13px;color:#5f5e5a;">
            🏢 {j['entreprise']} &nbsp;·&nbsp; 📍 {j['lieu']}
            {f"&nbsp;·&nbsp; 💶 {j['salaire']}" if j.get('salaire') else ""}
          </p>
          <p style="margin:0 0 10px;font-size:12px;color:#73726c;font-style:italic;">
            {j.get('raison_ia','')[:120]}
          </p>
          <div style="display:flex;gap:8px;align-items:center;">
            <span style="background:#f1efe8;color:#5f5e5a;font-size:11px;
                         padding:2px 8px;border-radius:10px;">{j['source']}</span>
            <a href="{j['lien']}" style="font-size:12px;color:#185fa5;
               text-decoration:none;font-weight:500;">
              Voir l'offre →
            </a>
          </div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Veille emploi — {date_str}</title>
</head>
<body style="margin:0;padding:0;background:#f5f3ee;font-family:Arial,sans-serif;">
  <div style="max-width:600px;margin:0 auto;padding:20px;">

    <!-- Header -->
    <div style="background:#1a1a18;border-radius:12px;padding:24px;
                margin-bottom:20px;text-align:center;">
      <h1 style="color:#ffffff;font-size:20px;margin:0 0 6px;">
        🔍 Veille Emploi — {date_str}
      </h1>
      <p style="color:#9c9a92;font-size:13px;margin:0;">
        Chef de projet technique · Directeur technique · {len(jobs)} offre(s) sélectionnée(s)
      </p>
    </div>

    <!-- Stats bar -->
    <div style="display:flex;gap:10px;margin-bottom:20px;">
      <div style="flex:1;background:#d1fae5;border-radius:8px;padding:10px;text-align:center;">
        <div style="font-size:20px;font-weight:700;color:#0a6b3d;">
          {len([j for j in jobs if j.get('score',0)>=80])}
        </div>
        <div style="font-size:11px;color:#0a6b3d;">Score 80+</div>
      </div>
      <div style="flex:1;background:#fef3c7;border-radius:8px;padding:10px;text-align:center;">
        <div style="font-size:20px;font-weight:700;color:#856404;">
          {len([j for j in jobs if 60<=j.get('score',0)<80])}
        </div>
        <div style="font-size:11px;color:#856404;">Score 60-79</div>
      </div>
      <div style="flex:1;background:#e6f1fb;border-radius:8px;padding:10px;text-align:center;">
        <div style="font-size:20px;font-weight:700;color:#185fa5;">{len(jobs)}</div>
        <div style="font-size:11px;color:#185fa5;">Total</div>
      </div>
    </div>

    <!-- Offres -->
    {cards_html if cards_html else
      '<p style="text-align:center;color:#888;padding:40px 0;">Aucune offre trouvée aujourd'hui.</p>'}

    <!-- Footer -->
    <div style="text-align:center;padding:20px 0;border-top:1px solid #e5e3db;
                margin-top:20px;">
      <p style="font-size:11px;color:#9c9a92;margin:0;">
        Généré automatiquement par votre agent IA · GitHub Actions<br>
        Plateformes : LinkedIn · Indeed · APEC · France Travail · HelloWork · Randstad
      </p>
    </div>

  </div>
</body>
</html>"""

# ── Envoi email ───────────────────────────────────────────────────────────────

def send_email(jobs, date_str):
    """Envoie le digest via SMTP (Gmail App Password ou Yahoo)."""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🔍 Veille emploi {date_str} — {len(jobs)} offre(s)"
    msg["From"] = CONFIG["smtp_user"]
    msg["To"] = CONFIG["email_dest"]

    # Version texte simple
    text_body = f"Veille emploi du {date_str}\n\n"
    for j in jobs[:25]:
        text_body += f"[{j.get('score',0)}/100] {j['titre']} — {j['entreprise']} ({j['lieu']})\n"
        text_body += f"  {j['lien']}\n\n"

    # Version HTML
    html_body = build_email_html(jobs, date_str)

    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        with smtplib.SMTP(CONFIG["smtp_host"], CONFIG["smtp_port"]) as server:
            server.ehlo()
            server.starttls()
            server.login(CONFIG["smtp_user"], CONFIG["smtp_password"])
            server.sendmail(CONFIG["smtp_user"], CONFIG["email_dest"], msg.as_string())
        log.info(f"✅ Email envoyé à {CONFIG['email_dest']}")
    except Exception as e:
        log.error(f"❌ Erreur envoi email: {e}")
        raise

# ── Point d'entrée ────────────────────────────────────────────────────────────

def main():
    date_str = datetime.now(timezone.utc).strftime("%d/%m/%Y")
    log.info(f"=== Démarrage agent veille emploi — {date_str} ===")

    # 1. Collecte
    raw_jobs = collect_all_jobs()

    # 2. Déduplication
    jobs = deduplicate(raw_jobs)

    # 3. Filtre géographique
    jobs = filtre_geo(jobs)

    # 4. Scoring IA
    if os.environ.get("ANTHROPIC_API_KEY"):
        jobs = score_jobs_with_claude(jobs)
    else:
        log.warning("ANTHROPIC_API_KEY non définie, scoring IA désactivé")
        for j in jobs:
            j["score"] = 50
            j["raison_ia"] = "Score par défaut"

    # 5. Envoi email
    send_email(jobs, date_str)
    log.info(f"=== Terminé. {len(jobs)} offres envoyées. ===")


if __name__ == "__main__":
    main()

