# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 04:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20171109_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 23, 58, 47, 675006)),
        ),
    ]