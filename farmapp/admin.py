from django.contrib import admin
from .models import Farmer, Field, Culture, Season

admin.site.register(Farmer)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'plot',
        'farmer',
        'culture',
        'seasons',
    ]
    list_display = [
        'plot',
        'farmer',
        'culture',
        'seasons',
    ]
    search_fields = [
        'farmer__name',
        'culture__name',
    ]
    list_filter = (
        'farmer__name',
        'culture__name',
    )




admin.site.register(Season)

admin.site.register(Culture)

