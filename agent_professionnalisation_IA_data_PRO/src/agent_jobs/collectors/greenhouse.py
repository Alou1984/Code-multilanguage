import requests


COMPANIES = [

    "dataiku",

    "mistral",

    "huggingface"

]



def search_greenhouse():

    jobs=[]


    for company in COMPANIES:


        try:

            url=(

                "https://boards-api.greenhouse.io/v1/boards/"

                +company+

                "/jobs"

            )


            response=requests.get(

                url,

                timeout=10

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
                    "",

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
                "Greenhouse:",
                e
            )


    return jobs