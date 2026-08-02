from .search_engine import search_jobs
from .scoring import score_jobs
from .filtering import filter_jobs
from .render import render_email
from .emailer import send_email



def main():


    jobs = search_jobs()


    jobs = score_jobs(jobs)


    jobs = filter_jobs(jobs)


    subject, html = render_email(
        jobs
    )


    send_email(

        subject=subject,

        html=html,

        text="Offres IA Data"

    )



if __name__ == "__main__":

    main()