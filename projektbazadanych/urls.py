from django.contrib import admin
from django.urls import path, include
# Wszystkie ścieżki wyświetlające zaimplementowane widoki aplikacji
# W przypadku tej aplikacji jest to podstawowa wiadomość
# Oraz widok strony administratora wraz z wszystkimi podstronami
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bazadanych.urls')),
]
