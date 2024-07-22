# Generated by Django 5.0.7 on 2024-07-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_formdata_dostep_do_sieci_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='dostep_do_sieci',
            field=models.CharField(blank=True, choices=[('dodanie uprawnień', 'dodanie uprawnień'), ('dodanie dostępu', 'dodanie dostępu'), ('dodanie terminala', 'dodanie terminala'), ('dodanie konta', 'dodanie konta'), ('dodanie systemu', 'dodanie systemu'), ('usunięcie uprawnień', 'usunięcie uprawnień'), ('usunięcie dostępu', 'usunięcie dostępu'), ('usunięcie terminala', 'usunięcie terminala'), ('usunięcie konta', 'usunięcie konta'), ('usunięcie systemu', 'usunięcie systemu'), ('nadanie uprawnień', 'nadanie uprawnień'), ('nadanie dostępu', 'nadanie dostępu'), ('nadanie terminala', 'nadanie terminala'), ('nadanie konta', 'nadanie konta'), ('nadanie systemu', 'nadanie systemu'), ('odebranie uprawnień', 'odebranie uprawnień'), ('odebranie dostępu', 'odebranie dostępu'), ('odebranie terminala', 'odebranie terminala'), ('odebranie konta', 'odebranie konta'), ('odebranie systemu', 'odebranie systemu')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='laboratorium',
            field=models.CharField(blank=True, choices=[('green', 'green'), ('red', 'red')], max_length=200, null=True),
        ),
    ]
