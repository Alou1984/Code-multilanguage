import requests



COMPANIES = [

    "anthropic",

    "scaleai"

]



def search_lever():


    jobs = []



    for company in COMPANIES:


        url = (

            "https://api.lever.co/v0/postings/"
            f"{company}"

        )


        try:


            data = requests.get(
                url,
                timeout=20
            ).json()



            for job in data:


                jobs.append({

                    "title":
                    job.get(
                        "text",
                        ""
                    ),

                    "company":
                    company,

                    "location":
                    job.get(
                        "categories",
                        {}
                    ).get(
                        "location",
                        ""
                    ),

                    "description":
                    job.get(
                        "descriptionPlain",
                        ""
                    ),

                    "link":
                    job.get(
                        "hostedUrl",
                        ""
                    )

                })


        except Exception as e:

            print(
                "Lever:",
                e
            )



    return jobs