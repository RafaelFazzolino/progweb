# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_trip_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='slug',
            field=models.SlugField(),
        ),
    ]