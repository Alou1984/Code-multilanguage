#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Daily Alternance Cyber Agent
Projet gratuit basé sur GitHub Actions + Python.

Objectif :
- Chercher chaque jour des offres stage / internship / graduate program / alternance / apprentissage.
- Cibler cybersécurité, ingénieur, expert, chef de projet.
- Cibler France et Suisse romande.
- Envoyer les liens par email à 08h00 heure de Paris.

Important :
- LinkedIn, Glassdoor et certains job boards bloquent souvent le scraping automatique.
- Ce script évite le scraping agressif et utilise des flux publics + liens de recherche directe.
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import smtplib
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Iterable
from urllib.parse import quote_plus

import feedparser
import requests
from bs4 import BeautifulSoup
from zoneinfo import ZoneInfo


CONFIG = {
    "candidate_email": "papalassane2003@yahoo.fr",
    "target_program": "Mastère Spécialisé® Expert en Cybersécurité",
    "target_start": "septembre 2026",
    "training_rhythm": "Alternance : 1 semaine par mois en cours / 3 semaines en entreprise",
    "timezone": "Europe/Paris",
    "send_hour_local": 8,
    "max_results_email": 60,
    "min_score": 4,

    "contract_terms": [
        "stage",
        "internship",
        "intership",
        "graduate program",
        "alternance",
        "apprentissage",
        "apprenticeship",
        "stagiaire",
        "apprenti",
    ],

    "role_terms": [
        "cybersécurité",
        "cybersecurite",
        "cybersecurity",
        "sécurité informatique",
        "securite informatique",
        "ingénieur cybersécurité",
        "ingenieur cybersecurite",
        "expert cybersécurité",
        "chef de projet cybersécurité",
        "project manager cybersecurity",
        "security engineer",
        "soc",
        "iam",
        "grc",
        "risk",
        "compliance",
        "pentest",
        "cloud security",
        "application security",
        "industrial cybersecurity",
    ],

    "engineering_terms": [
        "électronique",
        "electronique",
        "hardware",
        "hw",
        "software",
        "sw",
        "intégration système",
        "integration systeme",
        "système embarqué",
        "systeme embarque",
        "embedded",
        "logiciel",
        "ia",
        "ai",
        "robotique",
        "robotics",
        "ot",
        "iot",
        "industrie",
        "automatisme",
    ],

    "locations": [
        "Île-de-France",
        "Ile-de-France",
        "Paris",
        "Nanterre",
        "La Défense",
        "Courbevoie",
        "Puteaux",
        "Massy",
        "Saclay",
        "Centre-Val de Loire",
        "Orléans",
        "Tours",
        "Bourges",
        "Chartres",
        "Bourgogne-Franche-Comté",
        "Bourgogne Franche Comte",
        "Dijon",
        "Besançon",
        "Belfort",
        "Aube",
        "Troyes",
        "Suisse romande",
        "Genève",
        "Geneve",
        "Geneva",
        "Lausanne",
        "Vaud",
        "Neuchâtel",
        "Neuchatel",
        "Fribourg",
        "Valais",
        "Jura",
    ],

    "source_domains": [
        "linkedin.com/jobs",
        "glassdoor.fr",
        "indeed.fr",
        "indeed.com",
        "apec.fr",
        "hellowork.com",
        "teamtailor.com",
        "jobup.ch",
        "francetravail.fr",
        "randstad.fr",
        "careers.totalenergies.com",
        "totalenergies.com/careers",
    ],
}


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SEEN_FILE = DATA_DIR / "seen_jobs.json"


@dataclass
class Job:
    title: str
    link: str
    source: str
    summary: str = ""
    published: str = ""
    score: int = 0
    matched: list[str] | None = None


def clean_html(text: str) -> str:
    return BeautifulSoup(text or "", "html.parser").get_text(" ", strip=True)


def normalize(text: str) -> str:
    text = html.unescape(text or "")
    text = clean_html(text)
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text


def contains_term(text: str, term: str) -> bool:
    return normalize(term) in text


def score_job(job: Job) -> tuple[int, list[str]]:
    text = normalize(f"{job.title} {job.summary} {job.link}")
    matched: list[str] = []
    score = 0

    groups = [
        (CONFIG["contract_terms"], 4),
        (CONFIG["role_terms"], 5),
        (CONFIG["engineering_terms"], 2),
        (CONFIG["locations"], 3),
    ]

    for terms, weight in groups:
        for term in terms:
            if contains_term(text, term):
                score += weight
                matched.append(term)

    bonus_terms = [
        "cyber",
        "security",
        "sécurité",
        "securite",
        "alternance",
        "apprentissage",
        "stage",
        "intern",
        "graduate",
        "project",
        "chef de projet",
        "ingénieur",
        "ingenieur",
        "engineer",
    ]

    for term in bonus_terms:
        if term in text:
            score += 1

    negative_terms = [
        "senior only",
        "10 ans minimum",
        "cdi uniquement",
        "no internship",
        "stage non accepté",
        "alternance non acceptée",
    ]

    for term in negative_terms:
        if term in text:
            score -= 5

    return score, sorted(set(matched), key=str.lower)


def google_news_rss_url(query: str) -> str:
    return (
        "https://news.google.com/rss/search?q="
        + quote_plus(query)
        + "&hl=fr&gl=FR&ceid=FR:fr"
    )


def build_queries() -> list[str]:
    contract_part = "(" + " OR ".join([f'"{x}"' for x in CONFIG["contract_terms"]]) + ")"
    cyber_part = '("cybersécurité" OR cybersecurite OR cybersecurity OR "security engineer" OR SOC OR GRC OR IAM)'
    location_part = '("Ile-de-France" OR Paris OR "Centre-Val de Loire" OR Bourgogne OR Aube OR "Suisse romande" OR Genève OR Lausanne)'

    queries: list[str] = []

    for domain in CONFIG["source_domains"]:
        queries.append(f"site:{domain} {contract_part} {cyber_part} {location_part}")

    queries.extend(
        [
            f'{contract_part} {cyber_part} {location_part}',
            'alternance cybersécurité ingénieur Paris "Ile-de-France"',
            'stage cybersécurité ingénieur électronique logiciel système embarqué France Suisse romande',
            'graduate program cybersecurity France Switzerland',
            'apprentissage cybersécurité chef de projet sécurité informatique',
            'TotalEnergies alternance cybersécurité ingénieur',
            'Randstad alternance cybersécurité ingénieur',
            'APEC alternance cybersécurité chef de projet',
            'HelloWork stage cybersécurité Ile-de-France',
            'France Travail apprentissage cybersécurité Paris',
            'JobUp cybersecurity internship Geneva Lausanne',
        ]
    )

    return queries


def fetch_jobs_from_rss() -> list[Job]:
    jobs: list[Job] = []
    headers = {"User-Agent": "Mozilla/5.0 AlternanceAgent/1.0"}

    for query in build_queries():
        url = google_news_rss_url(query)
        try:
            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()
            feed = feedparser.parse(response.text)
        except Exception as exc:
            print(f"[WARN] RSS failed: {query[:90]}... error={exc}", file=sys.stderr)
            continue

        for entry in feed.entries[:20]:
            title = getattr(entry, "title", "").strip()
            link = getattr(entry, "link", "").strip()
            summary = getattr(entry, "summary", "").strip()
            published = getattr(entry, "published", "").strip()

            if not title or not link:
                continue

            source = "Google News RSS"
            if hasattr(entry, "source") and getattr(entry.source, "title", ""):
                source = entry.source.title

            jobs.append(
                Job(
                    title=title,
                    link=link,
                    source=source,
                    summary=summary,
                    published=published,
                )
            )

    return jobs


def add_direct_search_links() -> list[Job]:
    direct_queries = [
        (
            "LinkedIn",
            "https://www.linkedin.com/jobs/search/?keywords="
            + quote_plus("alternance stage cybersécurité ingénieur")
            + "&location="
            + quote_plus("Île-de-France, France"),
        ),
        (
            "Indeed France",
            "https://fr.indeed.com/jobs?q="
            + quote_plus("alternance stage cybersécurité ingénieur")
            + "&l="
            + quote_plus("Île-de-France"),
        ),
        (
            "APEC",
            "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles="
            + quote_plus("alternance cybersécurité ingénieur"),
        ),
        (
            "HelloWork",
            "https://www.hellowork.com/fr-fr/emploi/recherche.html?k="
            + quote_plus("alternance cybersécurité ingénieur"),
        ),
        (
            "France Travail",
            "https://candidat.francetravail.fr/offres/recherche?motsCles="
            + quote_plus("alternance cybersécurité"),
        ),
        (
            "JobUp Suisse",
            "https://www.jobup.ch/fr/emplois/?term="
            + quote_plus("cybersécurité alternance stage"),
        ),
        (
            "Teamtailor",
            "https://www.google.com/search?q="
            + quote_plus("site:teamtailor.com cybersécurité alternance stage France Suisse"),
        ),
        (
            "Glassdoor",
            "https://www.glassdoor.fr/Emploi/jobs.htm?sc.keyword="
            + quote_plus("alternance cybersécurité"),
        ),
        (
            "Randstad",
            "https://www.randstad.fr/emploi/s-cybersecurite/",
        ),
        (
            "TotalEnergies Careers",
            "https://careers.totalenergies.com/fr/rechercher-des-offres?keywords="
            + quote_plus("cybersécurité alternance"),
        ),
        (
            "Suisse romande Google",
            "https://www.google.com/search?q="
            + quote_plus("stage internship cybersecurity Geneva Lausanne alternance Suisse romande"),
        ),
    ]

    jobs: list[Job] = []
    for name, link in direct_queries:
        jobs.append(
            Job(
                title=f"Lien de recherche directe - {name}",
                link=link,
                source=name,
                summary="Lien utile pour vérifier les offres non accessibles par flux public ou protégées contre le scraping.",
                published="",
                score=CONFIG["min_score"],
                matched=["recherche directe"],
            )
        )

    return jobs


def deduplicate(jobs: Iterable[Job]) -> list[Job]:
    seen_hashes = set()
    unique: list[Job] = []

    for job in jobs:
        key = hashlib.sha256((job.title + job.link).encode("utf-8")).hexdigest()
        if key in seen_hashes:
            continue
        seen_hashes.add(key)
        unique.append(job)

    return unique


def load_seen() -> set[str]:
    if not SEEN_FILE.exists():
        return set()

    try:
        data = json.loads(SEEN_FILE.read_text(encoding="utf-8"))
        return set(data.get("seen_links", []))
    except Exception:
        return set()


def save_seen(links: Iterable[str]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    current = load_seen()
    current.update(links)

    SEEN_FILE.write_text(
        json.dumps(
            {
                "updated_at": datetime.now(timezone.utc).isoformat(),
                "seen_links": sorted(current),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def should_send_now() -> bool:
    if os.getenv("FORCE_SEND", "").lower() == "true":
        return True

    now = datetime.now(ZoneInfo(CONFIG["timezone"]))
    return now.hour == CONFIG["send_hour_local"]


def prepare_results() -> list[Job]:
    seen = load_seen()

    jobs = fetch_jobs_from_rss()
    jobs.extend(add_direct_search_links())
    jobs = deduplicate(jobs)

    scored: list[Job] = []
    for job in jobs:
        score, matched = score_job(job)

        if job.score:
            score = max(score, job.score)

        job.score = score
        job.matched = matched or job.matched or []

        if score >= CONFIG["min_score"] and job.link not in seen:
            scored.append(job)

    scored.sort(key=lambda x: x.score, reverse=True)

    if not scored:
        scored = [j for j in jobs if "Lien de recherche directe" in j.title]

    return scored[: CONFIG["max_results_email"]]


def build_email_html(jobs: list[Job]) -> str:
    today = datetime.now(ZoneInfo(CONFIG["timezone"])).strftime("%d/%m/%Y")

    items = []
    for idx, job in enumerate(jobs, start=1):
        matched = ", ".join(job.matched or [])[:300]
        summary = clean_html(job.summary or "")
        summary = html.escape(summary[:500])

        items.append(
            f"""
            <li style="margin-bottom:18px;">
              <strong>{idx}. <a href="{html.escape(job.link)}">{html.escape(job.title)}</a></strong><br/>
              <span><b>Source :</b> {html.escape(job.source)} | <b>Score :</b> {job.score}</span><br/>
              <span><b>Publié :</b> {html.escape(job.published or "non précisé")}</span><br/>
              <span><b>Mots-clés détectés :</b> {html.escape(matched or "recherche directe")}</span><br/>
              <p>{summary}</p>
            </li>
            """
        )

    return f"""
    <html>
      <body>
        <h2>Veille quotidienne alternance/stage cybersécurité - {today}</h2>

        <p>Bonjour,</p>

        <p>
          Voici les liens/offres détectés pour ta recherche :
          <b>stage, internship, graduate program, alternance, apprentissage</b>,
          pour un poste d'<b>expert, ingénieur ou chef de projet en cybersécurité</b>.
        </p>

        <p>
          Formation cible : <b>{html.escape(CONFIG["target_program"])}</b>,
          rentrée <b>{html.escape(CONFIG["target_start"])}</b>.<br/>
          Rythme : <b>{html.escape(CONFIG["training_rhythm"])}</b>.
        </p>

        <h3>Résultats</h3>
        <ol>
          {''.join(items)}
        </ol>

        <hr/>
        <p style="font-size:12px;color:#666;">
          Agent gratuit exécuté par GitHub Actions. Certains sites comme LinkedIn ou Glassdoor peuvent limiter
          l'accès automatique ; l'agent fournit alors des liens de recherche directe.
        </p>
      </body>
    </html>
    """


def send_email(subject: str, html_body: str) -> None:
    smtp_host = os.getenv("SMTP_HOST", "smtp.mail.yahoo.com")
    smtp_port = int(os.getenv("SMTP_PORT", "465"))
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO", CONFIG["candidate_email"])

    if not email_user or not email_password:
        raise RuntimeError(
            "EMAIL_USER et EMAIL_PASSWORD doivent être configurés dans GitHub Secrets."
        )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = email_user
    msg["To"] = email_to
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(email_user, email_password)
        server.sendmail(email_user, [email_to], msg.as_string())


def main() -> None:
    if not should_send_now():
        now = datetime.now(ZoneInfo(CONFIG["timezone"]))
        print(f"Pas encore 08:00 heure de Paris. Heure actuelle : {now.isoformat()}")
        return

    jobs = prepare_results()

    if not jobs:
        print("Aucune offre trouvée.")
        return

    subject_date = datetime.now(ZoneInfo(CONFIG["timezone"])).strftime("%d/%m/%Y")
    subject = f"Offres alternance/stage cybersécurité - {subject_date}"
    html_body = build_email_html(jobs)

    send_email(subject, html_body)

    save_seen(
        [
            job.link
            for job in jobs
            if "Lien de recherche directe" not in job.title
        ]
    )

    print(f"Email envoyé avec {len(jobs)} résultat(s).")


if __name__ == "__main__":
    main()
