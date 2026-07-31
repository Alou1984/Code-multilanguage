import requests



def search_remoteok():


    jobs = []



    try:


        data = requests.get(

            "https://remoteok.com/api",

            headers={

                "User-Agent":
                "Mozilla/5.0"

            },

            timeout=20

        ).json()



        for job in data[1:]:


            title = job.get(
                "position",
                ""
            )


            if any(

                key in title.lower()

                for key in [

                    "data",

                    "ai",

                    "machine",

                    "ml"

                ]

            ):


                jobs.append({

                    "title":
                    title,

                    "company":
                    job.get(
                        "company",
                        ""
                    ),

                    "location":
                    "Remote",

                    "description":
                    job.get(
                        "description",
                        ""
                    ),

                    "link":
                    job.get(
                        "url",
                        ""
                    )

                })


    except Exception as e:

        print(
            "RemoteOK:",
            e
        )



    return jobs