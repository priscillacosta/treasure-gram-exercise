# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20171021_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='media'),
        ),
    ]