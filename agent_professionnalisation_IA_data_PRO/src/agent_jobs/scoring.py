from .config import (
    TARGET_SKILLS,
    CONTRACT_KEYWORDS,
    EUROPE_KEYWORDS,
    TARGET_ROLES
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



    for role in TARGET_ROLES:

        if role in text:

            score +=30



    for skill in TARGET_SKILLS:

        if skill in text:

            score +=10



    for contract in CONTRACT_KEYWORDS:

        if contract in text:

            score +=50



    for place in EUROPE_KEYWORDS:

        if place in text:

            score +=20



    job["score"]=score


    return job




def score_jobs(jobs):


    result=[]


    for job in jobs:

        result.append(
            score_offer(job)
        )


    result.sort(

        key=lambda x:

        x.get(
            "score",
            0
        ),

        reverse=True

    )


    return result