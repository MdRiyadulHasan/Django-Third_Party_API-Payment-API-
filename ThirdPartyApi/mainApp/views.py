import requests
from django.conf import settings
from django.shortcuts import render
import datetime


def Practice(request):
    # city = request.GET.get('city', 'London')  # Default to London if no city is provided
    city = request.GET.get('city', 'London')
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)

    print("Response Riyad .... ", response)
    response_data = response.json()
    print("Data Riyad .... ", response_data)
    # response_data = {
    #     'coord': {'lon': -0.1257, 'lat': 51.5085},
    #     'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'},{'id': 801, 'main': 'Not Hazy', 'description': 'Not clear sky', 'icon': '02d'},{'id': 802, 'main': 'Very Hazy', 'description': 'Hazy sky', 'icon': '03d'}],
    #     'base': 'stations',
    #     'main': {'temp': 11.22, 'feels_like': 10.85, 'temp_min': 9.39, 'temp_max': 12.86, 'pressure': 1008, 'humidity': 94},
    #     'visibility': 10000,
    #     'wind': {'speed': 2.57, 'deg': 230},
    #     'clouds': {'all': 3},
    #     'dt': 1693117204,
    #     'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1693112678, 'sunset': 1693162807},
    #     'timezone': 3600,
    #     'id': 2643743,
    #     'name': 'London',
    #     'cod': 200
    # }

    result = {
        "longitude":response_data['coord']['lon'],
        "latitude":response_data['coord']['lat'],
        "description":[response_data['weather'][i]['description'] for i in range(len(response_data['weather']))],
        # "description":[response_data['weather'][i]['description'] for i in range(len(response_data['weather'])) if i%2==0],
        "main":  [response_data['weather'][i]['main'] for i in range(len(response_data['weather'])) if i%2==0],
        "temp_min": response_data['main']['temp_min'],
        "temp_max": response_data['main']['temp_max'],
        "City": city,
        'timezone': response_data['timezone'],
        'dt': response_data['dt'],
    }

    print("Result", result)

    return render(request, 'mainApp/hello.html')

def get_weather(request):
    city = request.GET.get('city', 'London')  # Default to London if no city is provided
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    print("data", data)

    context = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
    }
    return render(request, 'mainApp/index.html', {"infoData":context})


def IndexView(request):
    return render(request, 'mainApp/hello.html')

def workWithData(request):
   
# Example JSON response
    response_data = {
        'coord': {'lon': -0.1257, 'lat': 51.5085},
        'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'},{'id': 801, 'main': 'Hazy', 'description': 'Not clear sky', 'icon': '02d'}],
        'base': 'stations',
        'main': {'temp': 11.22, 'feels_like': 10.85, 'temp_min': 9.39, 'temp_max': 12.86, 'pressure': 1008, 'humidity': 94},
        'visibility': 10000,
        'wind': {'speed': 2.57, 'deg': 230},
        'clouds': {'all': 3},
        'dt': 1693117204,
        'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1693112678, 'sunset': 1693162807},
        'timezone': 3600,
        'id': 2643743,
        'name': 'London',
        'cod': 200
    }

    # Extracting and displaying relevant information
    temperature = response_data['main']['temp']
    description = response_data['weather'][0]['description']
    humidity = response_data['main']['humidity']
    wind_speed = response_data['wind']['speed']
    cloudiness = response_data['clouds']['all']
    sunrise_timestamp = response_data['sys']['sunrise']
    sunset_timestamp = response_data['sys']['sunset']

    sunrise_time = datetime.datetime.fromtimestamp(sunrise_timestamp)
    sunset_time = datetime.datetime.fromtimestamp(sunset_timestamp)

    print(f"Weather in {response_data['name']}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Cloudiness: {cloudiness}%")
    print(f"Sunrise Time: {sunrise_time}")
    print(f"Sunset Time: {sunset_time}")


