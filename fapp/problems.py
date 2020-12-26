import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from io import StringIO,BytesIO
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "misaljay1221@gmail.com"
receiver_email = "tanajim580@gmail.com"
password = "jaymisal123"

class Send_me:
    def __init__(self,name_user,email_user,message_user):
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "Your Website Issues"
        self.message["From"] = sender_email
        self.message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        html = f"""\
        <html>
        <body>
            <p>
                Name - > {name_user}<br>
                Email -> {email_user}<br>
                User's Issues -> {message_user}<br>
                Thankyou from user.
            </p>
        </body>
        </html>
        """

        part2 = MIMEText(html, "html")
        self.message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            # server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email,receiver_email,self.message.as_string())
Send_me('shubh','shubh@gmail.com','not working site')