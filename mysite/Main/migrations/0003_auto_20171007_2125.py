# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 21:25
from __future__ import unicode_literals

import Main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20171005_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=Main.models.upload_location),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=Main.models.upload_location),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to=Main.models.upload_location),
        ),
    ]
