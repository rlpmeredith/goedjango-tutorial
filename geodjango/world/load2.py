import os
from django.contrib.gis.utils import LayerMapping
from .models import aisdata

aisdata_mapping = {
    'vesseltype': 'VESSEL TYPE',
    'status': 'STATUS',
    'speed': 'SPEED (KNOTSx10)',
    'course': 'COURSE',
    'heading': 'HEADING',
    'timestamp': 'TIMESTAMP UTC',
    'geom': 'POINT',
}

aiscsv = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'convertcsv.geojson'),
)

def run(verbose=True):
    lm = LayerMapping(aisdata, aiscsv, aisdata_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
