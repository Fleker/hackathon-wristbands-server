from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import MLHOAuth2Provider

urlpatterns = default_urlpatterns(MLHOAuth2Provider)
