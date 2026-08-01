from .config import *


SENIOR_WORDS = [

    "senior",
    "staff",
    "principal",
    "director",
    "lead"

]


def score_offer(job):


    text = (

        job["title"]

        +" "

        +job["description"]

        +" "

        +job["company"]

        +" "

        +job["location"]

    ).lower()



    score = 0



    for skill in TARGET_SKILLS:

        if skill.lower() in text:

            score += 10



    for contract in TARGET_CONTRACTS:

        if contract.lower() in text:

            score += 40



    for location in TARGET_LOCATIONS:

        if location.lower() in text:

            score += 30



    for company in TARGET_COMPANIES:

        if company.lower() in text:

            score += 20



    for word in SENIOR_WORDS:

        if word in text:

            score -= 30



    job["score"] = max(score,0)


    return job



def score_jobs(jobs):

    return [

        score_offer(job)

        for job in jobs

    ]