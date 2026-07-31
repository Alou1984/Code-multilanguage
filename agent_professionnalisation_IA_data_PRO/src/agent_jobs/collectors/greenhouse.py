import requests



COMPANIES = [

    "nvidia",

    "openai",

    "databricks"

]



def search_greenhouse():


    jobs = []



    for company in COMPANIES:


        url = (

            "https://boards-api.greenhouse.io/"
            f"v1/boards/{company}/jobs"

        )


        try:

            data = requests.get(
                url,
                timeout=20
            ).json()



            for job in data.get(
                "jobs",
                []
            ):


                jobs.append({

                    "title":
                    job.get(
                        "title",
                        ""
                    ),

                    "company":
                    company,

                    "location":
                    "",

                    "description":
                    job.get(
                        "content",
                        ""
                    ),

                    "link":
                    job.get(
                        "absolute_url",
                        ""
                    )

                })



        except Exception as e:

            print(
                "Greenhouse:",
                e
            )



    return jobs