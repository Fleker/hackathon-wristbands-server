from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from allauth.account.models import EmailAddress

class MLHOAuth2Account(ProviderAccount):
    pass

class MLHOAuth2Provider(OAuth2Provider):
    id = 'mlh'
    name = 'mlh'
    package = 'mlh'
    account_class = MLHOAuth2Account

    def extract_uid(self, data):
        return data['data']['id']

    def extract_common_fields(self, data):
        
        return dict(email=data['data']['email'],
                    username=data['data']['email'],
                    first_name=data['data']['first_name'],
                    last_name=data['data']['last_name'],
                    graduation=data['data']['graduation'],
                    major=data['data']['major'],
                    shirt_size=data['data']['shirt_size'],
                    dietary_restrictions=data['data']['dietary_restrictions'],
                    special_needs=data['data']['special_needs'],
                    date_of_birth=data['data']['date_of_birth'],
                    gender=data['data']['gender'],
                    phone_number=data['data']['phone_number'],
                    school=data['data']['school']['name'],)
    
    def extract_email_addresses(self, data):
        ret = []
        email = data['data']['email']
        if email:
            ret.append(EmailAddress(email=email,
                                    verified=True,
                                    primary=True))
        return ret

providers.registry.register(MLHOAuth2Provider)
