from django.test import TestCase
from django.forms import ModelForm
from django.urls import reverse
from .models import Urzadzenie, SystemOperacyjny, Zgloszenie


class ZgloszenieModelForm(ModelForm):
    class Meta:
        model = Zgloszenie
        fields = ['nr_zgloszenia', 'nazwa_zakladu', 'zglaszajacy', 'data_zgloszenia']


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

        # Test usuwania systemu operacyjnego
        os1.delete()
        self.assertEqual(urzadzenie.system_operacyjny.count(), 1)


class ZgloszenieTest(TestCase):
    def test_zgloszenie_form_valid(self):
        form_data = {
            'nr_zgloszenia': '12345',
            'nazwa_zakladu': 'Zakład Badań Certyfikacyjnych (Z1)',
            'zglaszajacy': 'Jan Kowalski',
            'data_zgloszenia': '2024-07-30',
        }
        form = ZgloszenieModelForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")


class ViewsTest(TestCase):
    def test_default_message_view(self):
        response = self.client.get(reverse('default_message'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Korzystaj ze strony administratora")


class TemplateTest(TestCase):
    def test_default_message_template(self):
        response = self.client.get(reverse('default_message'))
        self.assertTemplateUsed(response, 'bazadanych/default_message.html')
        self.assertContains(response, "<h1>Korzystaj ze strony administratora</h1>")


def test_system_operacyjny_deletion(self):
    urzadzenie = Urzadzenie.objects.create(
        laboratorium="Laboratorium Testowe",
        nr_pomieszczenia="101"
    )
    os1 = SystemOperacyjny.objects.create(typ_system_operacyjny="Linux")
    os2 = SystemOperacyjny.objects.create(typ_system_operacyjny="Windows")
    urzadzenie.system_operacyjny.set([os1, os2])

    os1.delete()
    urzadzenie.refresh_from_db()
    self.assertEqual(urzadzenie.system_operacyjny.count(), 1)


def test_urzadzenie_full_info(self):
    urzadzenie = Urzadzenie.objects.create(
        laboratorium="Laboratorium Testowe",
        nr_pomieszczenia="101",
        typ_urzadzenia="PC"
    )
    os1 = SystemOperacyjny.objects.create(typ_system_operacyjny="Linux")
    urzadzenie.system_operacyjny.add(os1)

    self.assertEqual(urzadzenie.get_full_info(), "Laboratorium Testowe - 101 - PC - Linux")
