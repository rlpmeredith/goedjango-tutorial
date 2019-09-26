from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core.serializers import serialize
from .models import WorldBorder, FeedingAreas
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'world/index.html'

def borders_view(request):
    WorldBorders_as_geojson = serialize('geojson', WorldBorder.objects.all())
    return HttpResponse(WorldBorders_as_geojson, content_type='json')

def feeding_areas(request):
    FeedingAreas_as_geojson = serialize('geojson', FeedingAreas.objects.all())
    return HttpResponse(FeedingAreas_as_geojson, content_type='json')
