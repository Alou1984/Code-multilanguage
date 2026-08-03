from .config import (
    TARGET_SKILLS,
    TARGET_COMPANIES,
    EUROPE_LOCATIONS,
    VALID_CONTRACTS
)



def score_offer(job):


    text=(

        job.get("title","")

        +" "

        +job.get("description","")

        +" "

        +job.get("location","")

    ).lower()



    score=0



    # Poste IA/Data

    for skill in TARGET_SKILLS:

        if skill in text:

            score +=10



    # Europe

    for place in EUROPE_LOCATIONS:

        if place in text:

            score +=30



    # Contrat

    for contract in VALID_CONTRACTS:

        if contract in text:

            score +=50



    # Entreprise cible

    for company in TARGET_COMPANIES:

        if company in text:

            score +=20



    job["score"]=score


    return job




def score_jobs(jobs):


    return [

        score_offer(job)

        for job in jobs

    ]