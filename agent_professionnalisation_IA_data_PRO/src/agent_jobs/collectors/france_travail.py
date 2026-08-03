import os
import requests


SEARCH_TERMS = [

    "Data Engineer",
    "AI Engineer",
    "Machine Learning Engineer",
    "MLOps",
    "Big Data",
    "Intelligence Artificielle"

]


def search_france_travail():

    client_id = os.getenv(
        "FRANCE_TRAVAIL_CLIENT_ID"
    )

    client_secret = os.getenv(
        "FRANCE_TRAVAIL_CLIENT_SECRET"
    )


    if not client_id or not client_secret:

        print(
            "France Travail API non configurée"
        )

        return []


    jobs=[]


    try:

        token=requests.post(

            "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=/partenaire",

            data={

                "grant_type":"client_credentials",

                "client_id":client_id,

                "client_secret":client_secret,

                "scope":"api_offresdemploiv2 o2dsoffre"

            }

        ).json()



        access_token=token.get(
            "access_token"
        )



        headers={

            "Authorization":
            "Bearer "+access_token

        }



        for term in SEARCH_TERMS:


            response=requests.get(

                "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search",

                params={

                    "motsCles":term,

                    "range":"0-20"

                },

                headers=headers

            )


            data=response.json()



            for offer in data.get(
                "resultats",
                []
            ):


                jobs.append({

                    "title":
                    offer.get(
                        "intitule",
                        ""
                    ),

                    "company":
                    offer.get(
                        "entreprise",
                        {}
                    ).get(
                        "nom",
                        ""
                    ),

                    "location":
                    offer.get(
                        "lieuTravail",
                        {}
                    ).get(
                        "libelle",
                        ""
                    ),

                    "description":
                    offer.get(
                        "description",
                        ""
                    ),

                    "contract":
                    offer.get(
                        "typeContrat",
                        ""
                    ),

                    "link":
                    offer.get(
                        "origineOffre",
                        {}
                    ).get(
                        "urlOrigine",
                        ""
                    )

                })



    except Exception as e:

        print(
            "France Travail:",
            e
        )


    return jobs