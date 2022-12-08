from django.contrib import admin
from .models import Product, ShoppingCart, Order


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
        'owner'
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_id',
        'shopping_cart_id'
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Order, OrderAdmin)