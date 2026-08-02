from .collectors.france_travail import search_france_travail
from .collectors.greenhouse import search_greenhouse
from .collectors.lever import search_lever
from .collectors.teamtailor import search_teamtailor



def normalize(job):

    return {

        "title": job.get("title","").strip(),

        "company": job.get("company","").strip(),

        "location": job.get("location","").strip(),

        "description": job.get("description","").strip(),

        "link": job.get("link","").strip()

    }



def search_jobs():


    jobs = []


    collectors = [

        search_france_travail,

        search_greenhouse,

        search_lever,

        search_teamtailor

    ]


    for collector in collectors:


        try:

            results = collector()


            print(

                collector.__name__,

                len(results)

            )


            jobs.extend(results)



        except Exception as e:


            print(

                "Erreur",

                collector.__name__,

                e

            )



    unique = []

    seen = set()



    for job in jobs:


        job = normalize(job)



        # obligation vrai lien

        if not job["link"]:

            continue



        key = (

            job["title"],

            job["company"]

        )



        if key not in seen:

            seen.add(key)

            unique.append(job)



    print(

        "OFFRES REELLES :",

        len(unique)

    )


    return unique
