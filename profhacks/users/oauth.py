from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class MLHAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):

        if request.user.is_authenticated():
            return settings.LOGIN_REDIRECT_URL.format(
                username=request.user.username)
        else:
            return "/"