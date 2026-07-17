from .search_engine import search_jobs
from .emailer import send_email


def main():


    print("===================================")
    print("Agent professionnalisation IA Data")
    print("Recherche offres Big Data / IA")
    print("===================================")



    jobs = search_jobs()



    print(
        f"Offres brutes trouvées : {len(jobs)}"
    )



    if not jobs:


        subject = (
            "Aucune offre trouvée - "
            "Contrat professionnalisation Big Data IA"
        )


        text = """

Agent professionnalisation IA Data

Aucune offre exploitable trouvée aujourd'hui.

Critères :

- Contrat de professionnalisation
- Graduate Program
- Expert Big Data Engineer
- AI Engineer
- Data Engineer
- MLOps
- LLM
- Deep Learning
- Energie
- Oil & Gas
- Mining
- Aéronautique


"""


    else:


        subject = (
            f"{len(jobs)} offres ciblées "
            "Professionnalisation Big Data IA"
        )



        text = """

OFFRES CIBLEES CONTRAT DE PROFESSIONNALISATION
BIG DATA / IA

"""


        for index, job in enumerate(jobs,1):


            text += f"""

============================

OFFRE {index}


Poste :
{job.get('title','')}


Entreprise :
{job.get('company','')}


Lieu :
{job.get('location','')}


Lien :
{job.get('link','')}


"""


    send_email(

        subject=subject,

        text=text

    )



if __name__ == "__main__":

    main()