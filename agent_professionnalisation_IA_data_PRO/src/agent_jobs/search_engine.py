from .collectors.greenhouse import search_greenhouse
from .collectors.lever import search_lever
from .collectors.teamtailor import search_teamtailor
from .collectors.france_travail import search_france_travail



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

        search_greenhouse,

        search_lever,

        search_teamtailor,

        search_france_travail

    ]



    for collector in collectors:


        try:

            result = collector()


            print(

                collector.__name__,

                "=>",

                len(result)

            )


            jobs.extend(result)



        except Exception as e:


            print(

                "ERREUR",

                collector.__name__,

                e

            )



    final=[]


    seen=set()



    for job in jobs:


        job=normalize(job)



        # obligation vraie URL

        if not job["link"].startswith(
            "http"
        ):

            continue



        key=(

            job["title"],

            job["company"],

            job["link"]

        )



        if key not in seen:


            seen.add(key)

            final.append(job)



    print(

        "TOTAL OFFRES VALIDES",

        len(final)

    )


    return final