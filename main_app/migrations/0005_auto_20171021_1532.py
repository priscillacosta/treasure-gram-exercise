# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20171021_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='tresure_images'),
        ),
    ]