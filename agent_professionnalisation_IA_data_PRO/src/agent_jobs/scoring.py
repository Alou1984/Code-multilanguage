from .config import (
    TARGET_ROLES,
    TARGET_SKILLS,
    TARGET_CONTRACTS,
    TARGET_LOCATIONS,
    PRIORITY_COMPANIES,
    LOW_PRIORITY_KEYWORDS
)



def score_job(job):


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



    for role in TARGET_ROLES:

        if role in text:

            score +=30



    for skill in TARGET_SKILLS:

        if skill in text:

            score +=10



    for contract in TARGET_CONTRACTS:

        if contract in text:

            score +=60



    for location in TARGET_LOCATIONS:

        if location in text:

            score +=20



    for company in PRIORITY_COMPANIES:

        if company.lower() in text:

            score +=20



    for bad in LOW_PRIORITY_KEYWORDS:

        if bad in text:

            score -=30



    job["score"]=score


    return job




def score_jobs(jobs):


    result=[]


    for job in jobs:

        result.append(

            score_job(job)

        )


    result.sort(

        key=lambda x:

        x.get("score",0),

        reverse=True

    )


    return result