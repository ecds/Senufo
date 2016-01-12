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


def map_working(request):
    PlaceLocations = Objects_Places_Reason.objects.values('Reason_id', 'Objects_Name__Object_Name', 'Objects_Name__Object_Description', 'Objects_Name__Artist__Artist_Name', 'Related_Image__Image_Name', 'Related_Image__ImageCreator_Name__Artist_Name', 'Related_Image__stable_url', 'Places_Name__Map_Place_Name', 'Places_Name__Latitude', 'Places_Name__Longitude')
    return render_to_csv_response(PlaceLocations)

