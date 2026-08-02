from .collectors.greenhouse import search_greenhouse
from .collectors.lever import search_lever
from .collectors.teamtailor import search_teamtailor
from .collectors.france_travail import search_france_travail



def search_jobs():


    jobs=[]


    collectors=[

        search_greenhouse,

        search_lever,

        search_teamtailor,

        search_france_travail

    ]



    for collector in collectors:


        try:


            result=collector()


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


    return jobs