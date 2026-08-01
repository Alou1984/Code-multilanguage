import requests



EUROPE_WORDS = [

    "europe",
    "emea",
    "france",
    "germany",
    "switzerland",
    "luxembourg",
    "uk"

]



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


            text = (

                job.get("position","")

                +

                job.get("description","")

            ).lower()



            if not any(

                key in text

                for key in [

                    "data",

                    "ai",

                    "machine learning",

                    "mlops",

                    "llm"

                ]

            ):

                continue



            # éviter USA pur

            if "usa" in text:

                continue



            jobs.append({

                "title":
                job.get("position",""),

                "company":
                job.get("company",""),

                "location":
                "Remote Europe",

                "description":
                job.get("description",""),

                "link":
                job.get("url","")

            })


    except Exception as e:

        print(
            "RemoteOK:",
            e
        )



    return jobs