# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists_Creators',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Artist_Name', models.CharField(max_length=200, verbose_name=b"Artist's Name")),
                ('Information', models.TextField()),
                ('Artist_Notes1', models.TextField()),
            ],
            options={
                'verbose_name': 'Artists and Creators',
                'verbose_name_plural': 'Artists and Creators',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Image_Name', models.CharField(max_length=500)),
                ('CreatorAttributionCertainty', models.CharField(max_length=200)),
                ('Image_Filename', models.CharField(max_length=200)),
                ('stable_url', models.CharField(max_length=200)),
                ('HaveImage_YesNo', models.CharField(max_length=15)),
                ('Copyright_Permissions', models.CharField(max_length=500)),
                ('Image_Creation_Date', models.CharField(max_length=45)),
                ('Image_Notes1', models.TextField()),
                ('ImageCreator_Name', models.ManyToManyField(to='Senufo_App.Artists_Creators', verbose_name=b"Image Creator's Name")),
            ],
            options={
                'verbose_name': 'Images',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Object_Records',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Object_Name', models.CharField(max_length=200)),
                ('Object_Type', models.CharField(max_length=45)),
                ('ArtistAttributionCertainty', models.CharField(max_length=200)),
                ('Object_Description', models.TextField()),
                ('Object_Creation_date', models.CharField(max_length=45)),
                ('Material', models.CharField(max_length=200)),
                ('Dimensions', models.CharField(max_length=200)),
                ('Essay', models.TextField()),
                ('Essay_Author', models.CharField(max_length=200)),
                ('Publication', models.CharField(max_length=500)),
                ('Publication_PageNo', models.CharField(max_length=45)),
                ('Publication_ImageNo', models.CharField(max_length=45)),
                ('Collection_Name', models.CharField(max_length=200)),
                ('Collection_Number', models.CharField(max_length=200)),
                ('Collection_Information', models.CharField(max_length=500)),
                ('Other_Publications', models.CharField(max_length=500)),
                ('Reported_Provenance01_Earliest', models.CharField(max_length=500)),
                ('Reported_Provenance02', models.CharField(max_length=500)),
                ('Reported_Provenance03', models.CharField(max_length=500)),
                ('Reported_Provenance04', models.CharField(max_length=500)),
                ('Reported_Provenance05', models.CharField(max_length=500)),
                ('Reported_Provenance06', models.CharField(max_length=500)),
                ('ResearchNotes1', models.TextField()),
                ('ResearchNotes2', models.TextField()),
                ('Artist', models.ManyToManyField(to='Senufo_App.Artists_Creators')),
            ],
            options={
                'verbose_name': 'Objects',
                'verbose_name_plural': 'Objects',
            },
        ),
        migrations.CreateModel(
            name='Objects_Places_Reason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ReasonForPlace', models.TextField()),
                ('ObjectPlaceReason_Notes1', models.TextField()),
                ('Object_Name', models.ForeignKey(to='Senufo_App.Object_Records')),
            ],
            options={
                'verbose_name': 'Object Locations and Reasons for them',
                'verbose_name_plural': 'Object Locations and Reasons for them',
            },
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Place_Name', models.CharField(max_length=200)),
                ('Latitude', models.DecimalField(max_digits=8, decimal_places=6)),
                ('Longitude', models.DecimalField(max_digits=8, decimal_places=6)),
                ('NGA_Place', models.CharField(max_length=100)),
                ('NGA_Region', models.CharField(max_length=50)),
                ('NGA_Country', models.CharField(max_length=50)),
                ('Map_Place', models.CharField(max_length=100)),
                ('Map_Country', models.CharField(max_length=50)),
                ('Place_Notes1', models.TextField()),
            ],
            options={
                'verbose_name': 'Places',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.AddField(
            model_name='objects_places_reason',
            name='Place_Name',
            field=models.ForeignKey(to='Senufo_App.Places'),
        ),
        migrations.AddField(
            model_name='images',
            name='Objects_ID_No1',
            field=models.ForeignKey(related_name='ImageObject1', to='Senufo_App.Object_Records'),
        ),
        migrations.AddField(
            model_name='images',
            name='Objects_ID_No2',
            field=models.ForeignKey(related_name='ImageObject2', to='Senufo_App.Object_Records'),
        ),
        migrations.AddField(
            model_name='images',
            name='Objects_ID_No3',
            field=models.ForeignKey(related_name='ImageObject3', to='Senufo_App.Object_Records'),
        ),
    ]
