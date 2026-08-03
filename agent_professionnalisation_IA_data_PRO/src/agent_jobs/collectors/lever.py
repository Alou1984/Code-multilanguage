import requests



COMPANIES=[

    "dataiku",

    "mistral",

    "backmarket"

]



def search_lever():


    jobs=[]


    for company in COMPANIES:


        url=(

            "https://api.lever.co/v0/postings/"

            +company

            +"?mode=json"

        )


        try:


            response=requests.get(

                url,

                timeout=20

            )



            data=response.json()



            if not isinstance(data,list):

                continue



            for job in data:


                if not isinstance(job,dict):

                    continue



                categories = job.get(
                    "categories",
                    {}
                )



                jobs.append({

                    "title":
                    job.get(
                        "text",
                        ""
                    ),

                    "company":
                    company,

                    "location":
                    categories.get(
                        "location",
                        ""
                    ),

                    "description":
                    job.get(
                        "descriptionPlain",
                        ""
                    ),

                    "contract":
                    "",

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