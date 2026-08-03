from .config import (
    TARGET_SKILLS,
    CONTRACT_WORDS,
    TARGET_COMPANIES,
    EUROPE_LOCATIONS
)



def score_offer(job):


    text = (

        job.get("title","")

        + " "

        + job.get("description","")

        + " "

        + job.get("location","")

        + " "

        + job.get("company","")

    ).lower()



    score = 0



    # IA/Data

    for skill in TARGET_SKILLS:

        if skill in text:

            score += 10



    # Europe

    for location in EUROPE_LOCATIONS:

        if location in text:

            score += 20



    # Contrat recherché

    for contract in CONTRACT_WORDS:

        if contract in text:

            score += 50



    # Entreprises ciblées

    for company in TARGET_COMPANIES:

        if company in text:

            score += 20



    job["score"] = score


    return job




def score_jobs(jobs):


    scored = []


    for job in jobs:

        scored.append(

            score_offer(job)

        )


    scored.sort(

        key=lambda x:

        x.get("score",0),

        reverse=True

    )


    return scored