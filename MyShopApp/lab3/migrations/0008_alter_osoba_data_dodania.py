# Generated by Django 4.1.3 on 2022-11-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0007_alter_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]