# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Senufo_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work_records',
            name='Work_Creation_date_numeric',
        ),
        migrations.AddField(
            model_name='work_records',
            name='By_date',
            field=models.IntegerField(help_text=b'Enter a year', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='work_records',
            name='End_date',
            field=models.IntegerField(help_text=b'Enter a year', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='work_records',
            name='Not_after_date',
            field=models.IntegerField(help_text=b'Enter a year', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='work_records',
            name='Start_date',
            field=models.IntegerField(help_text=b'Enter a year', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='work_records',
            name='Work_Creation_date',
            field=models.CharField(help_text=b'Non-numeric dates, day and month information', max_length=45, null=True, verbose_name=b'Date information', blank=True),
        ),
    ]
