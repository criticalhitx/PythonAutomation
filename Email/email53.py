from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

msg = MIMEMultipart()
msg.attach(MIMEText(open("GCP_Training.pdf").read()))

import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com")
server.login("clink200032@gmail.com", "@@@")
server.sendmail("clink200032@gmail.com",
                "samhosgrace2@gmail.com",
                msg.as_string())
server.quit()
            
