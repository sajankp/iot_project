from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from .models import Data
from django.utils import timezone
from django.urls import reverse
import json
import datetime
from rest_framework import viewsets
from esp8266.serializers import DataSerializer
# Create your views here.


@csrf_exempt
def store(request):
    if json.loads(request.body)['ERROR_IN_MEASUREMENT'] == True:
        return HttpResponse("Error in value hence not recorded")
    temp = json.loads(request.body)['temp']
    humid = json.loads(request.body)['humidity']
    value = Data(temperature=temp, humidity=humid,
                 date=timezone.localtime(value=timezone.now()))
    value.save()
    return HttpResponse(value)


def index(request):
    values = Data.objects.all().order_by('date')
    context = {"values": values}
    return render(request, "esp8266/values.html", context)


def chart(request):
    '''
    Another way of implementing
    today = datetime.date.today()
    today_with_time = datetime.datetime(
        year=today.year,
        month=today.month,
        day=today.day,
        tzinfo = timezone.utc,
    )
    values = Data.objects.filter(date__gte=today_with_time-datetime.timedelta(seconds=60*60*5.5))
    '''
    values = Data.objects.filter(date__gte=datetime.date.today())
    #When USE_TZ is True, fields are converted to the current time zone before filtering.
    context = {"values": values}
    return render(request, "esp8266/chart.html", context)


class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows data to be viewed or edited.
    """
    queryset = Data.objects.all().order_by('date')
    serializer_class = DataSerializer
