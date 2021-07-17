from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Data, Sensor, Apartment, Building
from django.utils import timezone
from django.urls import reverse
import json
import collections
from rest_framework import viewsets
from esp8266.serializers import DataSerializer
from esp8266.forms import DateForm, DataFilterForm
from django.views import generic
from itertools import groupby
# Create your views here.


@csrf_exempt
def store(request):
    recieved_json = json.loads(request.body)
    try:
        sensor = Sensor.objects.filter(key__exact=recieved_json['secretkey'])[0]
    except:
        return JsonResponse({'message': "wrong key or sensor is not registered", 'time': 1000000})
    if recieved_json['ERROR_IN_MEASUREMENT']:
        return JsonResponse({'message': "Error in value hence not recorded"})
    if recieved_json['FIRST']:
        a = timezone.localtime()
        return JsonResponse({'time': (29 - a.minute % 30) * 60 + (90 - a.second),
                            'message': "Reading will be recorded next time, now time is "+str(a)})
    temp = recieved_json['temp']
    humid = recieved_json['humidity']
    value = Data(temperature=temp, humidity=humid,
                 date=timezone.localtime(value=timezone.now()), sensor=sensor)
    value.save()
    return JsonResponse({'message': str(value)})


class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows data to be viewed or edited.
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer


def graph_per_day(request, pk):
    if not request.GET:
        form = DateForm()
    else:
        form = DateForm(request.GET)
    sensor = Sensor.objects.get(pk=pk)
    data = Data.objects.filter(sensor__exact=sensor)
    values = data.filter(date__date=form['date'].value())
    return render(request, 'esp8266/graph_per_day.html', {'form': form, 'values': values, 'count': len(values), "sensor": sensor})


def graph_max_min(request, pk):
    """
    The filtered data based on form input with minimum and maximum of temp/humidity
    """
    if not request.GET:
        form = DataFilterForm()
    else:
        form = DataFilterForm(request.GET)
    sensor = Sensor.objects.get(pk=pk)
    datas = Data.objects.filter(sensor__exact=sensor)
    if form['filter'].value() == 'mh':
        values = datas.filter(date__month=timezone.localdate().month)
    elif form['filter'].value() == 'yr':
        values = datas.filter(date__year=timezone.localdate().year)
    else:
        values = datas.filter(date__week=timezone.localdate().isocalendar()[1])
    if form['reading'].value() == '1':
        b = {(timezone.localdate(x.date), x.temperature) for x in values}
    else:
        b = {(timezone.localdate(x.date), x.humidity) for x in values}
    b = sorted(list(b))
    max_values = (max(list(group)) for key, group in groupby(b, key=lambda x: x[0]))
    min_values = (min(list(group)) for key, group in groupby(b, key=lambda x: x[0]))
    combined_values = zip(max_values, min_values)
    reading = collections.namedtuple('Reading', ['date', 'max_reading', 'min_reading'])
    values = [reading(x[0][0], x[0][1], x[1][1]) for x in combined_values]
    return render(request, 'esp8266/graph_max_min.html', {"form": form, "values": values, 'sensor': sensor})


class SensorDetailView(generic.DetailView):
    model = Sensor


class ApartmentDetailView(generic.DetailView):
    model = Apartment


class BuildingDetailView(generic.DetailView):
    model = Building


def index(request):
    buildings = Building.objects.all()
    num_buildings = buildings.count()
    num_apartments = Apartment.objects.all().count()
    num_sensors = Sensor.objects.all().count()
    num_datas = Data.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {"buildings": buildings,
               "num_datas": num_datas,
               "num_sensors": num_sensors,
               "num_apartments": num_apartments,
               "num_buildings": num_buildings,
               "num_visits": num_visits,
               }
    return render(request, 'index.html', context)
