from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from django.contrib import admin
from Senufo_App.models import Object_Records, Images, Artists_Creators, Places, Objects_Places_Reason, AdditionalPlaces, Provenance

class Object_RecordsResource(resources.ModelResource):
    Artist = fields.Field(column_name='Artist', attribute='Artist', widget=ManyToManyWidget(Artists_Creators, ',', 'Artist_Name'))
    class Meta:
        model = Object_Records
        fields = ('Object_Name', 'Object_Type', 'Object_Description', 'Artist', 'ArtistAttributionCertainty', 'Essay', 'ResearchNotes1', 'ResearchNotes2',)
        export_order = ('Object_Name', 'Object_Type', 'Object_Description', 'Artist', 'ArtistAttributionCertainty', 'Essay', 'ResearchNotes1', 'ResearchNotes2',)

class ProvenanceInline(admin.TabularInline):
    model = Provenance

class Object_RecordsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    filter_horizontal = ('Artist',)
    resource_class = Object_RecordsResource
    fieldsets = (
        (None, {
            'fields': ('Object_Name', 'Object_Type', 'Artist', 'ArtistAttributionCertainty', 'Artist_Attribution_Certainty_Numeric', 'Object_Description', 'Object_Creation_date', 'Material', 'Dimensions', 'Publication_Information')
        }),
        ('Essay',{
            'fields': ('Essay', 'Essay_Author', 'Bibliography', 'Citation_Format')
        }),
        ('Collection Data and Provenance', {
            'fields': ('Collection_Name', 'Collection_Number', 'Collection_Information', 'Other_Publications', 'Reported_Provenance_Earliest')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('ResearchNotes1', 'ResearchNotes2')
        }),
    )
    list_display = ('Object_Name', 'Object_Type', 'Object_Description')
    inlines = [ProvenanceInline,]
    search_fields = ('Object_Name', 'Object_Type', 'Object_Description', 'Essay', 'ResearchNotes1', 'ResearchNotes2')

    
class ImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    filter_horizontal = ('ImageCreator_Name',)
    fieldsets = (
        (None, {
            'fields': ('Image_Name', 'ImageCreator_Name', 'CreatorAttributionCertainty', 'Creator_Attribution_Certainty_Numeric', 'Objects_ID_No1', 'Objects_ID_No2', 'Objects_ID_No3', 'Image_Filename', 'stable_url', 'HaveImagePermissions_YesNo', 'Copyright_Permissions', 'Image_Creation_Date')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('Image_Notes1',)
        }),
    )
    list_display = ('Image_Name', 'HaveImagePermissions_YesNo', 'Copyright_Permissions')
    search_fields = ('Image_Name', 'HaveImagePermissions_YesNo', 'Copyright_Permissions')



class Artists_CreatorsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Artist_Name', 'Information')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('Artist_Notes1',)
        }),
    )
    list_display = ('Artist_Name', 'Information')
    search_fields = ('Artist_Name', 'Information', 'Artist_Notes1')

class AdditionalPlacesInline(admin.TabularInline):
    model = AdditionalPlaces     

class PlacesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Map_Place_Name', 'Latitude', 'Longitude', 'NGA_Place_Name', 'NGA_Region', 'NGA_Country')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('Place_Notes1',)
        }),
    )
    list_display = ('Map_Place_Name', 'Latitude', 'Longitude')
    inlines = [AdditionalPlacesInline,]
    search_fields = ('Map_Place_Name', 'NGA_Place_Name', 'NGA_Region', 'NGA_Country')


class Object_Places_ReasonResource(resources.ModelResource):
    Object_Name = fields.Field(column_name='Objects_Name', attribute='Objects_Name', widget=ForeignKeyWidget(Object_Records, 'Object_Name'))
    Place_Name = fields.Field(column_name='Places_Name', attribute='Places_Name', widget=ForeignKeyWidget(Places, 'Place_Name'))
    Image_Name = fields.Field(column_name='Related_Image', attribute='Related_Image', widget=ForeignKeyWidget(Images, 'Image_Name'))
    class Meta:
        model = Object_Records
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
            'fields': ('ObjectPlaceReason_Notes1',)
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

admin.site.register(Object_Records, Object_RecordsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Artists_Creators, Artists_CreatorsAdmin)
admin.site.register(Places, PlacesAdmin)
admin.site.register(Objects_Places_Reason, Objects_Places_ReasonAdmin)
#admin.site.register(GetDATAclass)
#admin.site.register(Print_Map, Print_MapAdmin)