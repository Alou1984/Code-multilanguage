def filter_jobs(jobs):


    print(
        "DEBUG FILTER INPUT :",
        len(jobs)
    )


    for job in jobs[:10]:

        print(

            job.get("title"),

            "|",

            job.get("company"),

            "|",

            job.get("location")

        )


    # TEST :
    # on ne supprime aucune offre

    return jobs[:20]