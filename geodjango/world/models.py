from django.db import models

# Create your models here.

from django.contrib.gis.db import models
from djgeojson.fields import PolygonField

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class FeedingAreas(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    geom = models.PolygonField()

    def __unicode__(self):
        return self.title

class aisdata(models.Model):
    vesseltype = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    speed = models.IntegerField()
    course = models.IntegerField()
    heading = models.IntegerField()
    timestamp = models.DateTimeField()
    geom = models.PointField()

