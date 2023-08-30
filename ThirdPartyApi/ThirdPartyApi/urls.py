from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainApp.urls")),
    path('practice/', include("Practice.urls")),
    path('payment/', include('Payment.urls')),
]
