import requests



COMPANIES=[

    "airbus",

    "qonto",

    "backmarket"

]



def search_teamtailor():


    jobs=[]



    for company in COMPANIES:


        url=(

            "https://"

            +company

            +".teamtailor.com/api/v1/jobs"

        )


        try:


            response=requests.get(

                url,

                timeout=20,

                headers={

                    "Accept":
                    "application/json"

                }

            )


            if response.status_code != 200:

                continue



            try:

                data=response.json()

            except:

                continue



            for item in data.get(
                "data",
                []
            ):


                attrs=item.get(
                    "attributes",
                    {}
                )



                jobs.append({

                    "title":
                    attrs.get(
                        "title",
                        ""
                    ),

                    "company":
                    company,

                    "location":
                    attrs.get(
                        "location",
                        ""
                    ),

                    "description":
                    attrs.get(
                        "description",
                        ""
                    ),

                    "contract":
                    "",

                    "link":
                    attrs.get(
                        "url",
                        ""
                    )

                })


        except Exception as e:


            print(
                "Teamtailor",
                company,
                e
            )


    return jobs