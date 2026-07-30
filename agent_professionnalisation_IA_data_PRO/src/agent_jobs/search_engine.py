import os
import requests


SERP_URL = "https://serpapi.com/search"


# =====================================================
# DOMAINES DE RECHERCHE
# =====================================================

LOCATIONS = [

    # France
    "France",
    "Paris France",
    "Ile-de-France",
    "Sens France",
    "Bourgogne-Franche-Comté",
    "Centre-Val de Loire",
    "Lyon France",
    "Toulouse France",
    "Grenoble France",

    # Suisse / Luxembourg
    "Switzerland",
    "Geneva Switzerland",
    "Lausanne Switzerland",
    "Zurich Switzerland",
    "Luxembourg",

    # UK
    "United Kingdom",
    "London UK",
    "Manchester UK",

    # USA
    "United States",
    "USA",
    "New York USA",
    "California USA",
    "San Francisco USA",
    "Seattle USA",
    "Texas USA",

    # UAE
    "United Arab Emirates",
    "Dubai UAE",
    "Abu Dhabi UAE",

    # Saudi Arabia
    "Saudi Arabia",
    "Riyadh Saudi Arabia",
    "Jeddah Saudi Arabia",

    # Remote
    "Remote",
    "Full Remote",
    "Remote Worldwide"

]



# =====================================================
# REQUETES EMPLOI
# =====================================================

QUERIES = [

    # Big Data / Data Engineering

    "Big Data Engineer",
    "Expert Big Data Engineer",
    "Data Engineer",
    "Senior Data Engineer",
    "Cloud Data Engineer",
    "Data Platform Engineer",


    # IA

    "AI Engineer",
    "Artificial Intelligence Engineer",
    "Machine Learning Engineer",
    "Deep Learning Engineer",
    "MLOps Engineer",
    "LLM Engineer",
    "Generative AI Engineer",


    # GPU / Hardware IA

    "AI Engineer GPU",
    "Machine Learning GPU Engineer",
    "NVIDIA CUDA AI Engineer",
    "AI Hardware Engineer",
    "AWS Neuron AI Engineer",
    "TPU Machine Learning Engineer",


    # Formation / Graduate

    "Graduate Program Data Engineer",
    "Graduate Program Artificial Intelligence",
    "Junior Data Engineer",
    "Junior AI Engineer",
    "Contrat professionnalisation Data Engineer",
    "Professionalization contract Data Engineer",
    "Apprenticeship Data Engineer",


    # Industrie

    "EDF Data Engineer",
    "TotalEnergies Data Engineer",
    "Safran AI Engineer",
    "Framatome Data Engineer",
    "Airbus AI Engineer",
    "Eramet Data Engineer",
    "Prysmian Data Engineer",


    # Energie Oil Gas Mining

    "Energy Data Engineer",
    "Oil Gas Data Engineer",
    "Mining Data Engineer",
    "Industrial AI Engineer",


    # Systèmes embarqués

    "Embedded AI Engineer",
    "Robotics AI Engineer",
    "Autonomous Systems Engineer",


    # Remote international

    "Remote AI Engineer",
    "Remote Data Engineer",
    "Remote Machine Learning Engineer",
    "Remote LLM Engineer"

]



# =====================================================
# RECHERCHE SERPAPI
# =====================================================


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



    seen = set()



    for location in LOCATIONS:


        for query in QUERIES:


            params = {

                "engine": "google_jobs",

                "q": query,

                "location": location,

                "hl": "en",

                "api_key": api_key

            }


            try:


                response = requests.get(

                    SERP_URL,

                    params=params,

                    timeout=30

                )


                data = response.json()



                results = data.get(

                    "jobs_results",

                    []

                )



                print(

                    f"{location} | {query} | {len(results)} offres"

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


                    link = job.get(

                        "share_link",

                        ""

                    )



                    # suppression doublons

                    key = (

                        title,

                        company,

                        location

                    )


                    if key in seen:

                        continue



                    seen.add(key)



                    jobs.append({

                        "country":

                        location,


                        "title":

                        title,


                        "company":

                        company,


                        "location":

                        job.get(

                            "location",

                            location

                        ),


                        "link":

                        link,


                        "description":

                        job.get(

                            "description",

                            ""

                        )

                    })



            except Exception as error:


                print(

                    "Erreur SERPAPI :",

                    error

                )



    print(

        "TOTAL OFFRES BRUTES :",

        len(jobs)

    )


    return jobs