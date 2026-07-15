from dataclasses import dataclass

@dataclass(frozen=True)
class JobOffer:
    title: str
    company: str
    location: str
    url: str
    source: str
    snippet: str = ""
    score: int = 0
    distance_km: float | None = None
