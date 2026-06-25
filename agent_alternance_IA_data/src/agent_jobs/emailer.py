from __future__ import annotations

from email.message import EmailMessage
from html import escape
from datetime import datetime
import os
import smtplib
import ssl

from .search import JobResult


def render_html(results: list[JobResult], target_program: str) -> str:
    today = datetime.now().strftime("%d/%m/%Y")
    rows = []
    for item in results:
        rows.append(
            f"""
            <tr>
              <td style="padding:10px;border-bottom:1px solid #ddd;">
                <a href="{escape(item.url)}" style="font-weight:bold;color:#0b57d0;">{escape(item.title)}</a><br>
                <span>{escape(item.company)} · {escape(item.location)} · {escape(item.source)}</span><br>
                <small>{escape(item.snippet[:500])}</small>
              </td>
            </tr>
            """
        )
    return f"""
    <html>
      <body style="font-family:Arial, sans-serif; line-height:1.45; color:#222;">
        <h2>Agent alternance IA & Data — offres du {today}</h2>
        <p><b>Objectif :</b> {escape(target_program)}</p>
        <p>Recherche: stage, internship/intership, graduate program, alternance, apprentissage — Big Data, IA, MLOps, systèmes embarqués, logiciel, intégration système, robotique, HVAC, oil & gas, mining.</p>
        <table style="border-collapse:collapse;width:100%;">{''.join(rows)}</table>
        <p style="font-size:12px;color:#666;margin-top:18px;">
          Conseil: ajoute le secret SERPAPI_API_KEY pour recevoir des offres individuelles automatiquement. Sans clé, l'agent envoie des liens de recherche ciblés par site.
        </p>
      </body>
    </html>
    """


def render_text(results: list[JobResult], target_program: str) -> str:
    lines = [
        "Agent alternance IA & Data",
        f"Objectif: {target_program}",
        "",
    ]
    for i, item in enumerate(results, start=1):
        lines.extend(
            [
                f"{i}. {item.title}",
                f"   Source: {item.source} | Lieu: {item.location} | Société: {item.company}",
                f"   Lien: {item.url}",
                f"   Note: {item.snippet[:250]}",
                "",
            ]
        )
    return "\n".join(lines)


def send_email(subject: str, html: str, text: str) -> None:
    host = os.getenv("SMTP_HOST", "smtp.mail.yahoo.com")
    port = int(os.getenv("SMTP_PORT", "465"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    sender = os.getenv("EMAIL_FROM", user or "")
    recipient = os.getenv("EMAIL_TO", "papalassane2003@yahoo.fr")

    missing = [name for name, value in {
        "SMTP_USER": user,
        "SMTP_PASSWORD": password,
        "EMAIL_FROM": sender,
        "EMAIL_TO": recipient,
    }.items() if not value]
    if missing:
        raise RuntimeError(f"Secrets manquants: {', '.join(missing)}")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(text)
    msg.add_alternative(html, subtype="html")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)
