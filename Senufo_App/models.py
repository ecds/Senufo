from django.db import models

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
    Object_Name = models.CharField(max_length=200, blank=True, null=True)
    Object_Type = models.CharField(max_length=45, blank=True, null=True)
    Artist = models.ManyToManyField(Artists_Creators, blank=True)
    ArtistAttributionCertainty = models.CharField(max_length=200, blank=True, null=True)
    Object_Description = models.TextField(blank=True, null=True)
    Object_Creation_date = models.CharField(max_length=45, blank=True, null=True)
    Material = models.CharField(max_length=200, blank=True, null=True)
    Dimensions = models.CharField(max_length=200, blank=True, null=True)
    Essay = models.TextField(blank=True, null=True)
    Essay_Author = models.CharField(max_length=200, blank=True, null=True)
    Publication = models.CharField(max_length=500, blank=True, null=True)
    Publication_PageNo = models.CharField(max_length=45, blank=True, null=True)
    Publication_ImageNo = models.CharField(max_length=45, blank=True, null=True)
    Collection_Name = models.CharField(max_length=200, blank=True, null=True)
    Collection_Number = models.CharField(max_length=200, blank=True, null=True)
    Collection_Information = models.CharField(max_length=500, blank=True, null=True)
    Other_Publications = models.CharField(max_length=500, blank=True, null=True)
    Reported_Provenance01_Earliest = models.CharField(max_length=500, blank=True, null=True)
    Reported_Provenance02 = models.CharField(max_length=500, blank=True, null=True)
    Reported_Provenance03 = models.CharField(max_length=500, blank=True, null=True)
    Reported_Provenance04 = models.CharField(max_length=500, blank=True, null=True)
    Reported_Provenance05 = models.CharField(max_length=500, blank=True, null=True)
    Reported_Provenance06 = models.CharField(max_length=500, blank=True, null=True)
    ResearchNotes1 = models.TextField(blank=True, null=True)
    ResearchNotes2 = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Objects'
        verbose_name_plural = 'Objects'
    def __unicode__(self):
        return u"%s" % (self.Object_Name)

class Images(models.Model):
    Image_Name = models.CharField(max_length=500, blank=True, null=True)
    ImageCreator_Name = models.ManyToManyField(Artists_Creators, verbose_name="Image Creator's Name", blank=True)
    CreatorAttributionCertainty = models.CharField(max_length=200, blank=True, null=True)
    Objects_ID_No1 = models.ForeignKey('Object_Records', related_name='ImageObject1', blank=True, null=True)
    Objects_ID_No2 = models.ForeignKey('Object_Records', related_name='ImageObject2', blank=True, null=True)
    Objects_ID_No3 = models.ForeignKey('Object_Records', related_name='ImageObject3', blank=True, null=True)
    Image_Filename = models.CharField(max_length=200, blank=True, null=True)
    stable_url = models.CharField(max_length=200, blank=True, null=True)
    HaveImage_YesNo = models.CharField(max_length=15, blank=True, null=True)
    Copyright_Permissions = models.CharField(max_length=500, blank=True, null=True)
    Image_Creation_Date = models.CharField(max_length=45, blank=True, null=True)
    Image_Notes1 = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'
    def __unicode__(self):
        return u"%s" % (self.Image_Name)


class Places(models.Model):
    Place_Name = models.CharField(max_length=200, blank=True, null=True)
    Latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    NGA_Place = models.CharField(max_length=100, blank=True, null=True)
    NGA_Region = models.CharField(max_length=50, blank=True, null=True)
    NGA_Country = models.CharField(max_length=50, blank=True, null=True)
    Map_Place = models.CharField(max_length=100, blank=True, null=True)
    Map_Country = models.CharField(max_length=50, blank=True, null=True)
    Place_Notes1 = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Places'
        verbose_name_plural = 'Places'
    def __unicode__(self):
        return u"%s" % (self.Place_Name)


class Objects_Places_Reason(models.Model):
    Object_Name = models.ForeignKey('Object_Records', blank=True, null=True)
    Place_Name = models.ForeignKey(Places, blank=True, null=True)
    ReasonForPlace = models.TextField(blank=True, null=True)
    ObjectPlaceReason_Notes1 = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Object Locations and Reasons for them'
        verbose_name_plural = 'Object Locations and Reasons for them'
    def __unicode__(self):
        return u"%s, %s" % (self.Object_Name, self.Place_Name)