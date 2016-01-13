from django.shortcuts import render, redirect
from django.conf import settings
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import InfoForm, ResumeUploadForm

# Create your views here.

@login_required
def hacker_page(request):
    user = request.user
    info_form = InfoForm(initial={
            'teammates': user.teammates,
            'journalism': '1' if user.journalism else '2',
            'smart_buildings': '1' if user.smart_buildings else '2',
            'quantified_self': '1' if user.quantified_self else '2',
            'first_hackathon': '1' if user.first_hackathon else '2',
            'sms_notifications': '1' if user.sms_notifications else '2',})
    return render(request, "hacker_page.html", {
            'resume_upload': ResumeUploadForm,
            'info_form': info_form,
            'registration_status': 'registration_open',
            'first_name': user.first_name,
            'status': user.status,
            'deadline': '10',
            'resume_exists': 'False',
    })

@login_required
def upload_resume(request):
    user = request.user
    if request.method == 'POST':
        user.resume = request.POST.get('resume')
    import pdb; pdb.set_trace()
    user.save()
    return HttpResponse

@login_required
def update_info(request):
    user = request.user
    if request.method == 'POST':
        if request.POST.get('teammates'):
            user.teammates = request.POST.get('teammates')
        if request.POST.get('journalism'):
            if request.POST.get('journalism') == '1':
                user.journalism = True
            else:
                user.journalism = False
        if request.POST.get('smart_buildings'):
            if request.POST.get('smart_buildings') == '1':
                user.smart_buildings = True
            else:
                user.smart_buildings = False
        if request.POST.get('quantified_self'):
            if request.POST.get('quantified_self') == '1':
                user.quantified_self = True
            else:
                user.quantified_self = False
        if request.POST.get('first_hackathon'):
            if request.POST.get('first_hackathon') == '1':
                user.first_hackathon = True
            else:
                user.first_hackathon = False
        if request.POST.get('sms_notifications'):
            if request.POST.get('sms_notifications') == '1':
                user.sms_notifications = True
            else:
                user.sms_notifications = False
    user.save()
    return redirect('users:you')