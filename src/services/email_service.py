import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "your-email@gmail.com"
SMTP_PASSWORD = "your-email-password"

def send_email(to_email, subject, body):
    """
    Sends a single email.
    """
    try:
        msg = MIMEMultipart()
        msg["From"] = SMTP_USERNAME
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_bulk_emails(email_list, subject, body):
    """
    Sends bulk emails to a list of recipients.
    """
    for email in email_list:
        send_email(email, subject, body)