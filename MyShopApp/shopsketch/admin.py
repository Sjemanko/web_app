from django.contrib import admin
from .models import Product, ShoppingCart


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'product_gender',
        'product_sizes'
    ]

class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cart_name'
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
