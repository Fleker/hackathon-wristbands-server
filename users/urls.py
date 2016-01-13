# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^you/$',
        view=views.hacker_page,
        name='you'
    ),
    url(
        regex=r'^you/update_info/$',
        view=views.update_info,
        name='you_update_info'
    ),
]
