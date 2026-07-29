import os
import smtplib

from email.message import EmailMessage


def send_email(subject, html, text=None):

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "465"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    email_from = os.getenv("EMAIL_FROM")
    email_to = os.getenv("EMAIL_TO")


    missing = []

    for name, value in {

        "SMTP_HOST": smtp_host,
        "SMTP_USER": smtp_user,
        "SMTP_PASSWORD": smtp_password,
        "EMAIL_FROM": email_from,
        "EMAIL_TO": email_to

    }.items():

        if not value:
            missing.append(name)


    if missing:

        raise RuntimeError(
            "Secrets manquants: "
            + ", ".join(missing)
        )


    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = email_from
    msg["To"] = email_to


    if text:

        msg.set_content(text)

    else:

        msg.set_content(
            "Voir la version HTML"
        )


    msg.add_alternative(
        html,
        subtype="html"
    )


    with smtplib.SMTP_SSL(
        smtp_host,
        smtp_port
    ) as smtp:


        smtp.login(
            smtp_user,
            smtp_password
        )


        smtp.send_message(msg)


    print(
        "Email envoyé avec succès"
    )