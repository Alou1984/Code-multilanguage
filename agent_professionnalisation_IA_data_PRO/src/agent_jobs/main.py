from .search_engine import search_jobs
from .filtering import filter_jobs
from .render import render_email
from .emailer import send_email



def main():

    print(
        "=== AGENT PROFESSIONNALISATION IA DATA START ==="
    )


    # Recherche SERPAPI
    jobs = search_jobs()


    print("==============================")
    print("DEBUG RECHERCHE")
    print("==============================")

    print(
        "Nombre offres brutes :",
        len(jobs)
    )


    for job in jobs[:10]:

        print(
            job.get("title"),
            "|",
            job.get("company"),
            "|",
            job.get("location")
        )



    # Filtrage
    filtered_jobs = filter_jobs(
        jobs
    )


    print("==============================")
    print("DEBUG FILTRE")
    print("==============================")

    print(
        "Nombre offres après filtre :",
        len(filtered_jobs)
    )



    # Sécurité :
    # si le filtre supprime tout,
    # on garde les meilleures offres brutes

    if len(filtered_jobs) == 0 and len(jobs) > 0:

        print(
            "Aucune offre après filtre."
        )

        print(
            "Utilisation des offres brutes."
        )

        filtered_jobs = jobs[:10]



    subject, html = render_email(
        filtered_jobs
    )


    send_email(

        subject=subject,

        html=html,

        text=html

    )


    print(
        "=== AGENT FIN ==="
    )



if __name__ == "__main__":

    main()