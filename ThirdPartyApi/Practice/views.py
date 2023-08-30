import requests
from django.shortcuts import render
from .utils import get_weather

def api_example(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    results = {
        "id": [posts[i]['id'] for i in range(len(posts)) if i % 10 == 0],
        "title": [posts[i]['title'] for i in range(len(posts)) if i % 10 == 0],
    }

    context = {'results': results}
    return render(request, 'Practice/index.html', context)

def weather_view(request):
    city = request.GET.get('city', 'New York')
    weatherData = get_weather(city)
    context = {"weatherData":weatherData, "city":city}
    return render(request, 'Practice/index.html', context)