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



        # Senior seulement si le titre commence par senior

        if any(

            title.startswith(x)

            for x in SENIOR_KEYWORDS

        ):

            print(
                "REFUS SENIOR:",
                job["title"]
            )

            continue



        # Métiers interdits

        if any(

            word in text

            for word in FORBIDDEN_KEYWORDS

        ):

            print(
                "REFUS METIER:",
                job["title"]
            )

            continue



        # Poste IA/Data

        if not any(

            role in text

            for role in TARGET_ROLES

        ):

            print(
                "REFUS ROLE:",
                job["title"]
            )

            continue



        results.append(job)



    print(

        "APRES FILTRE:",

        len(results)

    )


    return results[:30]