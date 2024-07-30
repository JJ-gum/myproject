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


#### Uwierzytelnianie i Autoryzacja
