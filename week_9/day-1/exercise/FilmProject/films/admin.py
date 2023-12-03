from django.contrib import admin
from .models import Film, Director, Country, Category

admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Country)
admin.site.register(Category)
