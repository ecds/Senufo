from django.db import models

class Artists_Creators(models.Model):
    Artist_Name = models.CharField(max_length=200, verbose_name="Artist's Name")
    Information = models.TextField()
    Artist_Notes1 = models.TextField()

    class Meta:
        verbose_name = 'Artists and Creators'
        verbose_name_plural = 'Artists and Creators'
    def __unicode__(self):
        return u"%s" % (self.Artist_Name)

class Object_Records(models.Model):
    Object_Name = models.CharField(max_length=200)
    Object_Type = models.CharField(max_length=45)
    Artist = models.ManyToManyField(Artists_Creators)
    ArtistAttributionCertainty = models.CharField(max_length=200)
    Object_Description = models.TextField()
    Object_Creation_date = models.CharField(max_length=45)
    Material = models.CharField(max_length=200)
    Dimensions = models.CharField(max_length=200)
    Essay = models.TextField()
    Essay_Author = models.CharField(max_length=200)
    Publication = models.CharField(max_length=500)
    Publication_PageNo = models.CharField(max_length=45)
    Publication_ImageNo = models.CharField(max_length=45)
    Collection_Name = models.CharField(max_length=200)
    Collection_Number = models.CharField(max_length=200)
    Collection_Information = models.CharField(max_length=500)
    Other_Publications = models.CharField(max_length=500)
    Reported_Provenance01_Earliest = models.CharField(max_length=500)
    Reported_Provenance02 = models.CharField(max_length=500)
    Reported_Provenance03 = models.CharField(max_length=500)
    Reported_Provenance04 = models.CharField(max_length=500)
    Reported_Provenance05 = models.CharField(max_length=500)
    Reported_Provenance06 = models.CharField(max_length=500)
    ResearchNotes1 = models.TextField()
    ResearchNotes2 = models.TextField()

    class Meta:
        verbose_name = 'Objects'
        verbose_name_plural = 'Objects'
    def __unicode__(self):
        return u"%s" % (self.Object_Name)

class Images(models.Model):
    Image_Name = models.CharField(max_length=500)
    ImageCreator_Name = models.ManyToManyField(Artists_Creators, verbose_name="Image Creator's Name")
    CreatorAttributionCertainty = models.CharField(max_length=200)
    Objects_ID_No1 = models.ForeignKey('Object_Records', related_name='ImageObject1')
    Objects_ID_No2 = models.ForeignKey('Object_Records', related_name='ImageObject2')
    Objects_ID_No3 = models.ForeignKey('Object_Records', related_name='ImageObject3')
    Image_Filename = models.CharField(max_length=200)
    stable_url = models.CharField(max_length=200)
    HaveImage_YesNo = models.CharField(max_length=15)
    Copyright_Permissions = models.CharField(max_length=500)
    Image_Creation_Date = models.CharField(max_length=45)
    Image_Notes1 = models.TextField()
    
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'
    def __unicode__(self):
        return u"%s" % (self.Image_Name)


class Places(models.Model):
    Place_Name = models.CharField(max_length=200)
    Latitude = models.DecimalField(max_digits=8, decimal_places=6)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6)
    NGA_Place = models.CharField(max_length=100)
    NGA_Region = models.CharField(max_length=50)
    NGA_Country = models.CharField(max_length=50)
    Map_Place = models.CharField(max_length=100)
    Map_Country = models.CharField(max_length=50)
    Place_Notes1 = models.TextField()
    
    class Meta:
        verbose_name = 'Places'
        verbose_name_plural = 'Places'
    def __unicode__(self):
        return u"%s" % (self.Place_Name)


class Objects_Places_Reason(models.Model):
    Object_Name = models.ForeignKey('Object_Records')
    Place_Name = models.ForeignKey(Places)
    ReasonForPlace = models.TextField()
    ObjectPlaceReason_Notes1 = models.TextField()
    
    class Meta:
        verbose_name = 'Object Locations and Reasons for them'
        verbose_name_plural = 'Object Locations and Reasons for them'
    def __unicode__(self):
        return u"%s, %s" % (self.Object_Name, self.Place_Name)