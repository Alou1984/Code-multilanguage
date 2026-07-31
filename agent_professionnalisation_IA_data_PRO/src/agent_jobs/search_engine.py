import os
import requests


from .config import (
    LOCATIONS,
    TARGET_ROLES,
    TARGET_COMPANIES
)


SERP_URL = "https://serpapi.com/search"



def build_queries():


    queries = []


    # Métiers

    for role in TARGET_ROLES:

        queries.append(
            role
        )


    # Entreprises

    for company in TARGET_COMPANIES:

        queries.append(

            f"{company} Data Engineer"

        )

        queries.append(

            f"{company} AI Engineer"

        )


    # Contrats

    queries.extend([

        "contrat professionnalisation Data Engineer",

        "graduate program Data",

        "junior AI Engineer",

        "alternance Machine Learning",

        "MLOps Engineer junior",

        "LLM Engineer"

    ])


    return queries




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

    seen = set()



    queries = build_queries()



    print(
        f"Nombre de requêtes : {len(queries)}"
    )



    for location in LOCATIONS:


        for query in queries:


            print(
                f"Recherche : {query} | {location}"
            )



            params = {


                "engine":

                "google_jobs",


                "q":

                query,


                "location":

                location,


                "api_key":

                api_key

            }



            try:


                response = requests.get(

                    SERP_URL,

                    params=params,

                    timeout=30

                )


                data = response.json()



                if "error" in data:


                    print(

                        "Erreur SerpAPI :",

                        data["error"]

                    )


                    continue



                results = data.get(

                    "jobs_results",

                    []

                )



                print(

                    "Résultats :",

                    len(results)

                )



                for job in results:



                    title = job.get(

                        "title",

                        ""

                    )


                    company = job.get(

                        "company_name",

                        ""

                    )



                    key = (

                        title,

                        company

                    )



                    if key in seen:

                        continue



                    seen.add(key)



                    jobs.append({


                        "title":

                        title,


                        "company":

                        company,


                        "location":

                        job.get(

                            "location",

                            location

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



            except Exception as e:


                print(

                    "Erreur recherche :",

                    e

                )



    print(

        "TOTAL OFFRES TROUVEES :",

        len(jobs)

    )


    return jobs