from .config import (
    TARGET_ROLES,
    FORBIDDEN_KEYWORDS,
    SENIOR_KEYWORDS
)



def filter_jobs(jobs):


    results=[]


    print(
        "DEBUT FILTRE:",
        len(jobs)
    )


    for job in jobs:


        title = job.get(
            "title",
            ""
        ).lower()



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



        # suppression senior

        if any(

            word in title

            for word in SENIOR_KEYWORDS

        ):


            print(
                "REFUS SENIOR:",
                job.get("title")
            )

            continue



        # suppression métiers hors sujet

        if any(

            word in text

            for word in FORBIDDEN_KEYWORDS

        ):


            print(
                "REFUS METIER:",
                job.get("title")
            )

            continue



        # rôle IA/Data obligatoire

        if not any(

            role in text

            for role in TARGET_ROLES

        ):


            print(
                "REFUS ROLE:",
                job.get("title")
            )

            continue



        results.append(job)



    print(

        "APRES FILTRE:",

        len(results)

    )


    return results