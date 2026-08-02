from .config import (
    TARGET_SKILLS,
    EUROPE_LOCATIONS,
    CONTRACT_WORDS,
    TARGET_COMPANIES
)



def score_offer(job):


    text=(

        job.get("title","")

        +" "

        +job.get("description","")

        +" "

        +job.get("location","")

        +" "

        +job.get("company","")

    ).lower()



    score=0



    for skill in TARGET_SKILLS:

        if skill in text:

            score += 10



    for location in EUROPE_LOCATIONS:

        if location in text:

            score += 25



    for contract in CONTRACT_WORDS:

        if contract in text:

            score += 40



    for company in TARGET_COMPANIES:

        if company in text:

            score += 20



    job["score"]=score


    return job




def score_jobs(jobs):


    return [

        score_offer(job)

        for job in jobs

    ]