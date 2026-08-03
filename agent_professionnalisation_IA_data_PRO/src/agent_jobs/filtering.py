from .config import (
    TARGET_ROLES,
    FORBIDDEN_KEYWORDS
)



def filter_jobs(jobs):


    results=[]


    print(
        "FILTRAGE:",
        len(jobs)
    )


    for job in jobs:


        text=(

            job.get("title","")

            +" "

            +job.get("description","")

            +" "

            +job.get("company","")

        ).lower()



        if not job.get("link"):

            continue



        # Vérification IA/Data

        if not any(

            role in text

            for role in TARGET_ROLES

        ):

            continue



        # Exclusion hors domaine

        if any(

            word in text

            for word in FORBIDDEN_KEYWORDS

        ):

            continue



        results.append(job)



    print(

        "APRES FILTRE:",

        len(results)

    )


    return results[:30]