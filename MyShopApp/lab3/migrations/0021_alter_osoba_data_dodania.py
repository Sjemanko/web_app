# Generated by Django 4.1.3 on 2022-11-02 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0020_alter_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
