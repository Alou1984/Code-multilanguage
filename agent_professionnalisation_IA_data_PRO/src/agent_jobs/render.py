from datetime import datetime



def render_email(jobs):


    date=datetime.now().strftime("%d/%m/%Y")


    subject=(

        "Offres IA Big Data Europe - "

        +date

    )


    html=f"""

<h2>
Recherche IA / Big Data Europe
</h2>


<p>
Mastère Spécialisé Expert Big Data et IA
</p>


<p>
Date : {date}
</p>

"""


    if not jobs:


        html += """

<h3>
Aucune offre compatible aujourd'hui.
</h3>

<p>
Le moteur a exécuté la recherche mais aucune offre IA/Data exploitable n'a été retenue.
</p>

"""



    for job in jobs:


        html += f"""

<hr>


<h3>
{job.get('title')}
</h3>


Entreprise :
{job.get('company')}


<br>


Localisation :
{job.get('location')}


<br>


Score :
{job.get('score')}


<br><br>


<a href="{job.get('link')}">
Voir l'offre
</a>

"""


    return subject,html