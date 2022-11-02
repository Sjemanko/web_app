from django.db import models
from django.utils import timezone


# Create your models here.

class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    class WyborMiesiaca(models.IntegerChoices):
        STYCZEN = 1
        LUTY = 2
        MARZEC = 3
        KWIECIEN = 4
        MAJ = 5
        CZERWIEC = 6
        LIPIEC = 7
        SIERPIEN = 8
        WRZESIEN = 9
        PAZDZIERNIK = 10
        LISTOPAD = 11
        GRUDZIEN = 12

    # wybor_miesiaca = (
    #     ('1', 'Styczeń'),
    #     ('2', 'Luty'),
    #     ('3', 'Marzec'),
    #     ('4', 'Kwiecień'),
    #     ('5', 'Maj'),
    #     ('6', 'Czerwiec'),
    #     ('7', 'Lipiec'),
    #     ('8', 'Sierpień'),
    #     ('9', 'Wrzesień'),
    #     ('10', 'Październik'),
    #     ('11', 'Listopad'),
    #     ('12', 'Grudzień')
    # )
    miesiac_urodzenia = models.IntegerField(choices=WyborMiesiaca.choices)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
