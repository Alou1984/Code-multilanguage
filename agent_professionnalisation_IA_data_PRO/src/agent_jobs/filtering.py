def filter_jobs(jobs):


    jobs = sorted(

        jobs,

        key=lambda x:

        x.get("score",0),

        reverse=True

    )


    selected = []



    for job in jobs:


        title = job.get(
            "title",
            ""
        ).lower()



        # éviter trop senior

        if any(word in title for word in [

            "senior",
            "staff",
            "principal",
            "director"

        ]):

            continue



        selected.append(job)



    # Sécurité

    if not selected:

        selected = jobs[:10]



    return selected[:20]