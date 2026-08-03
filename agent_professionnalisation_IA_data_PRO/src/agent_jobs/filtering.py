from .config import (
    TARGET_ROLES,
    EUROPE_LOCATIONS,
    FORBIDDEN_WORDS
)



def filter_jobs(jobs):


    results = []


    for job in jobs:


        text = (

            job.get("title","")

            + " "

            + job.get("description","")

            + " "

            + job.get("location","")

            + " "

            + job.get("company","")

        ).lower()



        # URL obligatoire

        if not job.get("link"):

            continue



        if not job["link"].startswith("http"):

            continue



        # Poste IA/Data obligatoire

        if not any(

            role in text

            for role in TARGET_ROLES

        ):

            continue



        # Europe prioritaire

        if not any(

            place in text

            for place in EUROPE_LOCATIONS

        ):

            continue



        # suppression métiers hors cible

        if any(

            word in text

            for word in FORBIDDEN_WORDS

        ):

            continue



        results.append(job)



    return results