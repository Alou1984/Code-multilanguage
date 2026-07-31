from .collectors.france_travail import search_france_travail
from .collectors.greenhouse import search_greenhouse
from .collectors.lever import search_lever
from .collectors.remoteok import search_remoteok



def normalize_job(job):

    return {

        "title": job.get("title", "").strip(),

        "company": job.get("company", "").strip(),

        "location": job.get("location", "").strip(),

        "description": job.get("description", "").strip(),

        "link": job.get("link", "").strip(),

    }



def search_jobs():

    print("=== COLLECTE DES OFFRES ===")


    jobs = []


    collectors = [

        search_france_travail,

        search_greenhouse,

        search_lever,

        search_remoteok

    ]



    for collector in collectors:


        try:

            results = collector()


            print(
                collector.__name__,
                ":",
                len(results),
                "offres"
            )


            jobs.extend(results)



        except Exception as e:


            print(

                "Erreur collecteur",

                collector.__name__,

                e

            )



    # Normalisation

    normalized = [

        normalize_job(job)

        for job in jobs

    ]



    # Suppression doublons

    unique = []


    seen = set()



    for job in normalized:


        key = (

            job["title"],

            job["company"]

        )


        if key not in seen:


            seen.add(key)

            unique.append(job)



    print(

        "TOTAL OFFRES UNIQUES :",

        len(unique)

    )


    return unique
