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
        "COLLECTE:",
        len(jobs)
    )


    jobs = score_jobs(jobs)


    print(
        "SCORE TERMINE"
    )


    jobs = filter_jobs(jobs)


    print(
        "OFFRES FINALES:",
        len(jobs)
    )


    for job in jobs[:10]:

        print(

            job.get("title"),

            job.get("company"),

            job.get("score")

        )


    subject,html = render_email(jobs)


    send_email(

        subject=subject,

        html=html,

        text="Rapport quotidien IA Data"

    )



if __name__=="__main__":

    main()