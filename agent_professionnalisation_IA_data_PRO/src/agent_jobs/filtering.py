from .config import BLOCKED_COMPANIES



def filter_jobs(jobs):


    result=[]


    for job in jobs:


        company = job.get(
            "company",
            ""
        ).lower()



        if any(

            bad in company

            for bad in BLOCKED_COMPANIES

        ):

            continue



        if not job.get(
            "title"
        ):

            continue



        if not job.get(
            "link"
        ):

            continue



        if not job["link"].startswith(
            "http"
        ):

            continue



        result.append(job)



    result.sort(

        key=lambda x:

        x.get(
            "score",
            0
        ),

        reverse=True

    )



    return result[:20]