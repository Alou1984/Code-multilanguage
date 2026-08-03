from .collectors.france_travail import search_france_travail
from .collectors.apec import search_apec
from .collectors.hellowork import search_hellowork
from .collectors.welcome_to_jungle import search_wttj
from .collectors.jobteaser import search_jobteaser

from .collectors.jobup import search_jobup
from .collectors.jobs_ch import search_jobs_ch

from .collectors.moovijob import search_moovijob
from .collectors.jobs_lu import search_jobs_lu

from .collectors.company_careers import search_company_jobs
from .collectors.workday import search_workday

from .collectors.greenhouse import search_greenhouse
from .collectors.lever import search_lever



def normalize(job):

    return {

        "title": job.get("title",""),

        "company": job.get("company",""),

        "location": job.get("location",""),

        "description": job.get("description",""),

        "contract": job.get("contract",""),

        "link": job.get("link","")

    }



def search_jobs():


    jobs=[]


    collectors=[


        search_france_travail,

        search_apec,

        search_hellowork,

        search_wttj,

        search_jobteaser,


        search_jobup,

        search_jobs_ch,


        search_moovijob,

        search_jobs_lu,


        search_company_jobs,

        search_workday,


        search_greenhouse,

        search_lever

    ]



    for collector in collectors:


        try:

            result = collector()


            print(

                "SOURCE:",

                collector.__name__,

                "=>",

                len(result)

            )


            jobs.extend(result)



        except Exception as e:


            print(

                "ERREUR:",

                collector.__name__,

                e

            )



    final=[]

    seen=set()



    for job in jobs:


        job=normalize(job)


        key=(

            job["title"],

            job["company"],

            job["link"]

        )


        if key in seen:

            continue


        seen.add(key)


        if job["link"]:

            final.append(job)



    print(

        "TOTAL OFFRES UNIQUES:",

        len(final)

    )


    return final

    return cleaned