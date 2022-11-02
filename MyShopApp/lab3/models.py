from django.db import models
from datetime import date


# Create your models here.

class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    wybor_miesiaca = (
        ('1', 'Styczeń'),
        ('2', 'Luty'),
        ('3', 'Marzec'),
        ('4', 'Kwiecień'),
        ('5', 'Maj'),
        ('6', 'Czerwiec'),
        ('7', 'Lipiec'),
        ('8', 'Sierpień'),
        ('9', 'Wrzesień'),
        ('10', 'Październik'),
        ('11', 'Listopad'),
        ('12', 'Grudzień')
    )
    miesiac_urodzenia = models.CharField(blank=True, choices=wybor_miesiaca, max_length=20, default=4)
    data_dodania = models.DateField(default=date.today())
