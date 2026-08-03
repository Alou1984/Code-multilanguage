import os
import requests


def search_france_travail():

    jobs = []


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

        return jobs



    return jobs