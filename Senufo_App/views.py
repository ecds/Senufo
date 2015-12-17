import os
import re
import collections
from urllib import urlencode
import logging
import tempfile, zipfile
from django.core.servers.basehttp import FileWrapper
import mimetypes

from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext


import csv
from django.shortcuts import render
from django.http import HttpResponse
from djqscsv import render_to_csv_response
from Senufo_App.models import Object_Records, Images, Artists_Creators, Places, Objects_Places_Reason

#def object_location(request):
 #   response = HttpResponse(content_type='text/csv')
  #  response['Content-Disposition'] = 'attachment; filename="Object_Locations.csv"'
   # writer = csv.writer(response)
 #   writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
  #  writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

   # return response
from itertools import chain
from operator import attrgetter

def object_location(request):
    ObjectVariables = Object_Records.objects.only('Object_id', 'Object_Name', 'Object_Type', 'Object_Description', 'Artist__Artist_Name', 'ArtistAttributionCertainty', 'Essay', 'ResearchNotes1', 'ResearchNotes2').order_by('Object_id')
    PlaceVariables = Places.objects.only('id', 'Place_Name', 'Latitude', 'Longitude', 'NGA_Place', 'NGA_Region', 'NGA_Country', 'Map_Place', 'Map_Country').all()
    PlaceLocations = Objects_Places_Reason.objects.only('id', 'Object_Name', 'Place_Name').all()
#    AllVariables = chain(ObjectVariables, PlaceVariables, PlaceLocations)
    return render_to_csv_response(ObjectVariables)

def object_place(request):
    ObjectVariables = Object_Records.objects.only('Object_id', 'Object_Name', 'Object_Type', 'Object_Description', 'Artist', 'ArtistAttributionCertainty', 'Essay', 'ResearchNotes1', 'ResearchNotes2').order_by('Object_id')
    PlaceVariables = Places.objects.only('Places_id', 'Place_Name', 'Latitude', 'Longitude', 'NGA_Place', 'NGA_Region', 'NGA_Country', 'Map_Place', 'Map_Country').all()
    PlaceLocations = Objects_Places_Reason.objects.only('Reason_id', 'Objects_Name', 'Places_Name').all()
 #   if Objects_Places_Reason.Object_Name.id == Objects_Records.id and Objects_Places_Reason.Place_Name.id == Places.id:
  #      return Object_Records.Object_Name, Object_Records.Object_Type, Object_Records.Artist, Places.Place_Name, Places.Latitude, Places.Longitude as VariableTrying  
    return render_to_response('export.html', {'ObjectVariables':ObjectVariables, 'PlaceVariables':PlaceVariables, 'PlaceLocations':PlaceLocations}, context_instance=RequestContext(request))


def objectplace_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ObjectLocations_forMap.csv"'
    DictWriter.writeheader('Object_Name', 'Object_Type', 'Object_Description', 'Artist', 'ArtistAttributionCertainty', 'Place_Name', 'Latitude', 'Longitude','Map_Place', 'Map_Country'),
    csvwriter.writerow(    ()
    )



#def object_location(request):
#    ObjectVariables = Object_Records.objects.only('id', 'Object_Name', 'Object_Type', 'Object_Description', 'Artist', 'ArtistAttributionCertainty', 'Essay', 'ResearchNotes1', 'ResearchNotes2').order_by('id')
#    PlaceVariables = Places.objects.only('id', 'Place_Name', 'Latitude', 'Longitude', 'NGA_Place', 'NGA_Region', 'NGA_Country', 'Map_Place', 'Map_Country').all()
#    PlaceLocations = Objects_Places_Reason.objects.only('id', 'Object_Name', 'Place_Name').all()
#    for PlaceLocation in PlaceLocations:
#    for PlaceVariable in PlaceVariables:
#    for ObjectVariable in ObjectVariables:
#        if PlaceLocation.Object_Name.id == ObjectVariable.id and PlaceLocation.Place_Name.id == PlaceVariable.id:
#            Places_List.append(PlaceLocation)
#    return render_to_csv_response(Places_List)

def map_working(request):
    PlaceLocations = Objects_Places_Reason.objects.values('Reason_id', 'Objects_Name__Object_Name', 'Objects_Name__Object_Description', 'Places_Name__Place_Name', 'Places_Name__Latitude', 'Places_Name__Longitude')
    return render_to_csv_response(PlaceLocations)

#def map_working(request):
 #   for MapPrint in Objects_Places_Reason.objects.raw('SELECT `senufo_app_objects_places_reason`.`Reason_id`, `senufo_app_object_records`.`Object_Name`, `senufo_app_object_records`.`Object_Description`, `senufo_app_places`.`Place_Name`, `senufo_app_places`.`Latitude`, `senufo_app_places`.`Longitude` FROM ((`senufo_app_object_records` INNER JOIN `senufo_app_objects_places_reason`) INNER JOIN `senufo_app_places`) WHERE ((`senufo_app_objects_places_reason`.`Objects_Name_id` = `senufo_app_object_records`.`Object_id`) AND (`senufo_app_objects_places_reason`.`Places_Name_id` = `senufo_app_places`.`Places_id`))'):
 ##       response = HttpResponse(content_type='text/csv')
  #      response['Content-Disposition'] = 'attachment; filename="Object_Locations.csv"'
  #      writer = csv.writer(response)
  #      for Map in MapPrint:
  #          writer.writerow([Map])
  #      return response