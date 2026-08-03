from datetime import datetime



def render_email(jobs):


    date = datetime.now().strftime("%d/%m/%Y")


    subject = (
        "Offres Alternance IA / Big Data Europe - "
        + date
    )


    html = f"""

<html>

<body>

<h2>
Recherche Alternance IA / Big Data Europe
</h2>


<p>
<b>Mastère Spécialisé Expert Big Data et IA</b>
</p>


<p>
Date de recherche : {date}
</p>


<hr>

"""


    if not jobs:


        html += """

<h3>
Aucune offre compatible trouvée aujourd'hui.
</h3>


<p>
Critères recherchés :
</p>

<ul>

<li>Data Engineer</li>

<li>Big Data Engineer</li>

<li>AI Engineer</li>

<li>Machine Learning Engineer</li>

<li>MLOps Engineer</li>

<li>LLM Engineer</li>

<li>Alternance / Apprentissage / Graduate Program</li>

<li>France / Europe</li>

</ul>

"""


    else:


        html += f"""

<h3>
{len(jobs)} offres détectées
</h3>

"""


        for index, job in enumerate(jobs, start=1):


            html += f"""

<table border="0" cellpadding="5">


<tr>

<td>

<h3>
#{index} - {job.get('title','Non renseigné')}
</h3>


<b>Entreprise :</b>

{job.get('company','Non renseigné')}


<br>


<b>Localisation :</b>

{job.get('location','Europe')}


<br>


<b>Contrat :</b>

{job.get('contract','Non indiqué')}


<br>


<b>Score IA/Data :</b>

{job.get('score',0)}/100


<br><br>


<a href="{job.get('link','#')}">

Voir l'offre et candidater

</a>


</td>

</tr>


</table>


<hr>


"""


    html += """

<p>

Agent automatique de recherche emploi IA/Data.

</p>


</body>

</html>

"""


    return subject, html