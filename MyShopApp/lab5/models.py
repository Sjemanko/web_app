from django.db import models
import datetime


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name} ({self.country})'


class MonthBirth(models.IntegerChoices):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Person(models.Model):
    owner = models.ForeignKey("auth.User", null='true', related_name=("Person"), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    month_birth = models.IntegerField(choices=MonthBirth.choices)
    created_at_month = models.IntegerField(default=datetime.date.today().month)
    created_at = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ["last_name"]
