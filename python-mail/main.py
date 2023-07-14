import smtplib
import secret as sec

my_email = sec.email
my_password = sec.key

connection = smtplib.SMTP('smtp.gmail.com', port= 587)
connection.starttls()
connection.login(user=my_email, password=my_password)

connection.sendmail(from_addr=my_email, to_addrs=my_email, msg='Testing code')
connection.close()