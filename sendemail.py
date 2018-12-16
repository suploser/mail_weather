#/usr/bin/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr,formataddr

from weather import get_data,render_email
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
    
#from_addr=input('From:')

from_addr='****'
#password=input('Password:')
password='******'
#to_addr=input('To:')

to_addr='******'
#smtp_server=input('SMTP server:')
smtp_server='smtp.163.com'

content=render_email(get_data())
msg=MIMEMultipart()
msg.attach(MIMEText(content,'html','utf-8'))
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('儿子<%s>'%to_addr)
msg['Subject']=Header('天气预报','utf-8').encode()


server=smtplib.SMTP(smtp_server,25)
#server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()



