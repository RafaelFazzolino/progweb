# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.ImageField(blank=True, height_field='50', null=True, upload_to='trips/images/', verbose_name='Imagem', width_field='50'),
        ),
    ]
