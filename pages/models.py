from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    serial = models.CharField(max_length=20, unique=True, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
