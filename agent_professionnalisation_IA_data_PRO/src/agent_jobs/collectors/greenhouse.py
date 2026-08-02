import requests


COMPANIES = [

    "airbus",

    "safran",

    "thales",

    "dataiku",

    "qonto",

    "backmarket"

]



def search_greenhouse():


    jobs=[]


    for company in COMPANIES:


        url = (

            f"https://boards-api.greenhouse.io/v1/boards/"
            f"{company}/jobs"

        )


        try:


            response=requests.get(

                url,

                timeout=15

            )


            if response.status_code != 200:

                continue



            data=response.json()



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
                    job.get(
                        "location",
                        {}
                    ).get(
                        "name",
                        ""
                    ),

                    "description":
                    "",

                    "link":
                    job.get(
                        "absolute_url",
                        ""
                    )

                })


        except Exception as e:


            print(
                "Greenhouse",
                company,
                e
            )


    return jobs