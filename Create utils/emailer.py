import smtplib
from config import SMTP_EMAIL, SMTP_PASSWORD, RECEIVER_EMAIL

def send_email_notification(name, email, phone, interest):
    subject = f"New Lead from {name}"
    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nInterest: {interest}"
    email_text = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, RECEIVER_EMAIL, email_text)
