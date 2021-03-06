# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class User(AbstractUser):
    # MLH Data
    graduation = models.DateField(null=True)
    major = models.CharField(blank=True, max_length=255)
    shirt_size = models.CharField(blank=True, max_length=255)
    dietary_restrictions = models.CharField(blank=True, max_length=255)
    special_needs = models.CharField(null=True, blank=True, max_length=255)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(blank=True, max_length=255)
    phone_number = models.CharField(blank=True, max_length=10)
    school = models.CharField(blank=True, max_length=255)
    
    # Custom Data
    resume = models.FileField(blank=True)
    
    teammates = models.CharField(blank=True, max_length=255)
    journalism = models.BooleanField(default=False)
    smart_buildings = models.BooleanField(default=False)
    quantified_self = models.BooleanField(default=False)
    first_hackathon = models.BooleanField(default=False)
    sms_notifications = models.BooleanField(default=True)
    
    # Internal
    status = models.CharField(default='pending', max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})