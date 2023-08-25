from django.contrib import admin
from .models import Album, Song

@admin.register(Album)
class RolAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Song)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'album']