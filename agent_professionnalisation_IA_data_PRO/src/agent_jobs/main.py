import sys

from .search_engine import search_jobs
from .filtering import filter_jobs
from .render import render_email
from .emailer import send_email



def main():

    print(
        "=== AGENT PROFESSIONNALISATION IA DATA START ==="
    )


    # 1 - Recherche des offres
    print(
        "Recherche des offres..."
    )

    jobs = search_jobs()


    print(
        f"Offres brutes trouvées : {len(jobs)}"
    )


    # 2 - Filtrage et scoring
    print(
        "Filtrage des offres ciblées..."
    )

    filtered_jobs = filter_jobs(
        jobs
    )


    print(
        f"Offres ciblées retenues : {len(filtered_jobs)}"
    )


    # 3 - Génération email
    print(
        "Génération du mail..."
    )

    subject, html = render_email(
        filtered_jobs
    )


    # 4 - Envoi email
    print(
        "Envoi email..."
    )

    send_email(

        subject=subject,

        html=html,

        text=html

    )


    print(
        "=== AGENT PROFESSIONNALISATION IA DATA END ==="
    )



if __name__ == "__main__":

    main()