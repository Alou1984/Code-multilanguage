from .config import (
    VALID_CONTRACTS,
    FORBIDDEN_TERMS
)



def filter_jobs(jobs):


    selected = []



    for job in jobs:


        text = (

            job.get("title","")

            + " "

            + job.get("description","")

            + " "

            + job.get("contract","")

        ).lower()



        # Pas de lien = suppression

        if not job.get("link"):

            continue



        # Pas de contrat compatible = suppression

        if not any(

            contract in text

            for contract in VALID_CONTRACTS

        ):

            continue



        # Senior supprimé

        if any(

            word in text

            for word in FORBIDDEN_TERMS

        ):

            continue



        selected.append(job)



    selected.sort(

        key=lambda x:

        x.get(
            "score",
            0
        ),

        reverse=True

    )


    return selected[:20]