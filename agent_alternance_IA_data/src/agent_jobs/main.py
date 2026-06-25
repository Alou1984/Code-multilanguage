from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo
import os

from .config import load_config
from .emailer import render_html, render_text, send_email
from .search import collect_jobs
from .state import SentLinksState


def should_run_now() -> bool:
    """GitHub Actions utilise UTC. Le workflow est lancé à 06:00 et 07:00 UTC.
    Cette garde garantit un envoi à 08:00 Europe/Paris même avec le changement d'heure.
    En local, mettre FORCE_RUN=true pour ignorer cette garde.
    """
    if os.getenv("FORCE_RUN", "false").lower() == "true":
        return True
    now_paris = datetime.now(ZoneInfo("Europe/Paris"))
    return now_paris.hour == 8


def main() -> None:
    if not should_run_now():
        print("Hors créneau 08:00 Europe/Paris: pas d'envoi.")
        return

    config = load_config()
    state = SentLinksState()
    results = collect_jobs(config)
    new_results = [item for item in results if state.is_new(item.url)]

    # Si rien de nouveau, on envoie quand même les meilleurs liens de recherche pour garder le rendez-vous quotidien.
    results_to_send = new_results[:80] or results[:40]
    if not results_to_send:
        print("Aucun résultat à envoyer.")
        return

    target_program = config["profile"]["target_program"]
    subject = f"Offres alternance/stage IA & Data — {datetime.now().strftime('%d/%m/%Y')}"
    html = render_html(results_to_send, target_program)
    text = render_text(results_to_send, target_program)

    if os.getenv("DRY_RUN", "false").lower() == "true":
        print(text)
    else:
        send_email(subject=subject, html=html, text=text)
        state.mark_many([item.url for item in results_to_send])
        state.save()
        print(f"Email envoyé avec {len(results_to_send)} liens.")


if __name__ == "__main__":
    main()
