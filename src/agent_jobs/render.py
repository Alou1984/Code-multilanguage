from __future__ import annotations

from html import escape
from .models import JobOffer
from .settings import HOME_POSTAL_CODE, HOME_CITY, RADIUS_KM


def render(offers: list[JobOffer]) -> tuple[str, str]:
    title = f"Offres ciblées alternance/stage Big Data IA — priorité {RADIUS_KM} km autour de {HOME_CITY} {HOME_POSTAL_CODE}"

    if not offers:
        text = (
            "Aucune offre ciblée exploitable n'a été trouvée aujourd'hui.\n\n"
            "Vérifie que SERPAPI_API_KEY est renseigné dans GitHub Secrets. "
            "Sans clé SerpApi, l'agent n'envoie plus de liens vides.\n"
        )
        html = f"""
        <html><body>
        <h2>{escape(title)}</h2>
        <p>Aucune offre ciblée exploitable n'a été trouvée aujourd'hui.</p>
        <p><b>À vérifier :</b> le secret GitHub <code>SERPAPI_API_KEY</code> doit être renseigné pour récupérer de vraies offres.</p>
        <p>L'agent n'envoie plus de liens vides ou de résultats à 0.</p>
        </body></html>
        """
        return html, text

    lines = [title, "", f"{len(offers)} offres triées par pertinence et proximité.", ""]
    items = []
    for i, o in enumerate(offers, 1):
        dist = f"{o.distance_km} km" if o.distance_km is not None else "distance non détectée"
        company = f" — {o.company}" if o.company else ""
        loc = f" — {o.location}" if o.location else ""
        lines.append(f"{i}. {o.title}{company}{loc}")
        lines.append(f"   Source: {o.source} | Score: {o.score} | Distance: {dist}")
        lines.append(f"   {o.url}")
        if o.snippet:
            lines.append(f"   {o.snippet[:240]}")
        lines.append("")

        items.append(f"""
        <li style="margin-bottom:18px">
          <a href="{escape(o.url)}"><b>{escape(o.title)}</b></a><br/>
          <span>{escape(o.company or 'Entreprise non détectée')} — {escape(o.location or 'Localisation non détectée')}</span><br/>
          <span>Source: {escape(o.source)} | Score: {o.score} | Distance: {escape(dist)}</span><br/>
          <p>{escape(o.snippet[:360])}</p>
        </li>
        """)

    html = f"""
    <html><body>
      <h2>{escape(title)}</h2>
      <p><b>{len(offers)}</b> offres triées par pertinence et proximité.</p>
      <p>Priorité : IA, data, nouvelles technologies, énergie, oil & gas, secteur minier, postes ingénieur/expert/chef de projet, stage/alternance/apprentissage/graduate program.</p>
      <ol>{''.join(items)}</ol>
    </body></html>
    """
    return html, "\n".join(lines)
