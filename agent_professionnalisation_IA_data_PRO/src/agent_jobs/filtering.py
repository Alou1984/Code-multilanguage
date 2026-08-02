def filter_jobs(jobs):


    result=[]


    for job in jobs:


        if not job.get("title"):

            continue



        if not job.get("link"):

            continue



        result.append(job)



    result.sort(

        key=lambda x:

        x.get(
            "score",
            0
        ),

        reverse=True

    )


    return result[:20]