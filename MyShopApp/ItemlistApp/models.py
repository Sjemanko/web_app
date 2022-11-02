from django.db import models


# Create your models here.


class ClothItem(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    clothItem = models.ForeignKey(ClothItem, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
