import sys
from password import pwd_input
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import Encoders
from Tkinter import Tk
from tkFileDialog import askopenfilename
def runReq():
    print "Welcome to Gmail Encryption System, you can send your public key here~\r"
    print "~***********************************************************************~\r"
    print "Please input your email address:\r"
    from_addr = raw_input()
    password = pwd_input()
    print "\rPlease input the destination address:\r"
    to_addr = raw_input()
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Public Key File"
    body= "Hi I would like to Exchange Encrypted messages, this is my public key, please send me yours!"
    thebody = MIMEText(body, 'plain')
    msg.attach(thebody)
    print "Please select the public key file that you want to send:\r"
    Tk().withdraw()
    keyfile = askopenfilename()
    print(keyfile)
    attachment = MIMEBase('application', "octet-stream")
    attachment.set_payload(open(keyfile, "rb").read())
    Encoders.encode_base64(attachment)
    command= 'attachment; filename='
    command =command+from_addr+"_public.txt"
    attachment.add_header('Content-Disposition', command)
    msg.attach(attachment)
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(from_addr, password)
    mailserver.sendmail(from_addr, to_addr,msg.as_string())
    print "Done~\r"
    mailserver.quit()
