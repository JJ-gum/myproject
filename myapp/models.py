from django.db import models

class FormData(models.Model):
    nr_zgloszenia = models.CharField(max_length=100, blank=True, null=True)
    data_zgloszenia = models.DateField(blank=True, null=True)
    nazwa_zakladu = models.CharField(max_length=200, blank=True, null=True)
    laboratorium = models.CharField(max_length=200, blank=True, null=True)
    zglaszajacy = models.CharField(max_length=200, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    nr_pomieszczenia = models.CharField(max_length=100, blank=True, null=True)
    nazwa_urzadzenia = models.CharField(max_length=200, blank=True, null=True)
    dostep_do_sieci = models.BooleanField(blank=True, null=True)
    nr_ewidencyjny = models.CharField(max_length=100, blank=True, null=True)
    nr_gniazdka_lan = models.CharField(max_length=100, blank=True, null=True)
    opis_zgloszenia = models.TextField(blank=True, null=True)
    oczekiwania = models.TextField(blank=True, null=True)
    istotnosc_pouf = models.CharField(max_length=100, blank=True, null=True)
    istotnosc_integr = models.CharField(max_length=100, blank=True, null=True)
    istotnosc_dost = models.CharField(max_length=100, blank=True, null=True)
    kierownik_lim_opinia = models.TextField(blank=True, null=True)
    kierownik_lim_podpis = models.CharField(max_length=100, blank=True, null=True)
    kierownik_lim_data = models.DateField(blank=True, null=True)
    kierownik_km_opinia = models.TextField(blank=True, null=True)
    kierownik_km_podpis = models.CharField(max_length=100, blank=True, null=True)
    kierownik_km_data = models.DateField(blank=True, null=True)
    realizacja_opis = models.TextField(blank=True, null=True)
    realizacja_podpis = models.CharField(max_length=100, blank=True, null=True)
    realizacja_data = models.DateField(blank=True, null=True)
    potwierdzenie_podpis = models.CharField(max_length=100, blank=True, null=True)
    potwierdzenie_data = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nr_zgloszenia if self.nr_zgloszenia else 'No ID'
