from django.contrib import admin
from .models import Incidences
from leaflet.admin import LeafletGeoAdmin


class IncidencesAmin(LeafletGeoAdmin):
    pass
    # list_display = ('name', 'location')


admin.site.register(Incidences, IncidencesAmin)

