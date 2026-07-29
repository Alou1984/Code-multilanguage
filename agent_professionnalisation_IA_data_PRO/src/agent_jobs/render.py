from datetime import datetime


def render_email(jobs):

    date = datetime.now().strftime("%d/%m/%Y")

    subject = (
        f"Offres professionnalisation IA Data "
        f"Big Data Engineer - {date}"
    )


    if not jobs:

        html = """
        <html>
        <body>

        <h2>
        Aucune offre exploitable trouvée aujourd'hui.
        </h2>

        <p>
        Critères recherchés :
        </p>

        <ul>
            <li>Expert Big Data Engineer</li>
            <li>AI Engineer</li>
            <li>Data Engineer</li>
            <li>MLOps Engineer</li>
            <li>LLM Engineer</li>
            <li>Machine Learning</li>
            <li>Deep Learning</li>
            <li>Energie</li>
            <li>Oil & Gas</li>
            <li>Mining</li>
            <li>Aéronautique</li>
        </ul>

        </body>
        </html>
        """

        return subject, html



    html = """
    <html>
    <body>

    <h2>
    Offres ciblées IA Data Big Data Engineer
    </h2>

    """


    for job in jobs:

        html += f"""

        <hr>

        <h3>
        ⭐ Score : {job.get('score','')}
        </h3>

        <b>
        {job.get('title','')}
        </b>

        <br>

        Entreprise :
        {job.get('company','')}

        <br>

        Localisation :
        {job.get('location','')}

        <br><br>

        <a href="{job.get('link','')}">
        Voir l'offre
        </a>

        <br>

        """



    html += """

    </body>
    </html>

    """

    return subject, html