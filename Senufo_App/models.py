from django.db import connection, models
from tinymce.models import HTMLField

class Authors(models.Model):
    Author_Name = models.CharField(max_length=200, verbose_name="Author's Name", blank=True, null=True)
    Place_of_Birth = models.CharField(max_length=200, blank=True, null=True)
    Place_Active = models.TextField(blank=True, null=True)
    Dates_Active = models.CharField(max_length=200, blank=True, null=True)
    Bio_Information = models.TextField(blank=True, null=True, help_text="Additional biographical information")
    Author_Notes1 = models.TextField(blank=True, null=True)
    Author_Notes2 = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Authors'
        verbose_name_plural = 'Authors'
    def __unicode__(self):
        return u"%s" % (self.Author_Name)

class Work_Records(models.Model):
    Object_id = models.AutoField(primary_key=True)
    Work_Name = models.CharField(max_length=200, blank=True, null=True)
    Work_Type = models.CharField(max_length=45, blank=True, null=True, choices=(('Sculpture', 'Sculpture'),('Photograph', 'Photograph'),('PlaceHolder', 'Place Holder')))
    Author = models.ManyToManyField(Authors, blank=True)
    AuthorAttributionCertainty = models.CharField(verbose_name="Author Attribution Certainty", max_length=200, blank=True, null=True)
    Author_Attribution_Certainty_Numeric = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Object_Description = models.TextField(verbose_name="Description of Work", blank=True, null=True)
    Object_Creation_date = models.CharField(verbose_name="Work Creation Date", max_length=45, blank=True, null=True)
    Material = models.CharField(max_length=200, blank=True, null=True)
    Dimensions = models.CharField(max_length=200, blank=True, null=True)
    Publication_Information = HTMLField(blank=True, null=True, verbose_name="Selected Publication History")
    Collection_Name = models.CharField(max_length=200, blank=True, null=True)
    Collection_Number = models.CharField(max_length=200, blank=True, null=True)
    Collection_Information = models.CharField(max_length=255, blank=True, null=True)
    Other_Publications = models.TextField(blank=True, null=True)
    Reported_field_acquisition_name = models.CharField(max_length=255, blank=True, null=True)
    Reported_field_acquisition_location = models.ForeignKey('Places', blank=True, null=True)
    Reported_field_acquisition_date = models.CharField(max_length=255, blank=True, null=True)
    Reported_field_acquisition_date_numeric = models.IntegerField(blank=True, null=True)
    Reported_field_acquisition_certainty_notes = models.CharField(max_length=255, blank=True, null=True)
    Reported_field_acquisition_certainty_numeric = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Reported_field_acquisition_notes = models.TextField(blank=True, null=True)
    ResearchNotes1 = models.TextField(blank=True, null=True)
    ResearchNotes2 = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Works'
        verbose_name_plural = 'Works'
    def __unicode__(self):
        return u"%s" % (self.Work_Name)

class Provenance(models.Model):
    Reported_Provenance_name = models.CharField(max_length=500, help_text="Name of person or entity")
    Reported_Provenance_location = models.ForeignKey('Places', related_name="ProvLoc", blank=True, null=True)
    Reported_Provenance_date = models.CharField(max_length=500,blank=True, null=True)
    Reported_Provenance_start_date_numeric = models.IntegerField(blank=True, null=True)
    Provenance_Order = models.CharField(max_length=200, help_text="Earliest, second...?", blank=True, null=True)
    Reported_Provenance_notes = models.CharField(max_length=500, blank=True, null=True)
    Provenance = models.ForeignKey(Work_Records, blank=True, null=True)

    class Meta:
        verbose_name = 'Reported Provenance'
        verbose_name_plural = 'Additional Reported Provenance'
    def __unicode__(self):
        return u"%s" % (self.Reported_Provenance_name)

class Images(models.Model):
    Image_Name = models.CharField(max_length=500, blank=True, null=True)
    ImageAuthor_Name = models.ManyToManyField(Authors, verbose_name="Image Credits", help_text="Credited with Authorship of Image.", blank=True)
    AuthorAttributionCertainty = models.CharField(verbose_name="Attribution Certainty of Author Credited with Image", max_length=200, blank=True, null=True)
    Author_Attribution_Certainty_Numeric = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Works_ID = models.ManyToManyField('Work_Records', verbose_name="Related Works", related_name='ImageObject1', blank=True)
    Image_Filename = models.CharField(max_length=200, blank=True, null=True)
    stable_url = models.CharField(max_length=200, blank=True, null=True)
    HaveImagePermissions_YesNo = models.CharField(max_length=15, verbose_name="Do we have Image Permissions? Y/N", blank=True, null=True)
    Copyright_Permissions = HTMLField(blank=True, null=True, help_text="Describe our permissions.")
    Contact_Information_for_Copyright = HTMLField(blank=True, null=True, help_text="List the name, mailing address, e-mail address, telephone number, or other contact information for the identified rights holder.")
    Image_Creation_Date = models.CharField(max_length=45, blank=True, null=True)
    Photo_Credits = HTMLField(blank=True, null=True)
    Permissions_Correspondence_Date = models.CharField(max_length=200, blank=True, null=True, help_text="Date(s) of correspondence requesting image permissions.")
    Received_image_permission_date = models.CharField(max_length=200, blank=True, null=True)
    Image_Notes1 = models.TextField(blank=True, null=True)
    Image_Notes2 = models.TextField(blank=True, null=True)
    Image_Permissions_Notes = models.TextField(blank=True, null=True)
        
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'
    def __unicode__(self):
        return u"%s" % (self.Image_Name)

class Places(models.Model):
    Places_id = models.AutoField(primary_key=True)
    Map_Place_Name = models.CharField(max_length=200, verbose_name="Location Name", blank=True, null=True)
    Location_point_or_region = models.CharField(max_length=200, blank=True, null=True, help_text="Is this a point (city) or a region (polygon)?")
    Location_point_or_region_notes = models.TextField(blank=True, null=True, help_text="Scholarly region? Local term?")
    Latitude = models.DecimalField(max_digits=8, decimal_places=6, help_text="Decimal", blank=True, null=True)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6, help_text="Decimal", blank=True, null=True)
    NGA_Place_Name = models.CharField(max_length=100, blank=True, null=True)
    NGA_Administrative_Division = models.CharField(max_length=50, blank=True, null=True)
    NGA_Country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Geopolitical Entity Name", help_text="Country")
    Place_Notes1 = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Places'
        verbose_name_plural = 'Places'
    def __unicode__(self):
        return u"%s" % (self.Map_Place_Name)

class AdditionalPlaces(models.Model):
    Alternate_Place_Name = models.CharField(verbose_name="Alternate Place Name", max_length=200)
    Alternate_Name_Source = models.CharField(max_length=500, blank=True, null=True)
    NGA_Place_Name = models.ForeignKey(Places, blank=True, null=True)

    class Meta:
        verbose_name = 'Alternate Place Name or Spelling'
        verbose_name_plural = 'Alternate Place Names or Spellings'
    def __unicode__(self):
        return u"%s" % (self.Alternate_Place_Name)

#class ReasonForPlace(models.Model):
#    ReasonForPlace = models.CharField(max_length=200, blank=True, null=True)

class Objects_Places_Reason(models.Model):
    Reason_id = models.AutoField(primary_key=True)
    Objects_Name = models.ForeignKey('Work_Records', verbose_name="Work's Name", blank=True, null=True)
    Related_Image = models.ForeignKey('Images', blank=True, null=True)
    Places_Name = models.ForeignKey(Places, verbose_name="Place's Name", blank=True, null=True)
    ReasonForPlace = models.CharField(max_length=200, blank=True, null=True, verbose_name="Reason for Work-Place Association", choices=(('Artist', 'Artist'), ('Photograph', 'Photograph'), ('Drawing', 'Drawing'), ('Collection', 'Collection or Acquisition')))
    Place_Attribution_Certainty = models.CharField(max_length=200, blank=True, null=True)
    Place_Attribution_Certainty_Numeric = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ObjectPlaceReason_Notes1 = models.TextField(verbose_name="Work Location Reason Notes", blank=True, null=True)
    
    class Meta:
        verbose_name = 'Reasons for Mapped Work Locations'
        verbose_name_plural = 'Reasons for Mapped Work Locations'
    def __unicode__(self):
        return u"%s, %s" % (self.Objects_Name, self.Places_Name)

class Essays(models.Model):
#    Essay = HTMLField(blank=True, null=True)
#    Essay_Author = models.CharField(max_length=200, blank=True, null=True)
#    Essay_Date = models.CharField(max_length=100, blank=True, null=True)
#    Bibliography = HTMLField(blank=True, null=True)
    Essay_URL = models.URLField(max_length=200, blank=True, null=True)
    Citation_Format = models.CharField(max_length=200, blank=True, null=True)
    Related_Works = models.ManyToManyField(Work_Records, related_name='EssayObjects', blank=True)
    Related_Images = models.ManyToManyField(Images, related_name='EssayImages', blank=True)

    class Meta:
        verbose_name = 'Essay'
        verbose_name_plural = 'Essays'
    def __unicode__(self):
        return u"%s, %s" % (self.Citation_Format, self.Essay_URL)


#class PrintObjectPlace(models.Model):


#class GetDATAManager(models.Manager):
 #   def infostuff(self):
 #       cursor = connection.cursor()
 #       cursor.execute("'SELECT `senufo_app_objects_places_reason`.`Reason_id`, `senufo_app_object_records`.`Object_Name`, `senufo_app_object_records`.`Object_Description`, `senufo_app_places`.`Place_Name`, `senufo_app_places`.`Latitude`, `senufo_app_places`.`Longitude` FROM ((`senufo_app_object_records` INNER JOIN `senufo_app_objects_places_reason`) INNER JOIN `senufo_app_places`) WHERE ((`senufo_app_objects_places_reason`.`Objects_Name_id` = `senufo_app_object_records`.`Object_id`) AND (`senufo_app_objects_places_reason`.`Places_Name_id` = `senufo_app_places`.`Places_id`))'")
 #       return [row[0] for row in cursor.fetchone()]

#class GetDATAclass(models.Model):
#    ObjectName = GetDATAManager()


#class Print_Map(models.Model):
#    IDNo = models.AutoField(primary_key=True)
#    Object_Name = models.CharField(max_length=200, blank=True, null=True)
#    Object_Description = models.TextField(blank=True, null=True)
#    Place = models.CharField(max_length=200, blank=True, null=True)
#    Latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
#    Longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
#    class Meta:
#        db_table = 'Senufo_App_Print_Map'
#        managed = False
#        verbose_name = 'Print csv for the Map'
