from django.contrib import admin
from .models import Farmer, Field, Culture, Season
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Farmer)


class FieldInfo(LeafletGeoAdmin):
    pass


admin.site.register(Field, FieldInfo)
admin.site.register(Season)
admin.site.register(Culture)

# class InfoAdmin(LeafletGeoAdmin):
#     pass
    # list_display = ('name', 'location')


# admin.site.register(Incidences, InfoAdmin)

