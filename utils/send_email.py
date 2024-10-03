import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

smtp_server = config.SMTP_HOST
smtp_port = config.SMTP_PORT
username = config.SMTP_USERNAME
password = config.SMTP_PASSWORD

def send_email(sender: str, receiver: str, subject: str, message: str):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'html'))

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
            smtp.login(username, password)
            smtp.send_message(msg)
            print('Email sent successfully.')

    except Exception as e:
        print(f'Error: {e}')