from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from .models import Data
from django.utils import timezone
from django.urls import reverse
import json

# Create your views here.
@csrf_exempt
def store(request):
    a = json.loads(request.body)['value']
    value = Data(value = a,date = timezone.localtime(timezone.now()))
    value.save()
    return HttpResponse(f'Done and recieved {value.value} at {value.date}')
    '''return HttpResponseRedirect(reverse("index"))
    values = Data.objects.all()
    context = {"values" : values}
    return render(request,"esp8266/values.html",context)'''

def index(request):
    values = Data.objects.all()
    context = {"values" : values}
    return render(request,"esp8266/values.html",context)
