import requests



COMPANIES=[

    "mistral",

    "huggingface",

    "dataiku",

    "airbus",

    "safran",

    "thales"

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


                title=job.get(
                    "title",
                    ""
                ).lower()



                allowed=[

                    "data",

                    "machine learning",

                    "ai",

                    "ml",

                    "software engineer",

                    "research"

                ]



                if not any(

                    word in title

                    for word in allowed

                ):

                    continue



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
                "Greenhouse error",
                company,
                e
            )



    return jobs