from django.urls import path
from . import views

urlpatterns = [
    path('get-weather/', views.get_weather, name = 'get_weather'),
    path('IndexView/', views.IndexView, name = 'IndexView'),
    path('Practice/', views.Practice, name = 'Practice'),
]