from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from .models import Data
from django.utils import timezone
from django.urls import reverse
#import json
import datetime
from rest_framework import viewsets
from esp8266.serializers import DataSerializer
# Create your views here.

@csrf_exempt
def store(request):
    a = json.loads(request.body)['value']
    value = Data(value = a,date = timezone.localtime(timezone.now()))
    value.save()
    return HttpResponse(f'Done and recieved {value.value} at {value.date}')

def index(request):
    values = Data.objects.all().order_by('date')
    context = {"values" : values}
    return render(request,"esp8266/values.html",context)

def chart(request):
    now_in_timezone = timezone.now()
    one_hour_ago = now_in_timezone - datetime.timedelta(seconds = 60*60)
    values = Data.objects.filter(date__range=[one_hour_ago,now_in_timezone])
    context = {"values" : values}
    return render(request,"esp8266/chart.html",context)

class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows data to be viewed or edited.
    """
    queryset = Data.objects.all().order_by('date')
    serializer_class = DataSerializer
