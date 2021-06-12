import smtplib

my_email = "enetr your email"
my_pass = "enter email passs"
# smplib.smtp is the key  for start the smtplib
with  smtplib.SMTP("smtp.gmail.com") as connection:
# it is  used to send mail in encrypt type
    Connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs="sendermail"
                msg="you want send msg to sender"
    )