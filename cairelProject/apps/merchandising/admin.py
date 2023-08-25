from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class RolAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category']
