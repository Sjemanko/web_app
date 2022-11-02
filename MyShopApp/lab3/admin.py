from django.contrib import admin
from .models import Osoba


# Register your models here.

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania']


admin.site.register(Osoba)
