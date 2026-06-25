from __future__ import annotations

import math
import re

from .models import JobOffer
from .settings import (
    CONTRACT_TERMS, ROLE_TERMS, SECTOR_TERMS, PRIORITY_COMPANIES,
    NEARBY_LOCATIONS, HOME_LAT, HOME_LON, RADIUS_KM, MAX_RESULTS_EMAIL
)


def _norm(text: str) -> str:
    return text.lower().replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a").replace("ç", "c")


def _contains_any(text: str, terms: list[str]) -> bool:
    nt = _norm(text)
    return any(_norm(t) in nt for t in terms)


def _distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def infer_distance(text: str) -> float | None:
    nt = _norm(text)
    best: float | None = None
    for name, (lat, lon) in NEARBY_LOCATIONS.items():
        if _norm(name) in nt:
            d = _distance_km(HOME_LAT, HOME_LON, lat, lon)
            if best is None or d < best:
                best = d
    return round(best, 1) if best is not None else None


def score_offer(offer: JobOffer) -> JobOffer | None:
    blob = " ".join([offer.title, offer.company, offer.location, offer.snippet, offer.source])
    nt = _norm(blob)

    # Élimine les résultats non pertinents : pas de contrat cible OU pas de domaine cible.
    has_contract = _contains_any(nt, CONTRACT_TERMS)
    has_role = _contains_any(nt, ROLE_TERMS)
    has_sector = _contains_any(nt, SECTOR_TERMS)
    has_company = _contains_any(nt, PRIORITY_COMPANIES)

    if not has_contract:
        return None
    if not (has_role or has_sector or has_company):
        return None

    score = 0
    if has_contract: score += 25
    if has_role: score += 30
    if has_sector: score += 25
    if has_company: score += 15

    distance = infer_distance(blob)
    if distance is not None:
        if distance <= RADIUS_KM:
            score += 50
        elif distance <= 160:
            score += 20
        else:
            score -= 10
    else:
        # On garde les offres sans distance détectée mais moins prioritaires.
        score -= 5

    # Bonus pour mots très ciblés.
    priority_patterns = [
        r"big data", r"data engineer", r"mlops", r"machine learning", r"ia generative", r"intelligence artificielle",
        r"oil and gas", r"energie", r"nucleaire", r"mining", r"minier", r"embarque", r"robotique"
    ]
    score += sum(8 for p in priority_patterns if re.search(p, nt))

    return JobOffer(
        title=offer.title, company=offer.company, location=offer.location,
        url=offer.url, source=offer.source, snippet=offer.snippet,
        score=score, distance_km=distance
    )


def filter_and_rank(offers: list[JobOffer]) -> list[JobOffer]:
    ranked: list[JobOffer] = []
    seen_titles: set[str] = set()
    for offer in offers:
        scored = score_offer(offer)
        if not scored:
            continue
        key = _norm(scored.title)[:90]
        if key in seen_titles:
            continue
        seen_titles.add(key)
        ranked.append(scored)
    ranked.sort(key=lambda o: (o.distance_km is None, -(o.score), o.distance_km or 9999))
    return ranked[:MAX_RESULTS_EMAIL]
