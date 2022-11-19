from django.contrib import admin

# Register your models here.

from .models import Photo, Category, Team, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Photo)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'image', 'description']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
