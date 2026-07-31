from .config import (
    TARGET_SKILLS,
    TARGET_ROLES,
    TARGET_COMPANIES
)



def score_offer(job):


    text = (

        job.get("title","")

        + " "

        + job.get("description","")

        + " "

        + job.get("company","")

    ).lower()



    score = 0



    for skill in TARGET_SKILLS:


        if skill.lower() in text:

            score += 10



    for role in TARGET_ROLES:


        if role.lower() in text:

            score += 15



    for company in TARGET_COMPANIES:


        if company.lower() in text:

            score += 20



    return score