from datetime import datetime



def render_email(jobs):


    subject=(

        "Alternance IA Data Europe - "

        +datetime.now().strftime("%d/%m/%Y")

    )



    html="""

<h2>
Recherche Alternance IA / Big Data Europe
</h2>

<p>
Mastère Spécialisé Expert Big Data et IA
</p>

"""



    if not jobs:


        html+="""


<h3>
Aucune offre compatible aujourd'hui
</h3>


"""


    for job in jobs:


        html+=f"""

<hr>

<h3>
{job['title']}
</h3>

Entreprise :
{job['company']}

<br>

Lieu :
{job['location']}

<br>

Contrat :
{job.get('contract','')}

<br>

Score :
{job.get('score',0)}

<br><br>


<a href="{job['link']}">
Candidater
</a>


"""



    return subject,html