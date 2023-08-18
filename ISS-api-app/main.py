import requests
import pandas as pd
from datetime import datetime

MY_LONGITUDE = 73.743202
MY_LATITUDE  = 18.589800
NOW = datetime.now()

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data = pd.json_normalize(response.json())

# iss_lattitude = data['iss_position.latitude'][0]
# iss_longitude = data['iss_position.longitude'][0]

# print(data)
# print(iss_longitude)
# print(iss_lattitude)

parameters = {
    'lat'      : MY_LATITUDE,
    'lng'      : MY_LONGITUDE,
    'formatted': 0,
}

response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()

data    = pd.json_normalize(response.json()['results'])
sunrise = data['sunrise'][0]
sunset  = data['sunset'][0]


print(sunrise)
print(sunset)