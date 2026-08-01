from .config import (
    TARGET_SKILLS,
    TARGET_CONTRACTS,
    EUROPE_LOCATIONS,
    EUROPE_COMPANIES
)



SENIOR_WORDS = [

    "senior",
    "staff",
    "principal",
    "director",
    "lead",
    "architect",
    "manager"

]



def score_offer(job):


    text = (

        job.get("title","")

        + " "

        + job.get("description","")

        + " "

        + job.get("company","")

        + " "

        + job.get("location","")

    ).lower()



    score = 0



    # Compétences IA/Data

    for skill in TARGET_SKILLS:


        if skill.lower() in text:

            score += 10



    # Contrats recherchés

    for contract in TARGET_CONTRACTS:


        if contract.lower() in text:

            score += 30



    # Europe

    for location in EUROPE_LOCATIONS:


        if location.lower() in text:

            score += 25



    # Entreprises ciblées

    for company in EUROPE_COMPANIES:


        if company.lower() in text:

            score += 20



    # Pénalité senior

    for word in SENIOR_WORDS:


        if word in text:

            score -= 25



    # Bonus Remote Europe

    if "remote europe" in text:

        score += 20



    job["score"] = max(score,0)



    return job




def score_jobs(jobs):


    return [

        score_offer(job)

        for job in jobs

    ]