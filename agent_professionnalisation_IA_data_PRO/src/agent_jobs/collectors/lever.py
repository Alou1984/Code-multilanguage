import requests



COMPANIES=[

    "dataiku",

    "mistral",

    "backmarket"

]



def search_lever():

    jobs=[]


    for company in COMPANIES:


        try:


            url=(

                "https://api.lever.co/v0/postings/"

                +company+

                "?mode=json"

            )


            response=requests.get(

                url,

                timeout=10

            )


            data=response.json()


            if not isinstance(data,list):

                continue



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
                    "",

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
                "Lever:",
                e
            )


    return jobs