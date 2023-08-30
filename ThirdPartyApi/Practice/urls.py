from django.urls import path
from . import views

urlpatterns = [
    path('getApi/', views.api_example, name = 'api_example'),
    path('w1/', views.weather_view, name = 'weather_view'),
]