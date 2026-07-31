import os
import requests


SERP_URL = "https://serpapi.com/search"


SOURCES = [

    "linkedin.com/jobs",
    "indeed.com",
    "hellowork.com",
    "apec.fr",
    "francetravail.fr",
    "free-work.com",
    "glassdoor.fr",
    "teamtailor.com"

]


LOCATIONS = [

    "France",
    "Ile-de-France",
    "Centre-Val de Loire",
    "Bourgogne-Franche-Comté",
    "Suisse",
    "Luxembourg"

]


QUERIES = [

    "Data Engineer",

    "Big Data Engineer",

    "AI Engineer",

    "Machine Learning Engineer",

    "MLOps Engineer",

    "LLM Engineer",

    "Deep Learning Engineer",

    "AWS Neuron AI",

    "GPU Machine Learning",

    "Embedded AI Engineer",

    "Robotics AI Engineer"

]



def serpapi_search(params):

    key = os.getenv(
        "SERPAPI_API_KEY"
    )


    if not key:

        print(
            "SERPAPI_API_KEY absent"
        )

        return []



    params["api_key"] = key


    try:

        r = requests.get(

            SERP_URL,

            params=params,

            timeout=30

        )


        data = r.json()


        if "error" in data:

            print(
                "ERREUR SERPAPI :",
                data["error"]
            )

            return []



        return data



    except Exception as e:


        print(
            "Erreur connexion :",
            e
        )

        return []




def search_google_jobs():

    jobs = []


    for location in LOCATIONS:


        for query in QUERIES:


            print(
                "GOOGLE JOBS:",
                query,
                location
            )


            data = serpapi_search({

                "engine":
                "google_jobs",

                "q":
                query,

                "location":
                location

            })



            for job in data.get(
                "jobs_results",
                []
            ):


                jobs.append({

                    "title":
                    job.get(
                        "title",
                        ""
                    ),

                    "company":
                    job.get(
                        "company_name",
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
                        "share_link",
                        ""
                    )

                })


    return jobs





def search_web_jobs():

    jobs = []


    for location in LOCATIONS:


        for query in QUERIES:


            for site in SOURCES:


                q = (

                    f"{query} "

                    f"{location} "

                    f"site:{site}"

                )


                print(
                    "WEB:",
                    q
                )



                data = serpapi_search({

                    "engine":
                    "google",

                    "q":
                    q

                })



                for result in data.get(
                    "organic_results",
                    []
                ):


                    jobs.append({

                        "title":
                        result.get(
                            "title",
                            ""
                        ),

                        "company":
                        site,

                        "location":
                        location,

                        "description":
                        result.get(
                            "snippet",
                            ""
                        ),

                        "link":
                        result.get(
                            "link",
                            ""
                        )

                    })


    return jobs




def search_jobs():


    print(
        "=== DEBUT RECHERCHE ==="
    )


    jobs = []


    jobs.extend(
        search_google_jobs()
    )


    print(
        "Google Jobs :",
        len(jobs)
    )


    if len(jobs) == 0:


        print(
            "Passage recherche web"
        )


        jobs.extend(
            search_web_jobs()
        )


    print(
        "TOTAL OFFRES :",
        len(jobs)
    )


    return jobs
