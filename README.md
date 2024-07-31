# BAZA DANYCH
## Wstęp
Program ma na celu edycję bazy danych zawierającej:
- urządzenia,
- systemy operacyjne,
- zgłoszenia.

Aplikacja powstała w celu przystosowania istniejącej bazy danych,
do automatycznego generowania raportów zgłoszeń w formacie `.docx`.

Program wykorzystuje Panel Administracyjny Django do funkcjonowania.

## Wymagane biblioteki
- Django 5.0.7 lub nowsza,
- pandas 2.2.2 lub nowsza,
- python-docx 1.1.2 lub nowsza,
- Oczywiście wymagany jest też Python 3.12 lub nowszy.

### Instalacja:
```
pip install Django pandas python-docx
```

## Użytkowanie programu:
### Widok główny:
Składa się tylko z informacji o tym, że trzeba użytkować program
przez PA Django.
### Panel Administratora Django:
Dociera się do niego przez wejście w `AdresStrony/admin`.
Dostępny jest tylko po zalogowaniu się hasłem.
Obsługuje całą funkcjonalność programu.
Dzieli się na 2 główne widoki:
#### Baza Danych
Dzieli się na 3 podstrony:
- Systemy operacyjne,
- Urządzenia,
- Zgłoszenia.
Obsługa tych podstron będzie omówiona poniżej.

#### Uwierzytelnianie i Autoryzacja
W tym miejscu można edytować listę użytkowników 
oraz przyznawać im uprawnienia.

## Systemy Operacyjne
Kliknięcie tej opcji w Panelu Administracyjnym umożliwia 
otworzenie i edycję listy wszystkich systemów operacyjnych.

Systemy są uszeregowane w kolejności dodania, można je usunąć 
za pomocą rozwijanej listy bądź dodać za pomocą `+` znajdującego
się po prawej stronie ekranu.

## Urządzenia
Kliknięcie tej opcji w Panelu Administracyjnym umożliwia 
otworzenie i edycję listy wszystkich urządzeń.

Urządzenia są uszeregowane w kolejności dodania, można je usunąć 
za pomocą rozwijanej listy bądź dodać za pomocą `+` znajdującego
się po prawej stronie ekranu. Oprócz ID wyświetlane są także 
**data rejestracji**, **laboratorium** oraz **numer ewidencyjny**.

## Zgłoszenia
Kliknięcie tej opcji w Panelu Administracyjnym umożliwia 
otworzenie i edycję listy wszystkich zgłoszeń.

Zgłoszenia są uszeregowane w kolejności dodania, można wygenerować
zgłoszenie w formacie `.docx` lub usunąć za pomocą rozwijanej listy 
bądź dodać za pomocą `+` znajdującego się po prawej stronie ekranu. 
Oprócz ID wyświetlane są także 
**numer EZD ID koszulki**, **numer zgłoszenia**, **data zgłoszenia**,
**nazwa zakładu**, **nazwa laboratorium** i **ID urządzenia**
będącego przedmiotem zgłoszenia. Wyświetlane zgłoszenia można
sortować i filtrować po każdym z wymienionych pól.