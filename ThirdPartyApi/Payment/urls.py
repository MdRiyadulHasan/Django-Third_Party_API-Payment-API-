# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('p/', views.payment_view, name='payment'),
]
    