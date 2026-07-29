import os
import requests


def search_jobs():

    api_key = os.getenv("SERPAPI_API_KEY")

    if not api_key:
        print("SERPAPI_API_KEY absent")
        return []


    queries = [
        "Expert Big Data Engineer contrat professionnalisation France",
        "AI Engineer Graduate Program France",
        "Data Engineer MLOps Engineer France",
        "LLM Engineer GPU France",
        "Machine Learning Engineer Deep Learning France",
        "Data Engineer EDF Safran TotalEnergies",
        "Big Data Engineer Energie Oil Gas Mining"
    ]


    jobs = []


    for query in queries:

        params = {
            "engine": "google_jobs",
            "q": query,
            "location": "France",
            "api_key": api_key
        }


        try:

            response = requests.get(
                "https://serpapi.com/search",
                params=params,
                timeout=30
            )


            data = response.json()


            for job in data.get("jobs_results", []):

                jobs.append({

                    "title": job.get("title",""),

                    "company": job.get("company_name",""),

                    "location": job.get("location",""),

                    "link": job.get(
                        "share_link",
                        ""
                    ),

                    "description": job.get(
                        "description",
                        ""
                    )

                })


        except Exception as e:

            print(
                "Erreur recherche :",
                e
            )


    return jobs