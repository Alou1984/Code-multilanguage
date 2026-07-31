import os
import requests



TOKEN_URL = (
    "https://entreprise.francetravail.fr/"
    "connexion/oauth2/access_token"
)



API_URL = (
    "https://api.francetravail.io/"
    "partenaire/offresdemploi/v2/offres/search"
)



def get_token():


    client_id = os.getenv(
        "FT_CLIENT_ID"
    )


    client_secret = os.getenv(
        "FT_CLIENT_SECRET"
    )


    if not client_id or not client_secret:

        print(
            "France Travail API non configurée"
        )

        return None



    response = requests.post(

        TOKEN_URL,

        data={

            "grant_type":
            "client_credentials",

            "client_id":
            client_id,

            "client_secret":
            client_secret,

            "scope":
            "api_offresdemploiv2 o2dsoffre"

        }

    )


    return response.json().get(
        "access_token"
    )




def search_france_travail():


    token = get_token()


    if not token:

        return []



    headers = {

        "Authorization":
        f"Bearer {token}"

    }



    params = {

        "motsCles":
        "Data Engineer IA Machine Learning",

        "commune":
        "Sens"

    }



    response = requests.get(

        API_URL,

        headers=headers,

        params=params

    )



    data = response.json()


    jobs = []



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

            "link":
            offer.get(
                "origineOffre",
                {}
            ).get(
                "urlOrigine",
                ""
            )

        })



    return jobs