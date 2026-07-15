from __future__ import annotations

import os
import time
from urllib.parse import quote_plus

import requests

from .models import JobOffer
from .settings import CONTRACT_TERMS, ROLE_TERMS, SECTOR_TERMS, PRIORITY_COMPANIES, TARGET_SITES


def _queries() -> list[str]:
    contracts = " OR ".join([f'"{t}"' for t in CONTRACT_TERMS])
    roles = " OR ".join([f'"{t}"' for t in ROLE_TERMS[:16]])
    sectors = " OR ".join([f'"{t}"' for t in SECTOR_TERMS[:14]])
    locations = '"Sens" OR "89100" OR "Yonne" OR "Auxerre" OR "Troyes" OR "Montereau" OR "Fontainebleau" OR "Paris" OR "Ile-de-France" OR "Centre-Val de Loire" OR "Bourgogne-Franche-Comté" OR "Suisse romande"'

    queries: list[str] = []
    for site in TARGET_SITES:
        queries.append(f'site:{site} ({contracts}) ({roles}) ({sectors}) ({locations})')

    # Requêtes larges mais ciblées pour ne pas dépendre uniquement des sites.
    queries.extend([
        f'({contracts}) ("data engineer" OR "big data" OR "MLOps" OR "IA") ({locations}) offre emploi',
        f'({contracts}) ("oil and gas" OR énergie OR nucléaire OR minier OR mining) (data OR IA OR logiciel OR embarqué) ({locations})',
        f'({contracts}) ({" OR ".join([quote_plus(c) for c in PRIORITY_COMPANIES[:10]])}) (data OR IA OR software OR ingénieur) France',
    ])
    return queries


def _serpapi_search(query: str, api_key: str, limit: int = 10) -> list[dict]:
    params = {
        "engine": "google",
        "q": query,
        "google_domain": "google.fr",
        "gl": "fr",
        "hl": "fr",
        "num": limit,
        "api_key": api_key,
    }
    response = requests.get("https://serpapi.com/search.json", params=params, timeout=35)
    response.raise_for_status()
    data = response.json()
    return data.get("organic_results", []) or []


def _source_from_url(url: str) -> str:
    for site in TARGET_SITES:
        base = site.replace("www.", "")
        if base.split("/")[0] in url:
            return site
    return "web"


def _parse_offer(result: dict) -> JobOffer | None:
    title = (result.get("title") or "").strip()
    url = (result.get("link") or "").strip()
    snippet = (result.get("snippet") or result.get("rich_snippet", {}).get("top", {}).get("detected_extensions", {}) or "")
    if not title or not url:
        return None
    if isinstance(snippet, dict):
        snippet = " ".join(f"{k}: {v}" for k, v in snippet.items())
    snippet = str(snippet).strip()
    company = ""
    location = ""

    # Heuristique simple depuis le titre : "Poste - Entreprise - Ville"
    parts = [p.strip() for p in title.replace("|", "-").split("-") if p.strip()]
    if len(parts) >= 2:
        company = parts[-2] if len(parts) > 2 else ""
        location = parts[-1]

    return JobOffer(title=title, company=company, location=location, url=url, source=_source_from_url(url), snippet=snippet)


def search_offers() -> list[JobOffer]:
    api_key = os.getenv("SERPAPI_API_KEY", "").strip()
    if not api_key:
        # Sans API, on ne renvoie pas de liens vides ou de fausses offres.
        return []

    offers: list[JobOffer] = []
    seen: set[str] = set()
    for query in _queries():
        try:
            for result in _serpapi_search(query, api_key, limit=10):
                offer = _parse_offer(result)
                if not offer:
                    continue
                key = offer.url.split("?")[0].rstrip("/").lower()
                if key in seen:
                    continue
                seen.add(key)
                offers.append(offer)
        except Exception as exc:
            print(f"WARN search failed: {exc} | query={query[:120]}")
        time.sleep(0.25)
    return offers
