from __future__ import annotations

import os
import smtplib
from email.message import EmailMessage


def send_email(subject: str, html: str, text: str) -> None:
    host = os.getenv("SMTP_HOST", "smtp.mail.yahoo.com").strip()
    port = int(os.getenv("SMTP_PORT") or "465")
    user = os.getenv("SMTP_USER", "").strip()
    password = os.getenv("SMTP_PASSWORD", "").strip()
    email_from = (os.getenv("EMAIL_FROM") or user).strip()
    email_to = os.getenv("EMAIL_TO", "").strip()

    missing = []
    for name, value in {
        "SMTP_HOST": host,
        "SMTP_USER": user,
        "SMTP_PASSWORD": password,
        "EMAIL_FROM": email_from,
        "EMAIL_TO": email_to,
    }.items():
        if not value:
            missing.append(name)
    if missing:
        raise RuntimeError(f"Secrets manquants: {', '.join(missing)}")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_from
    msg["To"] = email_to
    msg.set_content(text)
    msg.add_alternative(html, subtype="html")

    if port == 465:
        with smtplib.SMTP_SSL(host, port, timeout=45) as smtp:
            smtp.login(user, password)
            smtp.send_message(msg)
    else:
        with smtplib.SMTP(host, port, timeout=45) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(user, password)
            smtp.send_message(msg)
