# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = AuthUserAdmin.fieldsets + (
        ('Major League Hacking Data',
                {'fields': 
                    ('graduation', 
                     'major', 
                     'shirt_size', 
                     'dietary_restrictions', 
                     'special_needs', 
                     'date_of_birth', 
                     'gender', 
                     'phone_number', 
                     'school',),
                 }
         ),
        ('Custom Data',
                {'fields':
                    ('resume',
                     'teammates',
                     'journalism',
                     'smart_buildings',
                     'quantified_self',
                     'first_hackathon',
                     'sms_notifications',),
                }
         ),
        ('Internal Use',
                {'fields':
                    ('status',),
                }
         )
    )