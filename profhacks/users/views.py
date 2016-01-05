from django.shortcuts import render, redirect
from django.conf import settings
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .forms import InfoForm

# Create your views here.

@login_required
def hacker_page(request):
    user = request.user
    return render(request, "hacker_page.html", {
            'info_form': InfoForm,
            'registration_status': 'registration_open',
            'first_name': user.first_name,
            'status': user.status,
            'resume': user.resume,
    })

@login_required
def update_info(request):
    user = request.user
    print(request)
    return redirect('users:you')