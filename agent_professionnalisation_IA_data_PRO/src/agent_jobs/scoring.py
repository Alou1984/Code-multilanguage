from .config import (
    TARGET_SKILLS,
    TARGET_LOCATIONS,
    TARGET_CONTRACTS
)



BAD_WORDS = [

    "senior",

    "staff",

    "principal",

    "director",

    "manager"

]



def score_offer(job):


    text = (

        job["title"]

        + " "

        + job["description"]

        + " "

        + job["location"]

    ).lower()



    score = 0



    for skill in TARGET_SKILLS:


        if skill.lower() in text:

            score += 10



    for location in TARGET_LOCATIONS:


        if location.lower() in text:

            score += 25



    for contract in TARGET_CONTRACTS:


        if contract.lower() in text:

            score += 35



    for bad in BAD_WORDS:


        if bad in text:

            score -= 30



    job["score"] = max(score,0)



    return job




def score_jobs(jobs):


    return [

        score_offer(job)

        for job in jobs

    ]