from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re
import pandas as pd
import unicodecsv as csv
from django.http import HttpResponse
from .models import Urzadzenie, Zgloszenie, SystemOperacyjny
from datetime import datetime
from django.db import connection
from io import BytesIO


# Funkcja generująca plik csv dla Urządzenia
def export_urzadzenie_to_csv(modeladmin, request, queryset):
    # Tworzy odpowiedź HTTP z typem zawartości 'text/csv'
    response = HttpResponse(content_type='text/csv')
    # Generowanie nazw pliku z aktualną datą i czasem
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'urzadzenia_{now}.csv'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Tworzenie nazw kolumn
    writer = csv.writer(response)
    writer.writerow([
        'PIM ID', 'Laboratorium', 'Nr Pomieszczenia', 'Opis', 'Nr Ewidencyjny', 'Typ Urządzenia',
        'System Operacyjny', 'CPU', 'RAM', 'Pamięć Dysku', 'Dodatkowe Komponenty', 'Oprogramowanie Specjalne',
        'Konta', 'Data Rejestracji', 'Nr Gniazda', 'Typ Gniazda', 'Opiekun 1', 'Opiekun 2',
        'Typ Połączenia Sieciowego', 'Notatki'
    ])

    for urzadzenie in queryset:
        # Pobiera wartości z pola wiele-do-wielu jako ciąg rozdzielony przecinkami
        system_operacyjny = ', '.join([sys.typ_system_operacyjny for sys in urzadzenie.system_operacyjny.all()])

        # Zapisywanie danych do pliku CSV
        writer.writerow([
            urzadzenie.pim_id,
            urzadzenie.laboratorium or '',
            urzadzenie.nr_pomieszczenia or '',
            urzadzenie.opis or '',
            urzadzenie.numer_ewidencyjny or '',
            urzadzenie.typ_urzadzenia or '',
            system_operacyjny,
            urzadzenie.cpu or '',
            urzadzenie.ram or '',
            urzadzenie.pamiec_dysku or '',
            urzadzenie.dodatkowe_komponenty or '',
            urzadzenie.oprogramowanie_specjalne or '',
            urzadzenie.konta or '',
            urzadzenie.data_rejestracji or '',
            urzadzenie.nr_gniazda or '',
            urzadzenie.typ_gniazd or '',
            urzadzenie.opiekun_1 or '',
            urzadzenie.opiekun_2 or '',
            urzadzenie.typ_polaczenia_sieciowego or '',
            urzadzenie.notatki or ''
        ])

    return response


# Funkcja generująca plik csv dla Zgłoszenia
def export_zgloszenie_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    # Generowanie nazw pliku z aktualną datą i czasem
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'zgloszenia_{now}.csv'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Tworzenie nagłówków kolumn
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'EZD ID Koszulki', 'Nr Zgłoszenia', 'Nr EZD', 'Data Zgłoszenia', 'Nazwa Zakładu', 'Laboratorium',
        'Zgłaszający', 'Telefon', 'Nr Pomieszczenia', 'Nazwa Urządzenia', 'Dostęp do Sieci', 'Nr Ewidencyjny',
        'Nr Gniazdka LAN', 'Opis Zgłoszenia', 'Oczekiwania', 'Istotność Poufności', 'Istotność Integralności',
        'Istotność Dostępności', 'Zgłaszający Podpis', 'Kierownik LIM Opinia', 'Kierownik LIM Podpis',
        'Kierownik LIM Data', 'Kierownik KM Opinia', 'Kierownik KM Podpis', 'Kierownik KM Data',
        'Realizacja Opis', 'Realizacja Podpis', 'Realizacja Data', 'Potwierdzenie Podpis', 'Potwierdzenie Data',
        'PIM ID Urządzenia', 'Notatki'
    ])

    zgloszenia = Zgloszenie.objects.all()
    for zgloszenie in zgloszenia:
        urzadzenie_id = zgloszenie.urzadzenie_id.pim_id if zgloszenie.urzadzenie_id else ''

        # Zapisywanie danych każdego zgłoszenia w pliku CSV
        writer.writerow([
            zgloszenie.id,
            zgloszenie.nr_EZD_ID_koszulki or '',
            zgloszenie.nr_zgloszenia or '',
            zgloszenie.nr_EZD or '',
            zgloszenie.data_zgloszenia or '',
            zgloszenie.nazwa_zakladu or '',
            zgloszenie.laboratorium or '',
            zgloszenie.zglaszajacy or '',
            zgloszenie.telefon or '',
            zgloszenie.nr_pomieszczenia or '',
            zgloszenie.nazwa_urzadzenia or '',
            zgloszenie.dostep_do_sieci or '',
            zgloszenie.nr_ewidencyjny or '',
            zgloszenie.nr_gniazdka_lan or '',
            zgloszenie.opis_zgloszenia or '',
            zgloszenie.oczekiwania or '',
            zgloszenie.istotnosc_pouf or '',
            zgloszenie.istotnosc_integr or '',
            zgloszenie.istotnosc_dost or '',
            zgloszenie.zglaszajacy_podpis or '',
            zgloszenie.kierownik_lim_opinia or '',
            zgloszenie.kierownik_lim_podpis or '',
            zgloszenie.kierownik_lim_data or '',
            zgloszenie.kierownik_km_opinia or '',
            zgloszenie.kierownik_km_podpis or '',
            zgloszenie.kierownik_km_data or '',
            zgloszenie.realizacja_opis or '',
            zgloszenie.realizacja_podpis or '',
            zgloszenie.realizacja_data or '',
            zgloszenie.potwierdzenie_podpis or '',
            zgloszenie.potwierdzenie_data or '',
            urzadzenie_id,
            zgloszenie.notatki or ''
        ])

    return response


# Funkcja generująca plik csv dla Systemu operacyjnego
def export_system_operacyjny_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')

    # Generowanie nazw pliku z aktualną datą i czasem
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'systemy_operacyjne_{now}.csv'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Tworzenie nagłówków do pliku CSV
    writer = csv.writer(response)
    writer.writerow([
        'Typ Systemu Operacyjnego'
    ])

    # Pobieranie wszystkich Systemy operacyjne i zapisuje je do CSV
    systemy_operacyjne = SystemOperacyjny.objects.all()
    for system_operacyjny in systemy_operacyjne:
        writer.writerow([
            system_operacyjny.typ_system_operacyjny
        ])

    return response


# Funkcja generująca dokument .docx.
# WYMAGA SZABLONU W ODPOWIEDNIM MIEJSCU
def generate_docx(modeladmin, request, queryset):
    # przekształcenie danych w format odpowiedni do wydruku
    ids = [obj.id for obj in queryset]
    # pobranie danych z bazy danych
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM bazadanych_zgloszenie WHERE id IN ({','.join(map(str, ids))})")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)
    buffer = BytesIO()
    # zapisywanie danych z bazy danych do odpowiednich komórek pliku formatki
    for index, row in df.iterrows():
        # TA FORMATKA MUSI BYĆ WE WSKAZANEJ LOKALIZACJI Z WSKAZANĄ NAZWĄ!!!
        # KAŻDA ZMIANA FORMATKI BĘDZIE SKUTKOWAŁA ZMIANĄ PONIŻSZEGO KODU!
        # Poniższa wersja działa tylko dla tej konkretnej wersji
        document = Document("bazadanych/Zgloszenie_szablon.docx")
        table1 = document.tables[0]
        table2 = document.tables[1]
        # Wpisywanie danych do pierwszej tabeli formatki (nagłówka)
        table1.cell(0, 3).paragraphs[0].text = row['nr_zgloszenia'] or ""
        table1.cell(0, 3).add_paragraph().alignment = WD_ALIGN_PARAGRAPH.CENTER
        table1.cell(0, 3).paragraphs[1].text = row['nr_EZD'] or ""
        # Wpisywanie dat wymaga zastosowania takiego stwierdzenia "if",
        # by uniknąć wstawienia "0" zamiast pustego miejsca przy braku podanej daty
        if str(row['data_zgloszenia']) == "None":
            table1.cell(1, 3).paragraphs[-1].text = ""
        else:
            table1.cell(1, 3).paragraphs[-1].text = str(row['data_zgloszenia'])
        # Wpisywanie danych do pól pomiędzy tabelami
        document.paragraphs[2].add_run(row['nazwa_zakladu'] or "")
        document.paragraphs[3].add_run(row['laboratorium'] or "")
        document.paragraphs[4].add_run(row['zglaszajacy'] or "")
        document.paragraphs[5].add_run(row['telefon'] or "")
        document.paragraphs[6].add_run(row['nr_pomieszczenia'] or "")

        # Wpisywanie danych do drugiej tabeli w formatce
        table2.cell(0, 0).paragraphs[-1].add_run(row['nazwa_urzadzenia'] or "")
        table2.cell(1, 0).paragraphs[-1].add_run(row['dostep_do_sieci'] or "")
        table2.cell(2, 0).paragraphs[-1].add_run(row['nr_ewidencyjny'] or "")
        table2.cell(2, 2).paragraphs[-1].add_run(row['nr_gniazdka_lan'] or "")
        table2.cell(3, 0).paragraphs[-1].add_run(row['opis_zgloszenia'] or "")
        table2.cell(4, 0).paragraphs[-1].add_run(row['oczekiwania'] or "")
        table2.cell(5, 3).text = row['istotnosc_pouf'] or ""
        table2.cell(6, 3).text = row['istotnosc_integr'] or ""
        table2.cell(7, 3).text = row['istotnosc_dost'] or ""
        table2.cell(9, 0).paragraphs[0].text = row['zglaszajacy_podpis'] or ""
        table2.cell(10, 0).paragraphs[1].add_run(row['kierownik_lim_opinia'] or "")
        table2.cell(11, 0).paragraphs[0].text = row['kierownik_lim_podpis'] or ""
        if str(row['kierownik_lim_data']) == "None":
            table2.cell(11, 0).paragraphs[2].text = ""
        else:
            table2.cell(11, 0).paragraphs[2].text = str(row['kierownik_lim_data'])

        table2.cell(12, 0).paragraphs[1].add_run(row['kierownik_km_opinia'] or "")
        table2.cell(13, 0).paragraphs[0].add_run(row['kierownik_km_podpis'] or "")
        if str(row['kierownik_km_data']) == "None":
            table2.cell(13, 0).paragraphs[-1].text = ""
        else:
            table2.cell(13, 0).paragraphs[-1].text = str(row['kierownik_km_data'])
        table2.cell(14, 0).paragraphs[1].add_run(row['realizacja_opis'] or "")
        table2.cell(15, 0).paragraphs[0].text = row['realizacja_podpis'] or ""
        if str(row['realizacja_data']) == "None":
            table2.cell(15, 0).paragraphs[-1].text = ""
        else:
            table2.cell(15, 0).paragraphs[-1].text = str(row['realizacja_data'])

        table2.cell(16, 0).paragraphs[2].add_run(row['potwierdzenie_podpis'] or "")
        if str(row['potwierdzenie_data']) == "None":
            table2.cell(16, 0).paragraphs[-1].text = ""
        else:
            table2.cell(16, 0).paragraphs[-1].text = str(row['potwierdzenie_data'])

        # Przygotowanie nazwy pliku (usuwanie z niej znaków zabronionych i dodanie odpowiedniego sufixa)
        prefix = (row['nr_zgloszenia'] or "Wybierz-kolego-numer-zgloszenia-nastepnym-razem-czy-cos").replace(".", "n").replace("/", "n")
        filename = f"{prefix}-F1-IP003-A-IT Zgloszenie-pomocy-technicznej-systemow-informatyki-metrologicznej-(SIM).docx"
        cleaned_name = re.sub(r'[\\/*?:"<>|]', "", filename)
        # Zapisanie pliku
        document.save(buffer)
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={cleaned_name}'

        return response