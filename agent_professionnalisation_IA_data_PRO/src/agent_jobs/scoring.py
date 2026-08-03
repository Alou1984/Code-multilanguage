from .config import (
    TARGET_SKILLS,
    EUROPE_LOCATIONS,
    VALID_CONTRACTS,
    TARGET_COMPANIES,
    FORBIDDEN_TERMS
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

        + " "

        + job.get("contract","")

    ).lower()



    score = 0



    # Compétences IA/Data

    for skill in TARGET_SKILLS:

        if skill in text:

            score += 10



    # Europe

    for location in EUROPE_LOCATIONS:

        if location in text:

            score += 25



    # Contrat recherché

    for contract in VALID_CONTRACTS:

        if contract in text:

            score += 100



    # Entreprise cible

    for company in TARGET_COMPANIES:

        if company in text:

            score += 20



    # Pénalité senior

    for word in FORBIDDEN_TERMS:

        if word in text:

            score -= 100



    job["score"] = score


    return job




def score_jobs(jobs):


    return [

        score_offer(job)

        for job in jobs

    ]