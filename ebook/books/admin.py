from django.contrib import admin
from .models import Books

class Booksadmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Books, Booksadmin)