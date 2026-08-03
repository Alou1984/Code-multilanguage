from .config import (
    TARGET_ROLES,
    EUROPE_LOCATIONS,
    VALID_CONTRACTS,
    FORBIDDEN_ROLES,
    FORBIDDEN_LEVELS
)



def filter_jobs(jobs):


    results=[]



    for job in jobs:


        text=(

            job.get("title","")

            +" "

            +job.get("description","")

            +" "

            +job.get("location","")

        ).lower()



        # lien obligatoire

        if not job.get("link"):

            continue



        # métier IA/Data obligatoire

        if not any(

            role in text

            for role in TARGET_ROLES

        ):

            continue



        # Europe obligatoire

        if not any(

            place in text

            for place in EUROPE_LOCATIONS

        ):

            continue



        # contrat obligatoire

        if not any(

            contract in text

            for contract in VALID_CONTRACTS

        ):

            continue



        # métiers interdits

        if any(

            word in text

            for word in FORBIDDEN_ROLES

        ):

            continue



        # niveau interdit

        if any(

            word in text

            for word in FORBIDDEN_LEVELS

        ):

            continue



        results.append(job)



    return results[:20]