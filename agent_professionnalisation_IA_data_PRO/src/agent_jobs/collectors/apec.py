import requests



def search_apec():


    jobs = []


    keywords = [

        "Data Engineer",

        "Ingénieur IA",

        "Machine Learning",

        "Big Data",

        "MLOps"

    ]



    for keyword in keywords:


        url = (

            "https://www.apec.fr/"
            "candidat/recherche-emploi.html"

        )


        try:


            response = requests.get(

                url,

                params={

                    "motsCles":
                    keyword

                },

                timeout=20

            )



            if response.status_code == 200:


                jobs.append({

                    "title":

                    keyword,


                    "company":

                    "APEC",


                    "location":

                    "France",


                    "description":

                    "Recherche APEC Data IA",


                    "link":

                    response.url

                })


        except Exception as e:


            print(
                "APEC:",
                e
            )


    return jobs