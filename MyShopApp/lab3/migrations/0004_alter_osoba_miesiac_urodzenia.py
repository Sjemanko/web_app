# Generated by Django 4.1.3 on 2022-11-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0003_alter_osoba_miesiac_urodzenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='miesiac_urodzenia',
            field=models.CharField(blank=True, choices=[('1', 'Styczeń'), ('2', 'Luty'), ('3', 'Marzec'), ('4', 'Kwiecień'), ('5', 'Maj'), ('6', 'Czerwiec'), ('7', 'Lipiec'), ('8', 'Sierpień'), ('9', 'Wrzesień'), ('10', 'Październik'), ('11', 'Listopad'), ('12', 'Grudzień')], default=4, max_length=20),
        ),
    ]
