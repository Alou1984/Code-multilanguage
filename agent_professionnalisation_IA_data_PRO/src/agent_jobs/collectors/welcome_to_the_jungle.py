import requests


def search_wttj():


    jobs = []


    queries = [

        "Data Engineer",

        "Machine Learning Engineer",

        "AI Engineer",

        "MLOps",

        "Data Scientist"

    ]


    for query in queries:


        url = (

            "https://api.welcometothejungle.com/"
            "api/v1/jobs"

        )


        try:

            response = requests.get(

                url,

                params={

                    "query":
                    query,

                    "page":
                    1

                },

                timeout=20

            )


            if response.status_code != 200:

                continue



            data = response.json()



            for job in data.get(
                "jobs",
                []
            ):


                jobs.append({

                    "title":
                    job.get(
                        "name",
                        ""
                    ),

                    "company":
                    job.get(
                        "company",
                        ""
                    ),

                    "location":
                    job.get(
                        "location",
                        ""
                    ),

                    "description":
                    job.get(
                        "description",
                        ""
                    ),

                    "link":
                    job.get(
                        "web_url",
                        ""
                    )

                })


        except Exception as e:

            print(
                "WTTJ:",
                e
            )


    return jobs