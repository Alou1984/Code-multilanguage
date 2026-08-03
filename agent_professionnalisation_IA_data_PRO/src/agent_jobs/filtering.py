from .config import (
    TARGET_ROLES,
    EUROPE_KEYWORDS,
    FORBIDDEN_KEYWORDS
)



def filter_jobs(jobs):


    results=[]


    print(
        "DEBUT FILTRE",
        len(jobs)
    )



    for job in jobs:


        text=(

            job.get("title","")

            +" "

            +job.get("description","")

            +" "

            +job.get("location","")

            +" "

            +job.get("company","")

            +" "

            +job.get("contract","")

        ).lower()



        if not job.get("link"):

            continue



        # métier IA/Data

        if not any(

            role in text

            for role in TARGET_ROLES

        ):


            print(
                "ROLE REFUSE:",
                job.get("title")
            )


            continue



        # Europe

        if not any(

            place in text

            for place in EUROPE_KEYWORDS

        ):


            print(
                "PAYS REFUSE:",
                job.get("title"),
                job.get("location")
            )


            continue



        # hors domaine

        if any(

            bad in text

            for bad in FORBIDDEN_KEYWORDS

        ):


            print(
                "MOT REFUSE:",
                job.get("title")
            )


            continue



        results.append(job)



    print(

        "APRES FILTRE:",

        len(results)

    )


    return results