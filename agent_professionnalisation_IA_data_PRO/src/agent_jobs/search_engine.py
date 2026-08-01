from .collectors.france_travail import search_france_travail
from .collectors.apec import search_apec
from .collectors.hellowork import search_hellowork
from .collectors.jobup import search_jobup
from .collectors.teamtailor import search_teamtailor
from .collectors.company_careers import search_company_careers



def normalize(job):

    return {

        "title": job.get("title",""),

        "company": job.get("company",""),

        "location": job.get("location",""),

        "description": job.get("description",""),

        "link": job.get("link","")

    }



def search_jobs():


    jobs = []


    collectors = [

        search_france_travail,

        search_apec,

        search_hellowork,

        search_jobup,

        search_teamtailor,

        search_company_careers

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
                collector.__name__,
                e
            )


    unique = []

    seen = set()


    for job in jobs:


        job = normalize(job)


        key = (

            job["title"],

            job["company"]

        )


        if key not in seen:

            seen.add(key)

            unique.append(job)



    print(
        "TOTAL EUROPE:",
        len(unique)
    )


    return unique
