from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

from .emailer import send_email
from .filtering import filter_and_rank
from .render import render
from .search import search_offers


def main() -> None:
    raw_offers = search_offers()
    offers = filter_and_rank(raw_offers)
    today = datetime.now(ZoneInfo("Europe/Paris")).strftime("%d/%m/%Y")
    subject = f"Offres ciblées Big Data IA / alternance-stage — {today}"
    html, text = render(offers)
    print(f"Offres brutes: {len(raw_offers)} | Offres ciblées envoyées: {len(offers)}")
    send_email(subject=subject, html=html, text=text)


if __name__ == "__main__":
    main()
