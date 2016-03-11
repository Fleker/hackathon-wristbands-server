from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from pages.models import Register, Event
from pages.serializers import RegisterSerializer, EventSerializer

# Create your views here.

auth_token = 'prof.hacks.2016*(aF3C-d)'

def home(request):
    return render(request, "index.html", {
            'registration_status': 'registration_closed',
    })

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def registration(request):
    if not request.body:
        return HttpResponse(status=400)

    try:
        register = Register()
    except:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request);
        if (not hasattr(data, 'auth_token') or auth_token != data['auth_token']):
            return HttpResponse(status=401)
        else:
            del data['auth_token']
        serializer = RegisterSerializer(register, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

def list_registration(request):
    if request.method == 'GET':
        register = Register.objects.all()
        serializer = RegisterSerializer(register, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def post_event(request):
    if not request.body:
        return HttpResponse(status=400)

    try:
        event = Event()
    except:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        if (not hasattr(data, 'auth_token') or auth_token != data['auth_token']):
            return HttpResponse(status=401)
        else:
            del data['auth_token']
        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

def list_events(request):
    if request.method == 'GET':
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return JSONResponse(serializer.data)
