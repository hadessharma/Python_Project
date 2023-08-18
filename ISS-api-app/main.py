import requests
import pandas as pd
from datetime import datetime, timezone
import smtplib

MY_EMAIL     = "" # address to send the email from
MY_PASSWORD  = "" # secret key for the same email to establish the connection
MY_LONGITUDE = 73.743202
MY_LATITUDE  = 18.589800
NOW          = datetime.now(timezone.utc)


# calling ISS position api through the function
def call_iss_api():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = pd.json_normalize(response.json())

    iss_lattitude = data['iss_position.latitude'][0]
    iss_longitude = data['iss_position.longitude'][0]

    return iss_lattitude, iss_longitude


# calling sunrise-sunset api for my current location
def call_sun_api():
    parameters = {
        'lat'      : MY_LATITUDE,
        'lng'      : MY_LONGITUDE,
        'formatted': 0,
    }

    response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
    response.raise_for_status()


    data    = pd.json_normalize(response.json()['results'])
    sunrise = data['sunrise'][0].split('T')[1].split(':')[0]
    sunset  = data['sunset'][0].split('T')[1].split(':')[0]

    return sunrise, sunset


def send_mail():
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()

        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg='Subject:Look up for the ISS\n\nThe ISS is over you, look up in the night sky!')


lat    , lng   = call_iss_api()
sunrise, sunset = call_sun_api()

if abs(MY_LATITUDE - lat) < 10 and abs(MY_LONGITUDE - lng) < 10:
    if NOW.hour <= sunrise or NOW.hour >= sunset:
        send_mail()
