from django.contrib import admin
from django.http import HttpResponse
from .models import FormData
from docx import Document
import re

def generate_docx(modeladmin, request, queryset):
    for form_data in queryset:
        document = Document()
        document.add_heading('User Input', 0)
        document.add_paragraph(f"Nr zgłoszenia: {form_data.nr_zgloszenia}")
        document.add_paragraph(f"Data zgłoszenia: {form_data.data_zgloszenia}")
        document.add_paragraph(f"Nazwa zakładu: {form_data.nazwa_zakladu}")
        document.add_paragraph(f"Laboratorium: {form_data.laboratorium}")
        document.add_paragraph(f"Zgłaszający: {form_data.zglaszajacy}")
        document.add_paragraph(f"Telefon: {form_data.telefon}")
        document.add_paragraph(f"Nr pomieszczenia: {form_data.nr_pomieszczenia}")
        document.add_paragraph(f"Nazwa urządzenia: {form_data.nazwa_urzadzenia}")
        document.add_paragraph(f"Dostęp do sieci: {'Yes' if form_data.dostep_do_sieci else 'No'}")
        document.add_paragraph(f"Nr ewidencyjny: {form_data.nr_ewidencyjny}")
        document.add_paragraph(f"Nr gniazdka LAN: {form_data.nr_gniazdka_lan}")
        document.add_paragraph(f"Opis zgłoszenia: {form_data.opis_zgloszenia}")
        document.add_paragraph(f"Oczekiwania: {form_data.oczekiwania}")
        document.add_paragraph(f"Istotność poufności: {form_data.istotnosc_pouf}")
        document.add_paragraph(f"Istotność integralności: {form_data.istotnosc_integr}")
        document.add_paragraph(f"Istotność dostępności: {form_data.istotnosc_dost}")
        document.add_paragraph(f"Kierownik LIM opinia: {form_data.kierownik_lim_opinia}")
        document.add_paragraph(f"Kierownik LIM podpis: {form_data.kierownik_lim_podpis}")
        document.add_paragraph(f"Kierownik LIM data: {form_data.kierownik_lim_data}")
        document.add_paragraph(f"Kierownik KM opinia: {form_data.kierownik_km_opinia}")
        document.add_paragraph(f"Kierownik KM podpis: {form_data.kierownik_km_podpis}")
        document.add_paragraph(f"Kierownik KM data: {form_data.kierownik_km_data}")
        document.add_paragraph(f"Realizacja opis: {form_data.realizacja_opis}")
        document.add_paragraph(f"Realizacja podpis: {form_data.realizacja_podpis}")
        document.add_paragraph(f"Realizacja data: {form_data.realizacja_data}")
        document.add_paragraph(f"Potwierdzenie podpis: {form_data.potwierdzenie_podpis}")
        document.add_paragraph(f"Potwierdzenie data: {form_data.potwierdzenie_data}")

        # Clean the filename to avoid illegal characters
        cleaned_name = re.sub(r'[\\/*?:"<>|]', "", form_data.nr_zgloszenia)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={cleaned_name}.docx'
        document.save(response)
        return response

generate_docx.short_description = "Generate DOCX for selected entries"

@admin.register(FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = ('nr_zgloszenia', 'data_zgloszenia', 'nazwa_zakladu', 'laboratorium')
    search_fields = ('nr_zgloszenia', 'nazwa_zakladu')
    list_filter = ('data_zgloszenia',)
    actions = [generate_docx]
