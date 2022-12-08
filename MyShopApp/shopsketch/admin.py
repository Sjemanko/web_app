from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'product_gender',
        'product_sizes'
    ]

admin.site.register(Product, ProductAdmin)

