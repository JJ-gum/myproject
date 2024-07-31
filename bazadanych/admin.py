from django.contrib import admin
from .models import Zgloszenie, Urzadzenie, SystemOperacyjny
from .functions import export_urzadzenie_to_csv, export_zgloszenie_to_csv,export_system_operacyjny_to_csv, generate_docx

# Opis funkcji — napis wyświetlany przy wybraniu tej opcji w panelu administratora
generate_docx.short_description = "Wygeneruj formularz w formacie .docx"
export_zgloszenie_to_csv.short_description = "Wyeksportuj zgłoszenia do csv"
export_urzadzenie_to_csv.short_description = "Wyeksportuj urządzenia do csv"
export_system_operacyjny_to_csv.short_description = "Wyeksportuj systemy operacyjne do csv"


# Ustawienia dotyczące wyświetlania Zgłoszenia w panelu administratora
@admin.register(Zgloszenie)
class Zgloszenie(admin.ModelAdmin):
    list_display = ('id', 'nr_EZD_ID_koszulki', 'nr_zgloszenia', 'data_zgloszenia', 'nazwa_zakladu', 'laboratorium', 'urzadzenie_id',)
    search_fields = ('nr_zgloszenia', 'data_zgloszenia', 'nazwa_zakladu', 'laboratorium', 'nr_EZD_ID_koszulki', 'urzadzenie_id')
    list_filter = ('data_zgloszenia', 'nazwa_zakladu', 'laboratorium',)
    ordering = ('-id',)
    # Dodatkowe akcje dostępne w PA
    actions = [generate_docx, export_zgloszenie_to_csv]


# Ustawienia dotyczące wyświetlania Urządzenia w panelu administratora
@admin.register(Urzadzenie)
class Urzadzenie(admin.ModelAdmin):
    list_display = ('pim_id', 'data_rejestracji', 'laboratorium', 'numer_ewidencyjny')
    search_fields = ('pim_id', 'data_rejestracji', 'numer_ewidencyjny')
    list_filter = ('laboratorium',)
    ordering = ('-pim_id',)
    # Dodatkowe akcje dostępne w PA
    actions = [export_urzadzenie_to_csv]


# Ustawienia dotyczące wyświetlania Systemu operacyjnego w panelu administratora
@admin.register(SystemOperacyjny)
class SystemOperacyjny(admin.ModelAdmin):
    list_display = ('typ_system_operacyjny',)
    actions = [export_system_operacyjny_to_csv]
