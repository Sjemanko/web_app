# Generated by Django 4.1.3 on 2022-11-06 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Druzyna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('kraj', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('miesiac_urodzenia', models.IntegerField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecien'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'), (11, 'Listopad'), (12, 'Grudzien')])),
                ('miesiac_dodania', models.DateField(default=11)),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
                ('druzyna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab5.druzyna')),
            ],
            options={
                'ordering': ['nazwisko'],
            },
        ),
    ]
