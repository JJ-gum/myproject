from django.db import models

# Lista dostępnych opcji przy wyborze połączenia sieciowego
# Dotyczy Urządzenia
TERMINAL_CHOICES = (
    ('Office', 'Office'),
    ('OT', 'OT'),
    ('Odizolowane', 'Odizolowane'),
    ('Brak', 'Brak')
)

# Lista dostępnych opcji przy wyborze typu urządzenia
# Dotyczy Urządzenia
DEVICE_CHOICES = (
    ('PC', 'PC'),
    ('Laptop', 'Laptop'),
    ('Monitor', 'Monitor'),
    ('Klimatyzator', 'Klimatyzator'),
    ('Inne', 'Inne')
)

# Lista dostępnych opcji przy wyborze zakładu GUM
# Dotyczy Zgłoszenia
ZAKLAD_CHOICES = [
    ('Zakład Badań Certyfikacyjnych (Z1)', 'Zakład Badań Certyfikacyjnych (Z1)'),
    ('Zakład Chemii Fizycznej i Środowiska (Z2)', 'Zakład Chemii Fizycznej i Środowiska (Z2)'),
    ('Zakład Czasu i Długości (Z3)', 'Zakład Czasu i Długości (Z3)'),
    ('Zakład Elektryczności i Promieniowania (Z4)', 'Zakład Elektryczności i Promieniowania (Z4)'),
    ('Zakład Mechaniki i Akustyki (Z5)', 'Zakład Mechaniki i Akustyki (Z5)'),
    ('Zakład Technologii Cyfrowych (Z6)', 'Zakład Technologii Cyfrowych (Z6)')
]

# Lista dostępnych opcji przy wyborze laboratorium GUM
# Dotyczy Zgłoszenia
LABORATORIUM_CHOICES = [
    ('Laboratorium Bezpieczeństwa Ruchu Drogowego (Z11)', 'Laboratorium Bezpieczeństwa Ruchu Drogowego (Z11)'),
    ('Laboratorium Badań Oprogramowania (Z12)', 'Laboratorium Badań Oprogramowania (Z12)'),
    ('Laboratorium Temperatury (Z21)', 'Laboratorium Temperatury (Z21)'),
    ('Laboratorium Wilgotności (Z22)', 'Laboratorium Wilgotności (Z22)'),
    ('Laboratorium Analizy Gazów (Z23)', 'Laboratorium Analizy Gazów (Z23)'),
    ('Laboratorium Analiz Elektrochemicznych i Nieorganicznych (Z24)', 'Laboratorium Analiz Elektrochemicznych i Nieorganicznych (Z24)'),
    ('Laboratorium Wzorców Fizykochemicznych (Z25)', 'Laboratorium Wzorców Fizykochemicznych (Z25)'),
    ('Laboratorium Czasu i Częstotliwości (Z31)', 'Laboratorium Czasu i Częstotliwości (Z31)'),
    ('Laboratorium Długości (Z32)', 'Laboratorium Długości (Z32)'),
    ('Laboratorium Precyzyjnych Pomiarów Geometrycznych (Z33)', 'Laboratorium Precyzyjnych Pomiarów Geometrycznych (Z33)'),
    ('Laboratorium Twardości (Z34)', 'Laboratorium Twardości (Z34)'),
    ('Laboratorium Nowych Technologii Czasu i Długości (Z35)', 'Laboratorium Nowych Technologii Czasu i Długości (Z35)'),
    ('Laboratorium Wzorców Wielkości Elektrycznych DC (Z41)', 'Laboratorium Wzorców Wielkości Elektrycznych DC (Z41)'),
    ('Laboratorium Wzorców Wielkości Elektrycznych Małej Częstotliwości (Z42)', 'Laboratorium Wzorców Wielkości Elektrycznych Małej Częstotliwości (Z42)'),
    ('Laboratorium Pomiarów Elektroenergetycznych (Z43)', 'Laboratorium Pomiarów Elektroenergetycznych (Z43)'),
    ('Laboratorium Mikrofal, Pola Elektromagnetycznego i Kompatybilności Elektromagnetycznej (Z44)', 'Laboratorium Mikrofal, Pola Elektromagnetycznego i Kompatybilności Elektromagnetycznej (Z44)'),
    ('Laboratorium Wzorców Spektrofotometrycznych (Z45)', 'Laboratorium Wzorców Spektrofotometrycznych (Z45)'),
    ('Laboratorium Wzorców Fotometrycznych i Radiometrycznych (Z46)', 'Laboratorium Wzorców Fotometrycznych i Radiometrycznych (Z46)'),
    ('Wieloosobowe Stanowisko Pracy do spraw Wzorców Barwy (Z47)', 'Wieloosobowe Stanowisko Pracy do spraw Wzorców Barwy (Z47)'),
    ('Laboratorium Promieniowania Jonizującego (Z48)', 'Laboratorium Promieniowania Jonizującego (Z48)'),
    ('Laboratorium Masy (Z51)', 'Laboratorium Masy (Z51)'),
    ('Laboratorium Przepływów (Z53)', 'Laboratorium Przepływów (Z53)'),
    ('Laboratorium Akustyki (Z55)', 'Laboratorium Akustyki (Z55)'),
    ('Laboratorium Drgań Mechanicznych (Z56)', 'Laboratorium Drgań Mechanicznych (Z56)'),
    ('Wieloosobowe Stanowisko Pracy ds. Ultradźwięków i Akustyki Podwodnej (Z57)', 'Wieloosobowe Stanowisko Pracy ds. Ultradźwięków i Akustyki Podwodnej (Z57)'),
    ('Laboratorium Siły i Momentu Siły (Z58)', 'Laboratorium Siły i Momentu Siły (Z58)'),
    ('Laboratorium Ciśnienia (Z59)', 'Laboratorium Ciśnienia (Z59)'),
    ('Laboratorium Informatyki Metrologicznej (Z61)', 'Laboratorium Informatyki Metrologicznej (Z61)'),
    ('Laboratorium Sztucznej Inteligencji (Z62)', 'Laboratorium Sztucznej Inteligencji (Z62)')
]

# Lista dostępnych opcji przy wyborze opcji dostępu do sieci
# Dotyczy Zgłoszenia
DOSTEP_DO_SIECI_CHOICES = [
    ('dodanie uprawnień', 'dodanie uprawnień'),
    ('dodanie dostępu', 'dodanie dostępu'),
    ('dodanie terminala', 'dodanie terminala'),
    ('dodanie konta', 'dodanie konta'),
    ('dodanie systemu', 'dodanie systemu'),
    ('usunięcie uprawnień', 'usunięcie uprawnień'),
    ('usunięcie dostępu', 'usunięcie dostępu'),
    ('usunięcie terminala', 'usunięcie terminala'),
    ('usunięcie konta', 'usunięcie konta'),
    ('usunięcie systemu', 'usunięcie systemu'),
    ('nadanie uprawnień', 'nadanie uprawnień'),
    ('nadanie dostępu', 'nadanie dostępu'),
    ('nadanie terminala', 'nadanie terminala'),
    ('nadanie konta', 'nadanie konta'),
    ('nadanie systemu', 'nadanie systemu'),
    ('odebranie uprawnień', 'odebranie uprawnień'),
    ('odebranie dostępu', 'odebranie dostępu'),
    ('odebranie terminala', 'odebranie terminala'),
    ('odebranie konta', 'odebranie konta'),
    ('odebranie systemu', 'odebranie systemu')
]

# Lista dostępnych opcji przy wyborach istotności problemu
# Dotyczy Zgłoszenia
ISTOTNOSC_CHOICES = [
    ('Bardzo mała', 'Bardzo mała'),
    ('Mała', 'Mała'),
    ('Średnia', 'Średnia'),
    ('Duża', 'Duża'),
    ('Krytyczna', 'Krytyczna')
]


# Klasa odpowiadająca za zapisanie systemu operacyjnego w bazie danych
class SystemOperacyjny(models.Model):
    typ_system_operacyjny = models.CharField(db_column="Operating System", primary_key=True, max_length=120)

    def __str__(self):
        return self.typ_system_operacyjny


# Klasa odpowiadająca za zapisanie informacji o urządzeniu w bazie danych
class Urzadzenie(models.Model):
    # ID — odpowiada za szeregowanie urządzeń w bazie danych, jest głównym kluczem
    pim_id = models.AutoField(db_column="PIM ID", primary_key=True)
    # Laboratorium, do którego należy dane urządzenie
    laboratorium = models.CharField(db_column="Lab Name", max_length=200, blank=True, null=True)
    # Nr pomieszczenia, w którym znajduje się urządzenie
    nr_pomieszczenia = models.CharField(db_column="Room number", max_length=40, blank=True, null=True)
    # Opis urządzenia odpowiadający za przedstawienie informacji na jego temat, niemających własnej rubryki
    opis = models.TextField(db_column="Terminal Description", blank=True, null=True)
    # Nr ewidencyjny służący do katalogowania urządzeń
    numer_ewidencyjny = models.CharField(db_column="Inventory Number", max_length=40, blank=True, null=True)
    # Typ urządzenia do wybrania z opcji dostępnych w DEVICE_CHOICES
    typ_urzadzenia = models.CharField(db_column="Device Type", max_length=40, choices=DEVICE_CHOICES, blank=True, null=True)
    # System operacyjny przechowywany w tabeli "Operating System" w bazie danych
    system_operacyjny = models.ManyToManyField(SystemOperacyjny, db_column="Operating System", blank=True)
    # CPU — każdy wie co to
    cpu = models.CharField(db_column="CPU", max_length=40, blank=True, null=True)
    # RAM — każdy wie co to
    ram = models.CharField(db_column="RAM", max_length=40, blank=True, null=True)
    # Ilość zainstalowanej pamięci dyskowej
    pamiec_dysku = models.CharField(db_column="Drive Memory", max_length=40, blank=True, null=True)
    # Dodatkowe komponenty niewymienione wyżej, a znajdujące się w urządzeniu
    dodatkowe_komponenty = models.TextField(db_column="Additional Components", blank=True, null=True)
    # Specjalistyczne oprogramowanie zainstalowane na komputerze
    oprogramowanie_specjalne = models.TextField(db_column="Specialized Software", blank=True, null=True)
    # Konta użytkownika dostępne na urządzeniu
    konta = models.TextField(db_column="Accounts", blank=True, null=True)
    # Data rejestracji urządzenia w systemie
    data_rejestracji = models.DateField(db_column="Date of Registry", null=True)
    # Nr gniazda LAN
    nr_gniazda = models.CharField(db_column="Socket Number", max_length=40, blank=True, null=True)
    # Rodzaj gniazda LAN
    typ_gniazd = models.CharField(db_column="Socket Type", max_length=120, blank=True, null=True)
    # Opiekun odpowiadający za dane urządzenie
    opiekun_1 = models.CharField(db_column="Supervisor 1", max_length=40, null=True)
    # Opiekun odpowiadający za dane urządzenie
    opiekun_2 = models.CharField(db_column="Supervisor 2", max_length=40, blank=True, null=True)
    # Typ podłączenia urządzenia do wybrania z opcji dostępnych w TERMINAL_CHOICES
    typ_polaczenia_sieciowego = models.CharField(db_column="Terminal Connection Type", max_length=40, choices=TERMINAL_CHOICES, blank=True, null=True)
    notatki = models.TextField(blank=True, null=True)

    # Wywołanie tej klasy zwraca string składający się z nazwy laboratorium, nr pomieszczenia, typu urządzenia i ID
    def __str__(self):
        return f"{self.laboratorium} - {self.nr_pomieszczenia} - {self.typ_urzadzenia} - {self.pim_id}"


class Zgloszenie(models.Model):
    id = models.AutoField(primary_key=True)
    nr_EZD_ID_koszulki = models.CharField(max_length=100, blank=True, null=True)
    nr_zgloszenia = models.CharField(max_length=100, blank=True, null=True)
    nr_EZD = models.CharField(max_length=100, blank=True, null=True)
    data_zgloszenia = models.DateField(blank=True, null=True)
    nazwa_zakladu = models.CharField(max_length=200, blank=True, null=True, choices=ZAKLAD_CHOICES)
    laboratorium = models.CharField(max_length=200, blank=True, null=True, choices=LABORATORIUM_CHOICES)
    zglaszajacy = models.CharField(max_length=200, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    nr_pomieszczenia = models.CharField(max_length=100, blank=True, null=True)
    nazwa_urzadzenia = models.CharField(max_length=200, blank=True, null=True)
    dostep_do_sieci = models.CharField(max_length=100, blank=True, null=True, choices=DOSTEP_DO_SIECI_CHOICES)
    nr_ewidencyjny = models.CharField(max_length=100, blank=True, null=True)
    nr_gniazdka_lan = models.CharField(max_length=100, blank=True, null=True)
    opis_zgloszenia = models.TextField(blank=True, null=True)
    oczekiwania = models.TextField(blank=True, null=True)
    istotnosc_pouf = models.CharField(max_length=100, blank=True, null=True, choices=ISTOTNOSC_CHOICES)
    istotnosc_integr = models.CharField(max_length=100, blank=True, null=True, choices=ISTOTNOSC_CHOICES)
    istotnosc_dost = models.CharField(max_length=100, blank=True, null=True, choices=ISTOTNOSC_CHOICES)
    zglaszajacy_podpis = models.CharField(max_length=200, blank=True, null=True)
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
    urzadzenie_id = models.ForeignKey(Urzadzenie, db_column="PIM ID", on_delete=models.CASCADE, blank=True, null=True)
    notatki = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nr_zgloszenia if self.nr_zgloszenia else 'No ID'
