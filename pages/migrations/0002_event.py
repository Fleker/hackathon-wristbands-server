# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('row_num', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=255)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Register')),
            ],
        ),
    ]