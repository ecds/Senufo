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
#from django.db import connection

import csv
from django.shortcuts import render
from django.http import HttpResponse
from djqscsv import render_to_csv_response
from Senufo_App.models import Work_Records, Images, Authors, Places, Works_Places
from django.db import connection

def map_working(request):
    PlaceLocations = Works_Places.objects.values('Reason_id', 'ReasonForPlace', 'Objects_Name__Work_Name', 'Objects_Name__Description', 'Objects_Name__Author__Author_Name', 'Objects_Name__AuthorAttributionCertainty', 'Objects_Name__Work_Creation_date', 'Related_Image__Image_Name', 'Related_Image__ImageAuthor_Name__Author_Name', 'Related_Image__stable_url', 'Places_Name__Map_Place_Name', 'Places_Name__Latitude', 'Places_Name__Longitude').filter(ReasonForPlace='Artist')
    return render_to_csv_response(PlaceLocations)

def map_working_drawingphoto(request):
    PlaceLocationDrawingPhoto = Works_Places.objects.values('Reason_id', 'ReasonForPlace', 'Objects_Name__Work_Name', 'Objects_Name__Description', 'Objects_Name__Author__Author_Name', 'Objects_Name__AuthorAttributionCertainty', 'Objects_Name__Work_Creation_date', 'Related_Image__Image_Name', 'Related_Image__ImageAuthor_Name__Author_Name', 'Related_Image__stable_url', 'Places_Name__Map_Place_Name', 'Places_Name__Latitude', 'Places_Name__Longitude').filter(Q(ReasonForPlace='Photograph') | Q(ReasonForPlace='Drawing'))
    return render_to_csv_response(PlaceLocationDrawingPhoto)

def map_working_collection(request):
    PlaceLocationCollection = Works_Places.objects.values('Reason_id', 'ReasonForPlace', 'Objects_Name__Work_Name', 'Objects_Name__Description', 'Objects_Name__Author__Author_Name', 'Objects_Name__AuthorAttributionCertainty', 'Objects_Name__Work_Creation_date', 'Related_Image__Image_Name', 'Related_Image__ImageAuthor_Name__Author_Name', 'Related_Image__stable_url', 'Places_Name__Map_Place_Name', 'Places_Name__Latitude', 'Places_Name__Longitude').filter(ReasonForPlace='Collection')
    return render_to_csv_response(PlaceLocationCollection)

# Still working on this.  How to link in-lines - alternate place names, provenance fields. How to link to essay url? = All 3 are backwards ForeignKey. Check into a mySQL view (workbench) for this!!
def mapped_work_page_view(request):
    WorkPageInformation = Works_Places.objects.values('Reason_id', 'Objects_Name__Work_Name', 'Objects_Name__Description', 'Objects_Name__Author__Author_Name', 'Objects_Name__AuthorAttributionCertainty', 'Objects_Name__Work_Creation_date', 'Objects_Name__Publication_Information', 'Objects_Name__Collection_Name', 'Objects_Name__Collection_Number', 'Objects_Name__Reported_field_acquisition_name', 'Objects_Name__Reported_field_acquisition_location__Map_Place_Name', 'Objects_Name__Reported_field_acquisition_date', 'Related_Image__ImageAuthor_Name__Author_Name')
    return render_to_csv_response(WorkPageInformation)
    
    
def mapped_work_webpage_view(request):
    MappedWorkItems = Works_Places.objects.raw('SELECT `senufo_app_works_places`.`Reason_id`, `senufo_app_work_records`.`Description`,`senufo_app_places`.`Map_Place_Name`, `senufo__db`.`senufo_app_work_records`.`Publication_Information`,`senufo__db`.`senufo_app_work_records`.`Collection_Name` AS `Collection_Name`,`senufo__db`.`senufo_app_work_records`.`Collection_Number` AS `Collection_Number`,`senufo__db`.`senufo_app_work_records`.`Reported_field_acquisition_name`,`senufo_app_places2`.`Map_Place_Name` AS `Reported_field_location`,`senufo_app_work_records`.`Reported_field_acquisition_date`,`senufo_app_images`.`Image_Filename`, GROUP_CONCAT(`senufo__db`.`senufo_app_authors`.`Author_Name`) AS `Image_Credits`, GROUP_CONCAT(`senufo_app_provenance`.`Reported_Provenance_name`) AS `Reported_Provenance_name`, GROUP_CONCAT(`senufo_app_places3`.`Map_Place_Name`) AS `Reported_Provenance_location`, GROUP_CONCAT(`senufo__db`.`senufo_app_provenance`.`Reported_Provenance_date`) AS `Reported_Provenance_date`, GROUP_CONCAT(`senufo_app_essays`.`Essay_URL`) AS `Essay_URL` FROM `senufo_app_works_places` left join `senufo_app_work_records` on `senufo_app_works_places`.`Objects_Name_id`=`senufo_app_work_records`.`Object_id`  left join `senufo_app_provenance` on `senufo_app_work_records`.`Object_id` = `senufo_app_provenance`.`Provenance_id` left join `senufo_app_images`on `senufo_app_works_places`.`Related_Image_id`=`senufo_app_images`.`id` left join `senufo_app_places`on `senufo_app_works_places`.`Places_Name_id`= `senufo_app_places`.`Places_id`  left join `senufo_app_additionalplaces` on `senufo_app_places`.`Places_id` = `senufo_app_additionalplaces`.`NGA_Place_Name_id` left join `senufo_app_essays_related_works` on `senufo_app_work_records`.`Object_id` = `senufo_app_essays_related_works`.`work_records_id` left join `senufo_app_essays` on `senufo_app_essays_related_works`.`essays_id` = `senufo_app_essays`.`id` left join `senufo_app_images_imageauthor_name` on `senufo_app_images`.`id` = `senufo_app_images_imageauthor_name`.`images_id` left join `senufo_app_authors` on `senufo_app_images_imageauthor_name`.`authors_id` = `senufo_app_authors`.`id` left join `senufo_app_places` `senufo_app_places2` on `senufo_app_work_records`.`Reported_field_acquisition_location_id` = `senufo_app_places2`.`Places_id` left join `senufo_app_places` `senufo_app_places3` on `senufo_app_provenance`.`Reported_Provenance_location_id` = `senufo_app_places3`.`Places_id` GROUP BY `senufo_app_works_places`.`Reason_id`')

    return render_to_csv_response(MappedWorkItems)

#def Page(self):
#    cursor = connection.cursor()

#    cursor.execute("CREATE VIEW `wordpress_page_view` AS SELECT `senufo_app_objects_places_reason`.`Reason_id` AS `Reason_id`, `senufo_app_work_records`.`Description` AS `Description`, `senufo_app_work_records`.`Work_Creation_date` AS `Date`, `senufo_app_places`.`Map_Place_Name` AS `Map_Place_Name`, `senufo_app_objects_places_reason`.`ReasonForPlace` AS `ReasonForPlace`, `senufo_app_work_records`.`Collection_Name` AS `Collection_Name`, `senufo_app_work_records`.`Collection_Number` AS `Collection_Number`, `senufo_app_images`.`Image_Filename` AS `Image_Filename`, GROUP_CONCAT(DISTINCT `senufo_app_authors`.`Author_Name` SEPARATOR ',') AS `Image_Credits`, `senufo_app_work_records`.`Reported_field_acquisition_name` AS `Reported_field_acquisition_name`, `senufo_app_places2`.`Map_Place_Name` AS `Reported_field_location`, `senufo_app_work_records`.`Reported_field_acquisition_date` AS `Reported_field_acquisition_date`, GROUP_CONCAT(DISTINCT `senufo_app_provenance`.`Reported_Provenance_name` SEPARATOR ',') AS `Reported_Provenance_name`, GROUP_CONCAT(DISTINCT `senufo_app_places3`.`Map_Place_Name` SEPARATOR ',') AS `Reported_Provenance_location`, GROUP_CONCAT(DISTINCT `senufo_app_provenance`.`Reported_Provenance_date` SEPARATOR ',') AS `Reported_Provenance_date`, `senufo_app_work_records`.`Publication_Information` AS `Selected_Publication_History`, GROUP_CONCAT(DISTINCT `senufo_app_essays`.`Essay_Title` SEPARATOR ',') AS `Essay_Title`, GROUP_CONCAT(DISTINCT `senufo_app_essays`.`Essay_Author` SEPARATOR ',') AS `Essay_Author`, GROUP_CONCAT(DISTINCT `senufo_app_essays`.`Essay_URL` SEPARATOR ',') AS `Essay_URL`, GROUP_CONCAT(DISTINCT `senufo_app_essays`.`Citation_Format` SEPARATOR ',') AS `Citation_Format`, GROUP_CONCAT(DISTINCT `senufo_app_images2`.`Image_Filename` SEPARATOR ',') AS `Related_Images`    FROM(((((((((((((`senufo_app_objects_places_reason` LEFT JOIN `senufo_app_work_records` ON ((`senufo_app_objects_places_reason`.`Objects_Name_id` = `senufo_app_work_records`.`Object_id`)) LEFT JOIN `senufo_app_provenance` ON ((`senufo_app_work_records`.`Object_id` = `senufo_app_provenance`.`Provenance_id`))) LEFT JOIN `senufo_app_images` ON ((`senufo_app_objects_places_reason`.`Related_Image_id` = `senufo_app_images`.`id`))) LEFT JOIN `senufo_app_places` ON ((`senufo_app_objects_places_reason`.`Places_Name_id` = `senufo_app_places`.`Places_id`))) LEFT JOIN `senufo_app_additionalplaces` ON ((`senufo_app_places`.`Places_id` = `senufo_app_additionalplaces`.`NGA_Place_Name_id`))) LEFT JOIN `senufo_app_essays_related_works` ON ((`senufo_app_work_records`.`Object_id` = `senufo_app_essays_related_works`.`work_records_id`))) LEFT JOIN `senufo_app_essays` ON ((`senufo_app_essays_related_works`.`essays_id` = `senufo_app_essays`.`id`))) LEFT JOIN `senufo_app_images_imageauthor_name` ON ((`senufo_app_images`.`id` = `senufo_app_images_imageauthor_name`.`images_id`))) LEFT JOIN `senufo_app_authors` ON ((`senufo_app_images_imageauthor_name`.`authors_id` = `senufo_app_authors`.`id`))) LEFT JOIN `senufo_app_places` `senufo_app_places2` ON ((`senufo_app_work_records`.`Reported_field_acquisition_location_id` = `senufo_app_places2`.`Places_id`))) LEFT JOIN `senufo_app_places` `senufo_app_places3` ON ((`senufo_app_provenance`.`Reported_Provenance_location_id` = `senufo_app_places3`.`Places_id`))) LEFT JOIN `senufo_app_essays_related_images` ON ((`senufo_app_essays`.`id` = `senufo_app_essays_related_images`.`essays_id`))) LEFT JOIN `senufo_app_images` `senufo_app_images2` ON ((`senufo_app_essays_related_images`.`images_id` = `senufo_app_images`.`id`))) GROUP BY `senufo_app_objects_places_reason`.`Reason_id`")
#    row = cursor.fetchall()
        
#    render_to_response("Page.html", {"row":row})


#def Page(request):
#    Page = Objects_Places_Reason.objects.SQL()
#    render_to_response("Page.html", {"Page":Page})