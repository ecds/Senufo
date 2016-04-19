# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalPlaces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Alternate_Place_Name', models.CharField(max_length=200, verbose_name=b'Alternate Place Name')),
                ('Alternate_Name_Source', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Alternate Place Name or Spelling',
                'verbose_name_plural': 'Alternate Place Names or Spellings',
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Author_Name', models.CharField(max_length=200, null=True, verbose_name=b"Author's Name", blank=True)),
                ('Place_of_Birth', models.CharField(max_length=200, null=True, blank=True)),
                ('Place_Active', models.TextField(null=True, blank=True)),
                ('Dates_Active', models.CharField(max_length=200, null=True, blank=True)),
                ('Bio_Information', models.TextField(help_text=b'Additional biographical information', null=True, blank=True)),
                ('Author_Notes1', models.TextField(null=True, blank=True)),
                ('Author_Notes2', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Authors',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Image_Name', models.CharField(max_length=500, null=True, blank=True)),
                ('AuthorAttributionCertainty', models.CharField(max_length=200, null=True, verbose_name=b'Attribution Certainty of Author Credited with Image', blank=True)),
                ('Author_Attribution_Certainty_Numeric', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('Image_Filename', models.CharField(max_length=200, null=True, blank=True)),
                ('stable_url', models.URLField(null=True, blank=True)),
                ('HaveImagePermissions_YesNo', models.CharField(max_length=15, null=True, verbose_name=b'Do we have Image Permissions? Y/N', blank=True)),
                ('Copyright_Permissions', tinymce.models.HTMLField(help_text=b'Describe our permissions.', null=True, blank=True)),
                ('Contact_Information_for_Copyright', tinymce.models.HTMLField(help_text=b'List the name, mailing address, e-mail address, telephone number, or other contact information for the identified rights holder.', null=True, blank=True)),
                ('Image_Creation_Date', models.CharField(max_length=45, null=True, blank=True)),
                ('Photo_Credits', tinymce.models.HTMLField(null=True, blank=True)),
                ('Permissions_Correspondence_Date', models.CharField(help_text=b'Date(s) of correspondence requesting image permissions.', max_length=200, null=True, blank=True)),
                ('Received_image_permission_date', models.CharField(max_length=200, null=True, blank=True)),
                ('Image_Notes1', models.TextField(null=True, blank=True)),
                ('Image_Notes2', models.TextField(null=True, blank=True)),
                ('Image_Permissions_Notes', models.TextField(null=True, blank=True)),
                ('ImageAuthor_Name', models.ManyToManyField(help_text=b'Credited with Authorship of Image.', to='Senufo_App.Authors', verbose_name=b'Image Credits', blank=True)),
            ],
            options={
                'verbose_name': 'Images',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('Places_id', models.AutoField(serialize=False, primary_key=True)),
                ('Map_Place_Name', models.CharField(max_length=200, null=True, verbose_name=b'Location Name', blank=True)),
                ('Location_point_or_region', models.CharField(help_text=b'Is this a point (city) or a region (polygon)?', max_length=200, null=True, blank=True)),
                ('Location_point_or_region_notes', models.TextField(help_text=b'Scholarly region? Local term?', null=True, blank=True)),
                ('Latitude', models.DecimalField(help_text=b'Decimal', null=True, max_digits=8, decimal_places=6, blank=True)),
                ('Longitude', models.DecimalField(help_text=b'Decimal', null=True, max_digits=8, decimal_places=6, blank=True)),
                ('NGA_Place_Name', models.CharField(max_length=100, null=True, blank=True)),
                ('NGA_Administrative_Division', models.CharField(max_length=50, null=True, blank=True)),
                ('NGA_Country', models.CharField(help_text=b'Country', max_length=50, null=True, verbose_name=b'Geopolitical Entity Name', blank=True)),
                ('Place_Notes1', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Places',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.CreateModel(
            name='Provenance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Reported_Provenance_name', models.CharField(help_text=b'Name of person or entity', max_length=500)),
                ('Reported_Provenance_date', models.CharField(max_length=500, null=True, blank=True)),
                ('Reported_Provenance_start_date_numeric', models.IntegerField(null=True, blank=True)),
                ('Provenance_Order', models.CharField(help_text=b'Earliest, second...?', max_length=200, null=True, blank=True)),
                ('Reported_Provenance_notes', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Reported Provenance',
                'verbose_name_plural': 'Additional Reported Provenance',
            },
        ),
        migrations.CreateModel(
            name='Work_Records',
            fields=[
                ('Object_id', models.AutoField(serialize=False, primary_key=True)),
                ('Work_Name', models.CharField(max_length=200, null=True, blank=True)),
                ('Work_Type', models.CharField(blank=True, max_length=45, null=True, choices=[(b'Sculpture', b'Sculpture'), (b'Photograph', b'Photograph'), (b'Engraving', b'Engraving'), (b'Drawing', b'Drawing'), (b'Video Still', b'Video Still'), (b'Ceramic', b'Ceramic')])),
                ('AuthorAttributionCertainty', models.CharField(max_length=200, null=True, verbose_name=b'Author Attribution Certainty', blank=True)),
                ('Author_Attribution_Certainty_Numeric', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('Description', models.TextField(null=True, verbose_name=b'Description of Work', blank=True)),
                ('Work_Creation_date', models.CharField(max_length=45, null=True, verbose_name=b'Work Creation Date', blank=True)),
                ('Work_Creation_date_numeric', models.IntegerField(null=True, blank=True)),
                ('Material', models.CharField(help_text=b'Material(s) identified, based on Getty vocabulary.', max_length=200, null=True, blank=True)),
                ('Dimensions', models.CharField(max_length=200, null=True, blank=True)),
                ('Publication_Information', tinymce.models.HTMLField(null=True, verbose_name=b'Selected Publication History', blank=True)),
                ('Collection_Name', models.CharField(max_length=200, null=True, blank=True)),
                ('Collection_Number', models.CharField(max_length=200, null=True, blank=True)),
                ('Collection_Information', models.CharField(max_length=255, null=True, blank=True)),
                ('Not_For_Map', models.BooleanField(default=False)),
                ('Other_Publications', models.TextField(null=True, blank=True)),
                ('Reported_field_acquisition_name', models.CharField(max_length=255, null=True, blank=True)),
                ('Reported_field_acquisition_date', models.CharField(max_length=255, null=True, blank=True)),
                ('Reported_field_acquisition_date_numeric', models.IntegerField(null=True, blank=True)),
                ('Reported_field_acquisition_certainty_notes', models.CharField(max_length=255, null=True, blank=True)),
                ('Reported_field_acquisition_certainty_numeric', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('Reported_field_acquisition_notes', models.TextField(null=True, blank=True)),
                ('ResearchNotes1', models.TextField(null=True, blank=True)),
                ('ResearchNotes2', models.TextField(null=True, blank=True)),
                ('Author', models.ManyToManyField(to='Senufo_App.Authors', blank=True)),
                ('Reported_field_acquisition_location', models.ForeignKey(blank=True, to='Senufo_App.Places', null=True)),
            ],
            options={
                'verbose_name': 'Works',
                'verbose_name_plural': 'Works',
            },
        ),
        migrations.CreateModel(
            name='Works_Places',
            fields=[
                ('WorkPlace_id', models.AutoField(serialize=False, primary_key=True)),
                ('ReasonForPlace_Artist', models.BooleanField(default=False)),
                ('ReasonForPlace_Drawing', models.BooleanField(default=False)),
                ('ReasonForPlace_Photograph', models.BooleanField(default=False)),
                ('ReasonForPlace_Collection', models.BooleanField(default=False)),
                ('Place_Attribution_Certainty', models.CharField(max_length=200, null=True, blank=True)),
                ('Place_Attribution_Certainty_Numeric', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('Work_URL', models.URLField(help_text=b'Current link to the WordPress page for this work-place instance.', null=True, blank=True)),
                ('Essay_Title', models.CharField(max_length=200, null=True, blank=True)),
                ('Essay_Author', models.CharField(max_length=200, null=True, blank=True)),
                ('Essay_Date', models.CharField(max_length=200, null=True, blank=True)),
                ('Essay_URL', models.URLField(null=True, blank=True)),
                ('Citation_Format', models.CharField(help_text=b'How to cite this essay.', max_length=200, null=True, blank=True)),
                ('WorkPlace_Notes1', models.TextField(null=True, verbose_name=b'Work Location Reason Notes', blank=True)),
                ('Main_Work_Image', models.ForeignKey(blank=True, to='Senufo_App.Images', null=True)),
                ('Objects_Name', models.ForeignKey(verbose_name=b"Work's Name", blank=True, to='Senufo_App.Work_Records', null=True)),
                ('Places_Name', models.ForeignKey(verbose_name=b"Place's Name", blank=True, to='Senufo_App.Places', null=True)),
                ('Related_Images', models.ManyToManyField(related_name='EssayImages', to='Senufo_App.Images', blank=True)),
            ],
            options={
                'verbose_name': 'Mapped Work Location',
                'verbose_name_plural': 'Mapped Work Locations',
            },
        ),
        migrations.AddField(
            model_name='provenance',
            name='Provenance',
            field=models.ForeignKey(blank=True, to='Senufo_App.Work_Records', null=True),
        ),
        migrations.AddField(
            model_name='provenance',
            name='Reported_Provenance_location',
            field=models.ForeignKey(related_name='ProvLoc', blank=True, to='Senufo_App.Places', null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='Works_ID',
            field=models.ManyToManyField(related_name='ImageObject1', verbose_name=b'Related Works', to='Senufo_App.Work_Records', blank=True),
        ),
        migrations.AddField(
            model_name='additionalplaces',
            name='NGA_Place_Name',
            field=models.ForeignKey(blank=True, to='Senufo_App.Places', null=True),
        ),
    ]
