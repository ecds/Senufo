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
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext


import csv
from django.shortcuts import render
from django.http import HttpResponse
from djqscsv import render_to_csv_response
from Senufo_App.models import Work_Records, Images, Authors, Places, Objects_Places_Reason


def map_working(request):
    PlaceLocations = Objects_Places_Reason.objects.values('Reason_id', 'ReasonForPlace', 'Objects_Name__Work_Name', 'Objects_Name__Object_Description', 'Objects_Name__Author__Author_Name', 'Objects_Name__AuthorAttributionCertainty', 'Objects_Name__Object_Creation_date', 'Related_Image__Image_Name', 'Related_Image__ImageAuthor_Name__Author_Name', 'Related_Image__stable_url', 'Places_Name__Map_Place_Name', 'Places_Name__Latitude', 'Places_Name__Longitude').filter(ReasonForPlace='Artist')
    return render_to_csv_response(PlaceLocations)

def map_working_drawingphoto(request):
    PlaceLocationDrawingPhoto = Objects_Places_Reason.objects.values('Reason_id', 'ReasonForPlace', 'Objects_Name__Work_Name', 'Objects_Name__Object_Description', 'Objects_Name__Author__Author_Name', 'Objects_Name__AuthorAttributionCertainty', 'Objects_Name__Object_Creation_date', 'Related_Image__Image_Name', 'Related_Image__ImageAuthor_Name__Author_Name', 'Related_Image__stable_url', 'Places_Name__Map_Place_Name', 'Places_Name__Latitude', 'Places_Name__Longitude').filter(Q(ReasonForPlace='Photograph') | Q(ReasonForPlace='Drawing'))
    return render_to_csv_response(PlaceLocationDrawingPhoto)

def map_working_collection(request):
    PlaceLocationCollection = Objects_Places_Reason.objects.values('Reason_id', 'ReasonForPlace', 'Objects_Name__Work_Name', 'Objects_Name__Object_Description', 'Objects_Name__Author__Author_Name', 'Objects_Name__AuthorAttributionCertainty', 'Objects_Name__Object_Creation_date', 'Related_Image__Image_Name', 'Related_Image__ImageAuthor_Name__Author_Name', 'Related_Image__stable_url', 'Places_Name__Map_Place_Name', 'Places_Name__Latitude', 'Places_Name__Longitude').filter(ReasonForPlace='Collection')
    return render_to_csv_response(PlaceLocationCollection)
