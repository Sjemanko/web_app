from django.contrib import admin
from .models import Product, ShoppingCart, OrderedItems

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'product_gender',
        'product_sizes',
    ]

class OrderedItemsAdmin(admin.ModelAdmin):
    list_display = [
        'shopping_cart',
        'product',
        'quantity',
    ]

class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'owner',
        'total_price'
    ]



admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(OrderedItems, OrderedItemsAdmin)