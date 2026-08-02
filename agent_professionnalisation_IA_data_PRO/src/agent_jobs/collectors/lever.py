import requests



COMPANIES=[

    "dataiku",

    "qonto",

    "backmarket",

    "mistral"

]



def search_lever():


    jobs=[]


    for company in COMPANIES:


        url=(

            f"https://api.lever.co/v0/postings/"
            f"{company}?mode=json"

        )


        try:


            data=requests.get(

                url,

                timeout=15

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
                "Lever",
                company,
                e
            )


    return jobs