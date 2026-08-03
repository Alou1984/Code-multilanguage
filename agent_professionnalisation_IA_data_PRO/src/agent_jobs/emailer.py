import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(
    subject,
    html,
    text=""
):


    sender = os.getenv(
        "EMAIL_SENDER"
    )


    password = os.getenv(
        "EMAIL_PASSWORD"
    )


    receiver = os.getenv(
        "EMAIL_RECEIVER"
    )



    if not sender:

        raise Exception(
            "EMAIL_SENDER manquant dans GitHub Secrets"
        )


    if not password:

        raise Exception(
            "EMAIL_PASSWORD manquant dans GitHub Secrets"
        )


    if not receiver:

        raise Exception(
            "EMAIL_RECEIVER manquant dans GitHub Secrets"
        )



    msg = MIMEMultipart(
        "alternative"
    )


    msg["Subject"] = subject

    msg["From"] = sender

    msg["To"] = receiver



    msg.attach(

        MIMEText(
            text,
            "plain"
        )

    )


    msg.attach(

        MIMEText(
            html,
            "html"
        )

    )



    try:


        server=smtplib.SMTP_SSL(

            "smtp.gmail.com",

            465

        )


        server.login(

            sender,

            password

        )


        server.sendmail(

            sender,

            receiver,

            msg.as_string()

        )


        server.quit()



        print(
            "Email envoyé avec succès"
        )



    except Exception as e:


        print(

            "ERREUR EMAIL:",

            e

        )

        raise