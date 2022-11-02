from django.contrib import admin
from .models import Osoba, Druzyna


# Register your models here.

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['id', 'druzyna', 'nazwisko', 'imie', 'miesiac_urodzenia', 'data_dodania']
    list_filter = ['druzyna']


class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']
    list_filter = ['kraj']


admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Druzyna, DruzynaAdmin)
