from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)
import requests

from .provider import MLHOAuth2Provider
from allauth.socialaccount import app_settings

class MLHOAuth2Adapter(OAuth2Adapter):
    provider_id = MLHOAuth2Provider.id
    access_token_url = 'https://my.mlh.io/oauth/token'
    authorize_url = 'https://my.mlh.io/oauth/authorize'
    profile_url = 'https://my.mlh.io/api/v1/user'
    
    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token})
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)

oauth2_login = OAuth2LoginView.adapter_view(MLHOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(MLHOAuth2Adapter)
