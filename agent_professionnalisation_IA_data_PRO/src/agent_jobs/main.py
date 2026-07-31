from .search_engine import search_jobs

from .scoring import score_jobs

from .filtering import filter_jobs

from .render import render_email

from .emailer import send_email




def main():


    print(
        "=== AGENT PROFESSIONNALISATION IA DATA ==="
    )



    jobs = search_jobs()



    print(

        "Offres collectées :",

        len(jobs)

    )



    jobs = score_jobs(
        jobs
    )



    jobs = filter_jobs(
        jobs
    )



    print(

        "Offres envoyées :",

        len(jobs)

    )



    subject, html = render_email(
        jobs
    )



    send_email(

        subject=subject,

        html=html,

        text="Voir version HTML"

    )



if __name__ == "__main__":

    main()