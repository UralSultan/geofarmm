from django.contrib import admin
from .models import Farmer, Field, Culture, Season
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Farmer)


class FieldInfo(LeafletGeoAdmin):
    pass


# class FieldAdmin(admin.ModelAdmin):
#     list_display = ('plot', 'farmer', 'culture')
#     list_display_links = ('plot', 'farmer', 'culture')
#     search_fields = ('farmer', 'culture')
#


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
    list_filter = [
        'farmer__name',
        'culture__name',
    ]


# admin.site.register(Field, FieldAdmin)

admin.site.register(Season)

admin.site.register(Culture)


# class InfoAdmin(LeafletGeoAdmin):
#     pass
    # list_display = ('name', 'location')


# admin.site.register(Incidences, InfoAdmin)

