import requests


def search_hellowork():


    jobs=[]


    url="https://www.hellowork.com"


    keywords=[

        "Data Engineer",
        "IA",
        "Machine Learning"

    ]


    for k in keywords:


        jobs.append({

            "title":k,

            "company":"HelloWork",

            "location":"France",

            "description":
            "Offre HelloWork Data IA",

            "link":url

        })


    return jobs