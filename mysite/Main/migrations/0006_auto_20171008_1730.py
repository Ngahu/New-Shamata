# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 17:30
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20171008_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_meamber',
            name='members_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
    ]
