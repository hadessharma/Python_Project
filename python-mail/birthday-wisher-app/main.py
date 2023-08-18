##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import smtplib
import pandas as pd
import os, os.path
import random

import secret # create a secret.py and add email and key

my_email = secret.email
my_key = secret.key

NOW = dt.datetime.now()
MONTH = NOW.month
DAY = NOW.day
YEAR = NOW.year


# check for the birthdays today
def check_birthday():
    birthdays = pd.read_csv('./python-mail/birthday-wisher-app/birthdays.csv')

    birthday_today = birthdays[(birthdays['day'] == DAY) & (birthdays['month'] == MONTH)]
    return birthday_today


# selecting a letter template
def select_letter():
    # counting number of templates
    count = 0
    for root_dir, cur_dir, files in os.walk('./python-mail/birthday-wisher-app/letter_templates'):
        count+=len(files)

    template_number = random.randint(1,count)
    
    # getting the content of the letter
    with open(file=f'./python-mail/birthday-wisher-app/letter_templates/letter_{template_number}.txt') as letter:
        letter_content = letter.read()

    return letter_content


# send birthday wishes over email
def send_birthday_wishes(letter, birthday):
    for ind in birthday.index:
        mail_content = letter.replace('[NAME]', birthday['name'][ind])
        
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_key)

            connection.sendmail(from_addr=my_email, to_addrs=birthday['email'][ind], msg=f'Subject:Birthay Wishes\n\n{mail_content}')



birthday_today = check_birthday()
letter_content = select_letter()

send_birthday_wishes(letter=letter_content, birthday=birthday_today)