from django.contrib import admin
from Senufo_App.models import Object_Records, Images, Artists_Creators, Places, Objects_Places_Reason

class Object_RecordsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Object_Name', 'Object_Type', 'Artist', 'ArtistAttributionCertainty', 'Object_Description', 'Object_Creation_date', 'Material', 'Dimensions', 'Essay', 'Essay_Author', 'Publication', 'Publication_PageNo', 'Publication_ImageNo')
        }),
        ('Collection Data and Provenance', {
            'fields': ('Collection_Name', 'Collection_Number', 'Collection_Information', 'Other_Publications', 'Reported_Provenance01_Earliest', 'Reported_Provenance02', 'Reported_Provenance03', 'Reported_Provenance04', 'Reported_Provenance05', 'Reported_Provenance06')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('ResearchNotes1', 'ResearchNotes2')
        }),
    )
    list_display = ('Object_Name', 'Object_Type', 'Object_Description')
    search_fields = ('Object_Name', 'Object_Type', 'Object_Description', 'Essay', 'ResearchNotes1', 'ResearchNotes2')


class ImagesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Image_Name', 'ImageCreator_Name', 'CreatorAttributionCertainty', 'Objects_ID_No1', 'Objects_ID_No2', 'Objects_ID_No3', 'Image_Filename', 'stable_url', 'HaveImage_YesNo', 'Copyright_Permissions', 'Image_Creation_Date')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('Image_Notes1',)
        }),
    )
    list_display = ('Image_Name', 'HaveImage_YesNo', 'Copyright_Permissions')
    search_fields = ('Image_Name', 'HaveImage_YesNo', 'Copyright_Permissions')



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


class PlacesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Place_Name', 'Latitude', 'Longitude', 'NGA_Place', 'NGA_Region', 'NGA_Country', 'Map_Place', 'Map_Country')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('Place_Notes1',)
        }),
    )
    list_display = ('Place_Name', 'Latitude', 'Longitude')
    search_fields = ('Place_Name', 'NGA_Place', 'NGA_Region', 'NGA_Country', 'Map_Place', 'Map_Country')


class Objects_Places_ReasonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Object_Name', 'Place_Name', 'ReasonForPlace')
        }),
        ('Notes for Research', {
            'classes': ('collapse',),
            'fields': ('ObjectPlaceReason_Notes1',)
        }),
    )
    list_display = ('Object_Name', 'Place_Name', 'ReasonForPlace')
    search_fields = ('ReasonForPlace',)


admin.site.register(Object_Records, Object_RecordsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Artists_Creators, Artists_CreatorsAdmin)
admin.site.register(Places, PlacesAdmin)
admin.site.register(Objects_Places_Reason, Objects_Places_ReasonAdmin)