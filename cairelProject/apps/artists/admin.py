from django.contrib import admin
from .models import Rol, Person

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'rol']
