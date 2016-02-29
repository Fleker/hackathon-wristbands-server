from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True  )


class Event(models.Model):
    row_num = models.AutoField(primary_key=True)
    id = models.ForeignKey('Register', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
