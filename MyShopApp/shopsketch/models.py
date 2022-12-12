from django.db import models
from django.contrib.auth.models import User
# from django.db.models import pre_save, post_save
# from django.dispatch import receiver
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
    product_price = models.FloatField(
        default=0
    )

    def __str__(self):
        return f'{self.product_name} {self.product_gender}'

    class Meta:
        ordering = ['id']
 
class ShoppingCart(models.Model):
    owner = models.ForeignKey('auth.User', null='true', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner.username} {self.id}'



class OrderedItems(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.shopping_cart.owner.username} {self.product.product_name}'




    
