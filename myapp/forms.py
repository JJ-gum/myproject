from django import forms
from .models import FormData

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = [
            'nr_zgloszenia', 'data_zgloszenia', 'nazwa_zakladu', 'laboratorium', 'zglaszajacy', 'telefon',
            'nr_pomieszczenia', 'nazwa_urzadzenia', 'dostep_do_sieci', 'nr_ewidencyjny', 'nr_gniazdka_lan',
            'opis_zgloszenia', 'oczekiwania', 'istotnosc_pouf', 'istotnosc_integr', 'istotnosc_dost',
            'kierownik_lim_opinia', 'kierownik_lim_podpis', 'kierownik_lim_data', 'kierownik_km_opinia',
            'kierownik_km_podpis', 'kierownik_km_data', 'realizacja_opis', 'realizacja_podpis', 'realizacja_data',
            'potwierdzenie_podpis', 'potwierdzenie_data'
        ]
