#Enable sending mail, in gmail: https://myaccount.google.com/u/3/lesssecureapps
#Multipurpose Internet Mail Extensions (MIME) 
#reading: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types

#Beautify with HTML: https://docs.python.org/2/library/email-examples.html#id5
# Courtesy : geeksforgeeks.com : https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/

# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#The mail addresses and password
sender_address = 'bitsandbytes01000100@gmail.com'
sender_password = 'BitsAndBytes123'

def send_mail(rcvr_mailid, subject_line, mail_text, attachment=''):
    fromaddr = sender_address
    toaddr = rcvr_mailid

    # instance of MIMEMultipart 
    msg = MIMEMultipart() 

    # storing the senders email address 
    msg['From'] = fromaddr 

    # storing the receivers email address 
    msg['To'] = toaddr 

    # storing the subject 
    msg['Subject'] = subject_line

    # string to store the body of the mail 
    body = mail_text

    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 

    # open the file to be sent 
    if attachment == '':
        pass
    else:
        filename = attachment
        attachment = open(filename, "rb") 

        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 

        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 

        # encode into base64 
        encoders.encode_base64(p) 

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(fromaddr, sender_password) 

    # Converts the Multipart msg into a string 
    text = msg.as_string() 

    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 

    # terminating the session 
    s.quit() 