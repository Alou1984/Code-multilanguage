from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from itertools import product
from urllib.parse import quote_plus
import os
import re
import requests


@dataclass(frozen=True)
class JobResult:
    title: str
    company: str
    location: str
    source: str
    url: str
    snippet: str
    published: str | None = None


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def build_core_queries(config: dict) -> list[str]:
    contracts = config["contracts"]
    roles = config["roles"]
    skills = config["skills"]
    # On limite volontairement les combinaisons pour éviter trop d'appels/API.
    main_roles = roles[:8]
    main_skills = skills[:10]
    queries: list[str] = []
    for contract, role in product(contracts, main_roles):
        queries.append(f'"{contract}" "{role}"')
    for contract, skill in product(contracts[:4], main_skills):
        queries.append(f'"{contract}" "{skill}" data IA')
    # Déduplication en conservant l'ordre.
    return list(dict.fromkeys(queries))


def build_locations(config: dict) -> list[str]:
    locations: list[str] = []
    for values in config["locations"].values():
        locations.extend(values)
    return list(dict.fromkeys(locations))


def build_direct_search_links(config: dict, limit: int = 120) -> list[JobResult]:
    """Fallback sans clé API : génère des liens de recherche ciblés par site."""
    results: list[JobResult] = []
    queries = build_core_queries(config)
    locations = build_locations(config)
    sources = config["sources"]

    for source in sources:
        for query in queries[:8]:
            for location in locations[:5]:
                url = source["search_url"].format(
                    query=quote_plus(query),
                    location=quote_plus(location),
                )
                results.append(
                    JobResult(
                        title=f"Recherche ciblée: {query}",
                        company="Recherche directe",
                        location=location,
                        source=source["name"],
                        url=url,
                        snippet=(
                            "Lien de recherche prêt à cliquer. Ajoute une clé SERPAPI_API_KEY "
                            "pour récupérer automatiquement des offres individuelles."
                        ),
                        published=None,
                    )
                )
                if len(results) >= limit:
                    return results
    return results


def serpapi_search(config: dict, max_results_per_query: int = 5) -> list[JobResult]:
    """Recherche d'offres via SerpApi Google Search.

    Nécessite le secret GitHub SERPAPI_API_KEY. Cette méthode évite de scraper directement
    LinkedIn/Indeed/Glassdoor et s'appuie sur une API de recherche.
    """
    api_key = os.getenv("SERPAPI_API_KEY", "").strip()
    if not api_key:
        return []

    queries = build_core_queries(config)[:20]
    locations = build_locations(config)[:10]
    sources = config["sources"]
    output: list[JobResult] = []

    session = requests.Session()
    for source in sources:
        for query in queries:
            location_filter = " OR ".join([f'"{loc}"' for loc in locations[:6]])
            q = f'{source["domain_query"]} {query} ({location_filter})'
            params = {
                "engine": "google",
                "q": q,
                "api_key": api_key,
                "hl": "fr",
                "gl": "fr",
                "num": max_results_per_query,
            }
            try:
                resp = session.get("https://serpapi.com/search.json", params=params, timeout=25)
                resp.raise_for_status()
                data = resp.json()
            except Exception as exc:  # noqa: BLE001 - on continue les autres sources
                output.append(
                    JobResult(
                        title=f"Erreur recherche {source['name']}",
                        company="SerpApi",
                        location="",
                        source=source["name"],
                        url=source["search_url"].format(query=quote_plus(query), location="France"),
                        snippet=f"Erreur temporaire: {exc}",
                    )
                )
                continue

            for item in data.get("organic_results", [])[:max_results_per_query]:
                url = item.get("link")
                if not url:
                    continue
                output.append(
                    JobResult(
                        title=normalize_space(item.get("title", "Offre potentielle")),
                        company=normalize_space(item.get("source", "")) or source["name"],
                        location="France / Suisse romande",
                        source=source["name"],
                        url=url,
                        snippet=normalize_space(item.get("snippet", "")),
                        published=datetime.utcnow().strftime("%Y-%m-%d"),
                    )
                )
    # Déduplication par URL.
    unique: dict[str, JobResult] = {}
    for item in output:
        unique.setdefault(item.url, item)
    return list(unique.values())


def collect_jobs(config: dict) -> list[JobResult]:
    max_results = int(os.getenv("MAX_RESULTS_PER_QUERY", "5"))
    api_results = serpapi_search(config, max_results_per_query=max_results)
    if api_results:
        return api_results
    return build_direct_search_links(config)
