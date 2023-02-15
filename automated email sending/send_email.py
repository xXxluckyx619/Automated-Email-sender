import os
import smtplib
import ssl 
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

#read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")
psw_email = os.getenv("psw")
email_to = "xluckyx619@gmail.com"

# #testing connection

# message = "Dear god, Please Help!!"

# simple_email_context = ssl.create_default_context()

# try:
#     print("connecting to server...")
#     TIE_server = smtplib.SMTP(EMAIL_SERVER,PORT)
#     TIE_server.starttls(context=simple_email_context)
#     TIE_server.login(sender_email, psw_email)
#     print("connected to server :-)")

#     print()
#     print(f"sending email to - {email_to}")
#     TIE_server.sendmail(sender_email,email_to,message)
#     print(f"Email successfully sent to - {email_to}")

# except Exception as e:
#     print(e)

# finally:
#     TIE_server.quit()

def send_email(subject,receiver_email,name,due_date,invoice_no, amount):
    #create the base text message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("RavTechnologies incorporated.", f"{sender_email}"))
    msg["to"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        I hope you are well.
        I just wanted to drop you a quick note to remind you that {amount} USD in respect of our invoice {invoice_no} is due for payment on {due_date}.
        I would be really grateful if you could confirm that everything is on track for payment.
        Best regards
        YOUR NAME
        """
    )
    #html version that designs the text in the email content

    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to remind you that <strong>{amount} USD</strong> in respect of our invoice {invoice_no} is due for payment on <strong>{due_date}</strong>.</p>
        <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
        <p>Best regards</p>
        <p>YOUR NAME</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, psw_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="John Doe",
        receiver_email="xluckyx619@gmail.com",
        due_date="11, Aug 2022",
        invoice_no="INV-21-12-009",
        amount="5",
    )