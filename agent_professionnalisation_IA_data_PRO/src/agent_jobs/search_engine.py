from .collectors.greenhouse import search_greenhouse
from .collectors.lever import search_lever
from .collectors.teamtailor import search_teamtailor
from .collectors.france_travail import search_france_travail



def normalize(job):


    return {

        "title":
        job.get("title",""),

        "company":
        job.get("company",""),

        "location":
        job.get("location",""),

        "description":
        job.get("description",""),

        "contract":
        job.get("contract",""),

        "link":
        job.get("link","")

    }




def search_jobs():


    jobs=[]



    collectors=[

        search_france_travail,

        search_greenhouse,

        search_lever,

        search_teamtailor

    ]



    for collector in collectors:


        try:


            result = collector()


            print(

                collector.__name__,

                len(result)

            )


            jobs.extend(result)



        except Exception as e:


            print(

                "Erreur",

                collector.__name__,

                e

            )



    final=[]



    for job in jobs:


        job = normalize(job)



        if not job["link"].startswith(
            "http"
        ):

            continue



        final.append(job)



    print(

        "Offres avant filtre:",

        len(final)

    )


    return final