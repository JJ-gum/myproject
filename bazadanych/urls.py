from django.urls import path
from . import views
# Wszystkie ścieżki wyświetlające zaimplementowane widoki aplikacji
# W przypadku tej aplikacji jest to tylko podstawowa wiadomość
urlpatterns = [
    path('', views.default_message, name='default_message'),
]
