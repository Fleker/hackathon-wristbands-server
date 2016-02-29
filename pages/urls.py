from django.conf.urls import url
from pages import views

urlpatterns = [
    url(r'^post/registration/$', views.registration),
    url(r'^get/registration/all/$', views.list_registration),
    url(r'^get/event/all/$', views.list_events),
    url(r'^post/event/$', views.post_event),
]
