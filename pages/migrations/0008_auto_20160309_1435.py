# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-09 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_event_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='serial',
            field=models.CharField(default='00:00:00:00:00:00:00', max_length=20),
        ),
    ]
