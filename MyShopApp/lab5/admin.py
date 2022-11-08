from django.contrib import admin
from .models import Person, Team


# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'month_birth', 'created_at']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']


admin.site.register(Person, PersonAdmin)
admin.site.register(Team, TeamAdmin)

