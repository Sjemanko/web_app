# Generated by Django 4.1.3 on 2022-11-02 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0009_alter_osoba_data_dodania_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=datetime.date(2022, 11, 2)),
        ),
    ]