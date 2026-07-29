from .settings import (
    TARGET_ROLES,
    TARGET_DOMAINS,
    TARGET_COMPANIES
)



def score_job(job):


    text = (

        job.get("title","")
        + " "
        + job.get("description","")
        + " "
        + job.get("company","")

    ).lower()



    score = 0



    for item in TARGET_ROLES:

        if item.lower() in text:

            score += 20



    for item in TARGET_DOMAINS:

        if item.lower() in text:

            score += 10



    for item in TARGET_COMPANIES:

        if item.lower() in text:

            score += 15



    return score




def filter_jobs(jobs):


    result = []



    for job in jobs:


        score = score_job(job)


        if score >= 20:


            job["score"] = score

            result.append(job)



    result.sort(

        key=lambda x:x["score"],

        reverse=True

    )


    return result[:20]