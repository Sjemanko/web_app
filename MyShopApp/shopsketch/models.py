from django.db import models

# Create your models here.


class Product(models.Model):
    GENDER = [
        ('ME', 'Male'),
        ('FE', 'Female')
    ]

    CATEGORIES = [
        ('JACKETS', 'Jackets'),
        ('TSHIRTS', 'T-Shirts'),
        ('HOODIES', 'Hoodies')
    ]

    SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    ]

    product_name = models.CharField(
        max_length=100
    )
    product_gender = models.CharField(
        max_length = 2,
        choices = GENDER,
        default = GENDER[0]
    )
    product_category = models.CharField(
        max_length = 20,
        choices = CATEGORIES
    )
    product_sizes = models.CharField(
        max_length = 2,
        choices = SIZES
    )

    def __str__(self):
        return f'{self.product_name} {self.product_gender}'

    class Meta:
        ordering = ['id']