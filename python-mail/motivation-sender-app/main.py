import smtplib
import secret as sec
import datetime as dt
import random

DAY_TO_SEND = 3 # 0-6 from Mon-Sun

# pulling secrets
my_email = sec.email
my_password = sec.key

# sending motivational quote via email
def send_motivational_mail() -> None:
    with open(file="./python-mail/quotes.txt", mode='r') as quotes:
        quote_list = quotes.read().split('\n')
        quote = random.choice(quote_list)

    with smtplib.SMTP('smtp.gmail.com', port= 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'Subject: Weekly dose of motivation\n\n{quote}')

# find the day of the week
now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == DAY_TO_SEND:
    send_motivational_mail()
