import os
import requests


SERP_URL = "https://serpapi.com/search"


LOCATIONS = [

    "France",
    "Paris France",
    "Ile-de-France",
    "Switzerland",
    "Luxembourg",
    "United Kingdom",
    "USA",
    "United Arab Emirates",
    "Saudi Arabia",
    "Remote"

]


QUERIES = [

    "Data Engineer",
    "Big Data Engineer",
    "AI Engineer",
    "Machine Learning Engineer",
    "MLOps Engineer",
    "LLM Engineer",
    "Deep Learning Engineer",
    "Graduate Program Data",
    "Data Engineer Remote",
    "AI Engineer Remote"

]


def search_jobs():


    api_key = os.getenv(
        "SERPAPI_API_KEY"
    )


    if not api_key:

        print(
            "ERREUR : SERPAPI_API_KEY absent"
        )

        return []



    jobs = []


    for location in LOCATIONS:


        for query in QUERIES:


            print(
                f"Recherche : {query} / {location}"
            )


            params = {

                "engine": "google_jobs",

                "q": query,

                "location": location,

                "api_key": api_key

            }



            try:

                response = requests.get(

                    SERP_URL,

                    params=params,

                    timeout=30

                )


                data = response.json()



                print(
                    "REPONSE SERPAPI KEYS :",
                    data.keys()
                )



                if "error" in data:

                    print(
                        "ERREUR SERPAPI :",
                        data["error"]
                    )

                    continue



                results = data.get(

                    "jobs_results",

                    []

                )



                print(

                    "RESULTATS TROUVES :",

                    len(results)

                )



                for job in results:


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
                            location
                        ),

                        "link":
                        job.get(
                            "share_link",
                            ""
                        ),

                        "description":
                        job.get(
                            "description",
                            ""
                        )

                    })



            except Exception as e:


                print(

                    "Erreur connexion SERPAPI :",

                    e

                )



    print(
        "TOTAL OFFRES BRUTES :",
        len(jobs)
    )


    return jobs