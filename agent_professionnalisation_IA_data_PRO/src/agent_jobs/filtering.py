def filter_jobs(jobs):


    jobs.sort(

        key=lambda x:x.get("score",0),

        reverse=True

    )


    result=[]


    for job in jobs:


        if job["score"] >= 30:

            result.append(job)



    if not result:

        result = jobs[:10]



    return result[:20]