from datetime import datetime



def render_email(jobs):


    date=datetime.now().strftime(
        "%d/%m/%Y"
    )


    subject=(

        "Offres IA Big Data Europe - "

        +date

    )



    html=f"""

<h2>
Recherche IA / Big Data Europe
</h2>


<p>
<b>Mastère Spécialisé Expert Big Data et IA</b>
</p>


<p>
Date : {date}
</p>

<hr>

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



    else:


        for job in jobs:


            html += f"""

<h3>
{job.get('title')}
</h3>


Entreprise :
{job.get('company')}

<br>

Lieu :
{job.get('location')}

<br>

Contrat :
{job.get('contract')}

<br>

Score :
{job.get('score')}

<br><br>


<a href="{job.get('link')}">
Voir l'offre
</a>


<hr>

"""



    return subject, html