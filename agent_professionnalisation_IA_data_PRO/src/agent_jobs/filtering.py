from .scoring import score_offer



def filter_jobs(jobs):


    scored = []



    for job in jobs:


        score = score_offer(job)


        job["score"] = score


        scored.append(job)



    scored.sort(

        key=lambda x: x["score"],

        reverse=True

    )



    # Priorité aux meilleures offres

    selected = [

        job

        for job in scored

        if job["score"] >= 20

    ]



    # Sécurité :
    # ne jamais envoyer un mail vide

    if not selected:


        selected = scored[:10]



    return selected[:20]