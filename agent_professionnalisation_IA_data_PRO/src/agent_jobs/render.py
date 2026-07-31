from datetime import datetime



def render_email(jobs):


    date = datetime.now().strftime(
        "%d/%m/%Y"
    )


    subject = (

        "Offres IA Data - "

        + date

    )



    html = f"""

<html>

<body>


<h2>
Offres IA / Big Data / Machine Learning
</h2>


<p>
Recherche quotidienne pour Mastère Spécialisé Expert Big Data et IA
</p>


<h3>
Date : {date}
</h3>


"""



    if not jobs:


        html += """

<h3>
Aucune offre trouvée aujourd'hui
</h3>

"""



    for job in jobs:


        html += f"""


<hr>


<h3>

{job['title']}

</h3>


<b>

Entreprise :

</b>

{job['company']}


<br>


<b>

Localisation :

</b>

{job['location']}


<br>


<b>

Score IA/Data :

</b>

{job.get('score',0)}/100


<br><br>



<a href="{job['link']}">

Voir l'offre

</a>


<br>


"""


    html += """

</body>

</html>

"""


    return subject, html