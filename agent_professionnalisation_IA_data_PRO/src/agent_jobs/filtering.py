def filter_jobs(jobs):


    jobs = sorted(

        jobs,

        key=lambda x:

        x.get("score",0),

        reverse=True

    )



    selected = [

        job

        for job in jobs

        if job.get(
            "score",
            0
        ) >= 20

    ]



    # Sécurité :
    # toujours envoyer quelque chose

    if not selected:


        selected = jobs[:10]



    return selected[:20]