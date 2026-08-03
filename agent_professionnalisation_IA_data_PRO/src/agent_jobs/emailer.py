import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(
    subject,
    html,
    text=""
):


    sender=os.getenv(
        "EMAIL_SENDER"
    )

    password=os.getenv(
        "EMAIL_PASSWORD"
    )

    receiver=os.getenv(
        "EMAIL_RECEIVER"
    )



    msg=MIMEMultipart(
        "alternative"
    )


    msg["Subject"]=subject

    msg["From"]=sender

    msg["To"]=receiver



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



    with smtplib.SMTP_SSL(

        "smtp.gmail.com",

        465

    ) as server:


        server.login(

            sender,

            password

        )


        server.sendmail(

            sender,

            receiver,

            msg.as_string()

        )



    print(

        "Email envoyé avec succès"

    )