from .collectors.france_travail import search_france_travail
from .collectors.greenhouse import search_greenhouse
from .collectors.lever import search_lever
from .collectors.teamtailor import search_teamtailor



def enrich_contract(job):


    text=(

        job.get("title","")

        +" "

        +job.get("description","")

    ).lower()



    contracts=[

        "alternance",

        "apprentissage",

        "professionnalisation",

        "graduate",

        "junior",

        "stage"

    ]



    for contract in contracts:


        if contract in text:

            job["contract"]=contract

            return job



    job["contract"]=""

    return job




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


            jobs.extend(

                collector()

            )


        except Exception as e:


            print(e)



    final=[]



    for job in jobs:


        job=enrich_contract(job)



        if job.get("link","").startswith("http"):

            final.append(job)



    return final