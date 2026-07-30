from datetime import datetime



def render_email(jobs):


    date = datetime.now().strftime(
        "%d/%m/%Y"
    )


    subject = (

        "Agent professionnalisation IA Data - "

        + date

    )



    if not jobs:


        html = """

<h2>
Aucune offre reçue
</h2>

<p>
Le moteur SERPAPI n'a retourné aucune annonce.
</p>

<ul>

<li>Vérifier SERPAPI_API_KEY</li>

<li>Vérifier quota SERPAPI</li>

<li>Vérifier Google Jobs API</li>

</ul>

"""


        return subject, html




    html = """

<h2>
Offres IA Data trouvées
</h2>

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

Lieu :
{job.get('location')}

<br>

<a href="{job.get('link')}">
Voir l'offre
</a>

<br>

"""



    return subject, html