from .config import *


def score_offer(job):


    text=(

        job["title"]

        +" "

        +job["description"]

        +" "

        +job["location"]

    ).lower()



    score=0



    for skill in TARGET_SKILLS:

        if skill in text:

            score += 10



    for location in TARGET_LOCATIONS:

        if location in text:

            score += 20



    for contract in CONTRACT_WORDS:

        if contract in text:

            score += 30



    for bad in BLOCKED_WORDS:

        if bad in text:

            score -= 25



    job["score"]=max(score,0)



    return job




def score_jobs(jobs):


    return [

        score_offer(job)

        for job in jobs

    ]