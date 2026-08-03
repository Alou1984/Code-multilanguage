import requests


COMPANIES=[

    "airbus",

    "safran",

    "thales",

    "dataiku",

    "mistral"

]



def search_greenhouse():


    jobs=[]


    for company in COMPANIES:


        url=(

            "https://boards-api.greenhouse.io/v1/boards/"

            +company+

            "/jobs"

        )


        try:


            response=requests.get(

                url,

                timeout=20

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

                    "contract":
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