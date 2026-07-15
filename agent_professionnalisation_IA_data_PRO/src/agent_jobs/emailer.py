import os
import smtplib
from email.message import EmailMessage

def send_email(subject, text):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.environ["EMAIL_FROM"]
    msg["To"] = os.environ["EMAIL_TO"]
    msg.set_content(text)

    with smtplib.SMTP_SSL(
        os.environ["SMTP_HOST"],
        int(os.environ.get("SMTP_PORT", "465"))
    ) as smtp:
        smtp.login(
            os.environ["SMTP_USER"],
            os.environ["SMTP_PASSWORD"]
        )
        smtp.send_message(msg)
