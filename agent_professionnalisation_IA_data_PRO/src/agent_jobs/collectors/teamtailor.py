import requests


COMPANIES = [

    "airbus",
    "qonto",
    "doctolib",
    "backmarket",
    "deezer"

]


def search_teamtailor():

    jobs = []


    for company in COMPANIES:


        url = (
            f"https://{company}.teamtailor.com/api/jobs"
        )


        try:

            response = requests.get(
                url,
                timeout=20
            )


            data = response.json()


            for job in data.get(
                "data",
                []
            ):


                attributes = job.get(
                    "attributes",
                    {}
                )


                jobs.append({

                    "title":
                    attributes.get(
                        "title",
                        ""
                    ),

                    "company":
                    company,

                    "location":
                    attributes.get(
                        "location",
                        ""
                    ),

                    "description":
                    attributes.get(
                        "description",
                        ""
                    ),

                    "link":
                    attributes.get(
                        "url",
                        ""
                    )

                })


        except Exception as e:

            print(
                "Teamtailor:",
                company,
                e
            )


    return jobs