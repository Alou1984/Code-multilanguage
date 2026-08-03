from .config import (
    TARGET_SKILLS,
    TARGET_ROLES,
    CONTRACT_KEYWORDS,
    EUROPE_KEYWORDS,
    SENIOR_KEYWORDS
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



    for role in TARGET_ROLES:

        if role in text:

            score += 30



    for skill in TARGET_SKILLS:

        if skill in text:

            score += 10



    for contract in CONTRACT_KEYWORDS:

        if contract in text:

            score += 50



    for place in EUROPE_KEYWORDS:

        if place in text:

            score += 20



    for senior in SENIOR_KEYWORDS:

        if senior in text:

            score -= 50



    job["score"] = score


    return job




def score_jobs(jobs):


    results=[]


    for job in jobs:

        results.append(
            score_offer(job)
        )



    results.sort(

        key=lambda x:

        x.get(
            "score",
            0
        ),

        reverse=True

    )


    return results