import os
import requests

from .settings import LOCATIONS


SERP_URL = "https://serpapi.com/search"



QUERIES = [

    "Big Data Engineer",
    "Data Engineer",
    "AI Engineer",
    "Machine Learning Engineer",
    "MLOps Engineer",
    "LLM Engineer",
    "Generative AI Engineer",

    "Graduate Program Data",
    "Graduate Program Artificial Intelligence",

    "contrat professionnalisation Data Engineer",
    "contrat professionnalisation IA",

    "EDF Data Engineer",
    "Safran AI Engineer",
    "Framatome Big Data",
    "TotalEnergies Data Engineer",

    "Oil Gas Data Engineer",
    "Mining Data Engineer",

    "Embedded AI Engineer",
    "Robotics AI Engineer",
    "HVAC Data Engineer"

]



def search_jobs():


    api_key = os.getenv(
        "SERPAPI_API_KEY"
    )


    if not api_key:

        print(
            "SERPAPI_API_KEY absent"
        )

        return []



    jobs = []



    for location in LOCATIONS:

        for query in QUERIES:


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
                    "Erreur SERPAPI:",
                    e
                )



    return jobs