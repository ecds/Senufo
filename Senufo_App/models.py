from django.db import connection, models
from tinymce.models import HTMLField

class Artists_Creators(models.Model):
    Artist_Name = models.CharField(max_length=200, verbose_name="Artist's Name", blank=True, null=True)
    Information = models.TextField(blank=True, null=True)
    Artist_Notes1 = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Artists and Creators'
        verbose_name_plural = 'Artists and Creators'
    def __unicode__(self):
        return u"%s" % (self.Artist_Name)

class Object_Records(models.Model):
    Object_id = models.AutoField(primary_key=True)
    Object_Name = models.CharField(max_length=200, blank=True, null=True)
    Object_Type = models.CharField(max_length=45, blank=True, null=True)
    Artist = models.ManyToManyField(Artists_Creators, blank=True)
    ArtistAttributionCertainty = models.CharField(verbose_name="Artist Attribution Certainty", max_length=200, blank=True, null=True)
    Artist_Attribution_Certainty_Numeric = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Object_Description = models.TextField(blank=True, null=True)
    Object_Creation_date = models.CharField(max_length=45, blank=True, null=True)
    Material = models.CharField(max_length=200, blank=True, null=True)
    Dimensions = models.CharField(max_length=200, blank=True, null=True)
    Essay = HTMLField(blank=True, null=True)
    Essay_Author = models.CharField(max_length=200, blank=True, null=True)
    Bibliography = HTMLField(blank=True, null=True)
    Citation_Format = models.CharField(max_length=200, blank=True, null=True)
    Publication_Information = HTMLField(blank=True, null=True)
    Collection_Name = models.CharField(max_length=200, blank=True, null=True)
    Collection_Number = models.CharField(max_length=200, blank=True, null=True)
    Collection_Information = models.CharField(max_length=500, blank=True, null=True)
    Other_Publications = models.CharField(max_length=500, blank=True, null=True)
    Reported_Provenance_Earliest = models.CharField(verbose_name='Provenance, Earliest Reported', max_length=500, blank=True, null=True)
    ResearchNotes1 = models.TextField(blank=True, null=True)
    ResearchNotes2 = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Objects'
        verbose_name_plural = 'Objects'
    def __unicode__(self):
        return u"%s" % (self.Object_Name)

class Provenance(models.Model):
    Additional_Reported_Provenance = models.CharField(max_length=500)
    Provenance = models.ForeignKey(Object_Records, blank=True, null=True)

    class Meta:
        verbose_name = 'Reported Provenance'
        verbose_name_plural = 'Additional Reported Provenance'
    def __unicode__(self):
        return u"%s" % (self.Additional_Reported_Provenance)

class Images(models.Model):
    Image_Name = models.CharField(max_length=500, blank=True, null=True)
    ImageCreator_Name = models.ManyToManyField(Artists_Creators, verbose_name="Image Creator's Name", blank=True)
    CreatorAttributionCertainty = models.CharField(verbose_name="Creator Attribution Certainty", max_length=200, blank=True, null=True)
    Creator_Attribution_Certainty_Numeric = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Objects_ID_No1 = models.ForeignKey('Object_Records', related_name='ImageObject1', blank=True, null=True)
    Objects_ID_No2 = models.ForeignKey('Object_Records', related_name='ImageObject2', blank=True, null=True)
    Objects_ID_No3 = models.ForeignKey('Object_Records', related_name='ImageObject3', blank=True, null=True)
    Image_Filename = models.CharField(max_length=200, blank=True, null=True)
    stable_url = models.CharField(max_length=200, blank=True, null=True)
    HaveImagePermissions_YesNo = models.CharField(max_length=15, verbose_name="Do we have Image Permissions? Y/N", blank=True, null=True)
    Copyright_Permissions = models.CharField(max_length=500, blank=True, null=True)
    Image_Creation_Date = models.CharField(max_length=45, blank=True, null=True)
    Image_Notes1 = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'
    def __unicode__(self):
        return u"%s" % (self.Image_Name)

class Places(models.Model):
    Places_id = models.AutoField(primary_key=True)
    Map_Place_Name = models.CharField(max_length=200, blank=True, null=True)
    Latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    NGA_Place_Name = models.CharField(max_length=100, blank=True, null=True)
    NGA_Region = models.CharField(max_length=50, blank=True, null=True)
    NGA_Country = models.CharField(max_length=50, blank=True, null=True)
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

class Objects_Places_Reason(models.Model):
    Reason_id = models.AutoField(primary_key=True)
    Objects_Name = models.ForeignKey('Object_Records', verbose_name="Object's Name", blank=True, null=True)
    Related_Image = models.ForeignKey('Images', blank=True, null=True)
    Places_Name = models.ForeignKey(Places, verbose_name="Place's Name", blank=True, null=True)
    ReasonForPlace = models.TextField(verbose_name="Reason for the Place", blank=True, null=True)
    Place_Attribution_Certainty = models.CharField(max_length=200, blank=True, null=True)
    Place_Attribution_Certainty_Numeric = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ObjectPlaceReason_Notes1 = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Object Locations and Reasons for them'
        verbose_name_plural = 'Object Locations and Reasons for them'
    def __unicode__(self):
        return u"%s, %s" % (self.Objects_Name, self.Places_Name)

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
