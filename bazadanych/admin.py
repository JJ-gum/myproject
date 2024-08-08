from django.contrib import admin
from django.urls import path
from .models import Zgloszenie, Urzadzenie, SystemOperacyjny
from .functions import (
    export_urzadzenie_to_csv, export_zgloszenie_to_csv, export_system_operacyjny_to_csv,
    generate_docx, view_urzadzenia, view_zgloszenia, view_urzadzenia_view, view_zgloszenia_view
)


# Ustawienia dotyczące wyświetlania Zgłoszenia w panelu administratora
@admin.register(Zgloszenie)
class ZgloszenieAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nr_EZD_ID_koszulki', 'nr_zgloszenia', 'data_zgloszenia', 'nazwa_zakladu', 'laboratorium', 'urzadzenie_id')
    search_fields = (
        'nr_zgloszenia', 'data_zgloszenia', 'nazwa_zakladu', 'laboratorium', 'nr_EZD_ID_koszulki', 'urzadzenie_id')
    list_filter = ('data_zgloszenia', 'nazwa_zakladu', 'laboratorium')
    ordering = ('-id',)
    actions = [generate_docx, export_zgloszenie_to_csv, view_urzadzenia]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('view_urzadzenia/<str:urzadzenie_ids>/', self.admin_site.admin_view(view_urzadzenia_view),
                 name='view_urzadzenia')
        ]
        return custom_urls + urls


# Ustawienia dotyczące wyświetlania Urządzenia w panelu administratora
@admin.register(Urzadzenie)
class UrzadzenieAdmin(admin.ModelAdmin):
    list_display = ('pim_id', 'data_rejestracji', 'laboratorium', 'numer_ewidencyjny')
    search_fields = ('pim_id', 'data_rejestracji', 'numer_ewidencyjny')
    list_filter = ('laboratorium',)
    ordering = ('-pim_id',)
    actions = [export_urzadzenie_to_csv, view_zgloszenia]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('view_zgloszenia/<str:urzadzenie_ids>/', self.admin_site.admin_view(view_zgloszenia_view),
                 name='view_zgloszenia')
        ]
        return custom_urls + urls


# Ustawienia dotyczące wyświetlania Systemu operacyjnego w panelu administratora
@admin.register(SystemOperacyjny)
class SystemOperacyjnyAdmin(admin.ModelAdmin):
    list_display = ('typ_system_operacyjny',)
    actions = [export_system_operacyjny_to_csv]
