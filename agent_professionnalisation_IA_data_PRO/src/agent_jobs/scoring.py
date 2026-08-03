from .config import (
    TARGET_SKILLS,
    TARGET_COMPANIES,
    EUROPE_KEYWORDS,
    CONTRACT_KEYWORDS
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

        +" "

        +job.get("contract","")

    ).lower()



    score=0



    for role in TARGET_SKILLS:

        if role in text:

            score +=10



    for country in EUROPE_KEYWORDS:

        if country in text:

            score +=20



    for contract in CONTRACT_KEYWORDS:

        if contract in text:

            score +=50



    for company in TARGET_COMPANIES:

        if company in text:

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
        x.get("score",0),

        reverse=True

    )


    return result