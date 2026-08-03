from .config import (
    TARGET_ROLES,
    FORBIDDEN_KEYWORDS
)



def filter_jobs(jobs):


    results=[]


    print(
        "DEBUT FILTRE:",
        len(jobs)
    )


    for job in jobs:


        text=(

            job.get("title","")

            +" "

            +job.get("description","")

            +" "

            +job.get("company","")

            +" "

            +job.get("location","")

        ).lower()



        if not job.get("link"):

            continue



        # IA/Data obligatoire

        if not any(

            role in text

            for role in TARGET_ROLES

        ):


            print(

                "REFUS ROLE:",

                job.get("title")

            )

            continue



        # suppression métiers hors sujet

        if any(

            bad in text

            for bad in FORBIDDEN_KEYWORDS

        ):


            print(

                "REFUS METIER:",

                job.get("title")

            )

            continue



        results.append(job)



    print(

        "APRES FILTRE:",

        len(results)

    )


    return results[:30]