def filter_jobs(jobs):


    valid = []



    for job in jobs:


        if len(job.get(
            "title",
            ""
        )) < 3:

            continue



        if len(job.get(
            "description",
            ""
        )) < 30:

            continue



        link = job.get(
            "link",
            ""
        )



        if not link.startswith(
            "http"
        ):

            continue



        valid.append(job)



    valid.sort(

        key=lambda x:

        x.get(
            "score",
            0
        ),

        reverse=True

    )


    return valid[:20]