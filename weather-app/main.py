import requests

parameters = {
    'lat'  : 18.580750,
    'lon'  : 73.744610,
    'appid': '84cfe15e61d71145d7601320c2ecff1a',
    # 'q'    : 'Pune'
}

will_rain = None

with requests.get(url='https://api.openweathermap.org/data/2.5/weather', params=parameters) as connection:
    connection.raise_for_status()
    
    weather = connection.json()
    if weather['weather'][0]['id'] > 700:
        will_rain = False
    else:
        will_rain = True
        
