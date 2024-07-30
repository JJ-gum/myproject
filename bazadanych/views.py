from django.shortcuts import render


# Wyświetlanie default wiadomości, gdy użytkownik wejdzie na stronę aplikacji,
# a nie na stronę Panelu Administracyjnego Django tak jak powinien
def default_message(request):
    # Lokalizacja pliku z wiadomością
    return render(request, 'bazadanych/default_message.html')
