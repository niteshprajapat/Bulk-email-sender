import pandas as pd
import smtplib

e=pd.read_excel("D:\Email.xlsx") # enter excel file path where you store all email addresses
emails=e['Emails'].values
server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login('enter your email address','enter your password !!')
msg="hello this is for testing purpose !!"
subject="hello everyone"
body="Subject : {}\n {}".format(subject,msg)

for email in emails:
    server.sendmail('npanonymous7918@gmail.com',email,body)
server.close()
