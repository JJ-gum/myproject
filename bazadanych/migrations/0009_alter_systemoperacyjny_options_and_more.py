# Generated by Django 5.0.7 on 2024-07-31 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazadanych', '0008_rename_os_type_systemoperacyjny_typ_system_operacyjny'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemoperacyjny',
            options={'verbose_name': 'System operacyjny', 'verbose_name_plural': 'Systemy operacyjne'},
        ),
        migrations.AlterModelOptions(
            name='urzadzenie',
            options={'verbose_name': 'Urządzenie', 'verbose_name_plural': 'Urządzenia'},
        ),
        migrations.AlterModelOptions(
            name='zgloszenie',
            options={'verbose_name': 'Zgłoszenie', 'verbose_name_plural': 'Zgłoszenia'},
        ),
    ]