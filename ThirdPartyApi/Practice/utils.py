# weather/utils.py
import requests
import pycountry

def get_full_country_name(short_code):
    try:
        country = pycountry.countries.get(alpha_2=short_code)
        if country:
            return country.name
        else:
            return "Country not found"
    except AttributeError:
        return "Invalid short code"


def get_weather(city_name):
    api_key = '268abf382e131e57f9ac1a45962e327f'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        print("Data", data)
        weather = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'country':   get_full_country_name( data['sys']['country'])
        }
        return weather
    else:
        return None
