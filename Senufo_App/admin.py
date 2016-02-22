from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from django.contrib import admin
from Senufo_App.models import Work_Records, Images, Essays, Authors, Places, Objects_Places_Reason, AdditionalPlaces, Provenance

class Work_RecordsResource(resources.ModelResource):
    Author = fields.Field(column_name='Author', attribute='Author', widget=ManyToManyWidget(Authors, ',', 'Author_Name'))
    class Meta:
        model = Work_Records
        fields = ('Work_Name', 'Work_Type', 'Object_Description', 'Author', 'AuthorAttributionCertainty', 'ResearchNotes1', 'ResearchNotes2',)
        export_order = ('Work_Name', 'Work_Type', 'Object_Description', 'Author', 'AuthorAttributionCertainty', 'ResearchNotes1', 'ResearchNotes2',)

class ProvenanceInline(admin.TabularInline):
    model = Provenance

class Work_RecordsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    filter_horizontal = ('Author',)
    resource_class = Work_RecordsResource
    fieldsets = (
        (None, {
            'fields': ('Work_Name', 'Work_Type', 'Author', 'AuthorAttributionCertainty', 'Author_Attribution_Certainty_Numeric', 'Description', 'Work_Creation_date', 'Work_Creation_date_numeric', 'Material', 'Dimensions', 'Publication_Information')
        }),
        ('Collection Data and Provenance', {
            'fields': ('Collection_Name', 'Collection_Number', 'Collection_Information', 'Other_Publications')
        }),
        ('Reported Field Acquisition', {
            'fields': ('Reported_field_acquisition_name', 'Reported_field_acquisition_location', 'Reported_field_acquisition_date', 'Reported_field_acquisition_date_numeric', 'Reported_field_acquisition_certainty_notes', 'Reported_field_acquisition_certainty_numeric')
        }),
       ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('ResearchNotes1', 'ResearchNotes2', 'Reported_field_acquisition_notes')
        }),
    )
    list_display = ('Work_Name', 'Work_Type', 'Description')
    inlines = [ProvenanceInline,]
    search_fields = ('Work_Name', 'Work_Type', 'Description', 'ResearchNotes1', 'ResearchNotes2', 'Material')

    
class ImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    filter_horizontal = ('ImageAuthor_Name', 'Works_ID')
    fieldsets = (
        (None, {
            'fields': ('Image_Name', 'ImageAuthor_Name', 'AuthorAttributionCertainty', 'Author_Attribution_Certainty_Numeric', 'Works_ID', 'Image_Filename', 'stable_url', 'Image_Creation_Date', 'Photo_Credits')
        }),
        ('Copyright and Permissions', {
            'fields': ('HaveImagePermissions_YesNo', 'Copyright_Permissions', 'Contact_Information_for_Copyright', 'Permissions_Correspondence_Date', 'Received_image_permission_date')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('Image_Notes1','Image_Notes2','Image_Permissions_Notes')
        }),
    )
    list_display = ('Image_Name', 'HaveImagePermissions_YesNo', 'Copyright_Permissions_html')
    search_fields = ('Image_Name', 'HaveImagePermissions_YesNo', 'Copyright_Permissions')

class EssaysAdmin(admin.ModelAdmin):
    search_fields = ('Essay_URL', 'Citation_Format')
    filter_horizontal = ('Related_Works','Related_Images')

class AuthorsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Author_Name', 'Place_of_Birth', 'Place_Active', 'Dates_Active', 'Bio_Information')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('Author_Notes1','Author_Notes2')
        }),
    )
    list_display = ('Author_Name', 'Place_of_Birth', 'Place_Active', 'Bio_Information')
    search_fields = ('Author_Name', 'Place_of_Birth', 'Place_Active', 'Bio_Information', 'Dates_Active', 'Author_Notes1', 'Author_Notes2')

class AdditionalPlacesInline(admin.TabularInline):
    model = AdditionalPlaces     

class PlacesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Map_Place_Name', 'Latitude', 'Longitude', 'Location_point_or_region', 'Location_point_or_region_notes', 'NGA_Place_Name', 'NGA_Administrative_Division', 'NGA_Country')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('Place_Notes1',)
        }),
    )
    list_display = ('Map_Place_Name', 'Latitude', 'Longitude')
    inlines = [AdditionalPlacesInline,]
    search_fields = ('Map_Place_Name', 'Location_point_or_region', 'Location_point_or_region_notes', 'NGA_Place_Name', 'NGA_Administrative_Division', 'NGA_Country')


class Object_Places_ReasonResource(resources.ModelResource):
    Object_Name = fields.Field(column_name='Objects_Name', attribute='Objects_Name', widget=ForeignKeyWidget(Work_Records, 'Work_Name'))
    Place_Name = fields.Field(column_name='Places_Name', attribute='Places_Name', widget=ForeignKeyWidget(Places, 'Place_Name'))
    Image_Name = fields.Field(column_name='Related_Image', attribute='Related_Image', widget=ForeignKeyWidget(Images, 'Image_Name'))
    class Meta:
        model = Work_Records
        fields = ('Objects_Name', 'Image_Name', 'Places_Name',)
        export_order = ('Objects_Name', 'Image_Name', 'Places_Name',)

class Objects_Places_ReasonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Object_Places_ReasonResource
    fieldsets = (
        (None, {
            'fields': ('Objects_Name', 'Related_Image', 'Places_Name', 'ReasonForPlace', 'Place_Attribution_Certainty', 'Place_Attribution_Certainty_Numeric')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('WorkPlaceReason_Notes1',)
        }),
    )
    list_display = ('Objects_Name', 'Places_Name', 'ReasonForPlace')
    search_fields = ('ReasonForPlace', 'Place_Attribution_Certainty', 'Place_Attribution_Certainty_Numeric')

#class Print_MapResource(resources.ModelResource):
#    class Meta:
#        model = Print_Map
#        fields = ('Object_Name', 'Object_Description', 'Place', 'Latitude', 'Longitude',)
#        export_order = ('Object_Name', 'Object_Description', 'Place', 'Latitude', 'Longitude',)
  

#class Print_MapAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#    resource_class = Print_MapResource
#    list_display = ('IDNo', 'Object_Name', 'Object_Description', 'Place', 'Latitude', 'Longitude')

admin.site.register(Work_Records, Work_RecordsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Places, PlacesAdmin)
admin.site.register(Objects_Places_Reason, Objects_Places_ReasonAdmin)
admin.site.register(Essays, EssaysAdmin)
#admin.site.register(ReasonForPlace)
#admin.site.register(GetDATAclass)
#admin.site.register(Print_Map, Print_MapAdmin)