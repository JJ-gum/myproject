from django.test import TestCase
from .models import Urzadzenie, SystemOperacyjny
from .admin import Zgloszenie
from django.contrib import admin
from django.urls import reverse


class UrzadzenieModelTest(TestCase):
    def test_urzadzenie_creation(self):
        urzadzenie = Urzadzenie.objects.create(
            laboratorium="Laboratorium Testowe",
            nr_pomieszczenia="101",
            typ_urzadzenia="PC"
        )
        self.assertEqual(str(urzadzenie), "Laboratorium Testowe - 101 - PC - 1")

    def test_system_operacyjny_many_to_many(self):
        urzadzenie = Urzadzenie.objects.create(
            laboratorium="Laboratorium Testowe",
            nr_pomieszczenia="101"
        )
        os1 = SystemOperacyjny.objects.create(typ_system_operacyjny="Linux")
        os2 = SystemOperacyjny.objects.create(typ_system_operacyjny="Windows")
        urzadzenie.system_operacyjny.set([os1, os2])
        self.assertEqual(urzadzenie.system_operacyjny.count(), 2)


class ZgloszenieFormularzTest(TestCase):
    def test_zgloszenie_form_valid(self):
        form_data = {
            'nr_zgloszenia': '12345',
            'nazwa_zakladu': 'Zakład Badań Certyfikacyjnych (Z1)',
            'zglaszajacy': 'Jan Kowalski',
            'data_zgloszenia': '2024-07-30',
        }
        form = Zgloszenie(data=form_data)
        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")


class ViewsTest(TestCase):
    def test_default_message_view(self):
        response = self.client.get(reverse('default_message'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "Korzystaj ze strony administratora")

class TemplateTest(TestCase):
    def test_default_message_template(self):
        response = self.client.get(reverse('default_message'))
        self.assertTemplateUsed(response, 'bazadanych/default_message.html')  # Użyj nazwy szablonu
        self.assertContains(response, "<h1>Korzystaj ze strony administratora</h1>")
