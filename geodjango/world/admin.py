from django.contrib import admin

# Register your models here.

from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis import admin

from .models import WorldBorder
from .models import FeedingAreas
from .models import aisdata

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(aisdata, admin.GeoModelAdmin)
admin.site.register(FeedingAreas, LeafletGeoAdmin)



