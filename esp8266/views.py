from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Data
from django.utils import timezone
from django.urls import reverse
import json,collections
import datetime
from rest_framework import viewsets
from esp8266.serializers import DataSerializer
from esp8266.forms import DateForm,DataFilterForm
from django.views import generic
from itertools import groupby
# Create your views here.


@csrf_exempt
def store(request):
    if json.loads(request.body)['ERROR_IN_MEASUREMENT'] == True:
        return JsonResponse({'message':"Error in value hence not recorded"})
    if json.loads(request.body)['FIRST'] == True:
        a=timezone.now()
        return JsonResponse({'time':(14-a.minute%15)*60+(90-a.second),
                            'message':"Reading will be recorded next time, now time is "+str(a)})
    temp = json.loads(request.body)['temp']
    humid = json.loads(request.body)['humidity']
    value = Data(temperature=temp, humidity=humid,
                 date=timezone.localtime(value=timezone.now()))
    value.save()
    return JsonResponse({'message':str(value)})


def index(request):
    values = Data.objects.all().order_by('date')
    context = {"values": values}
    return render(request, "esp8266/values.html", context)

def chart(request):
    '''
    # Another way of implementing
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
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataListView(generic.ListView):
    model = Data
    #paginate_by = 50


def test(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DateForm(request.POST)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = DateForm()
    values = Data.objects.filter(date__date=form['date'].value())
    return render(request, 'esp8266/test.html', {'form': form, 'values':values, 'count':len(values)})

def test3(request):
    """
    The filtered data based on form input with minimum and maximum of temp/humidity
    """
    if request.method == "POST":
        form = DataFilterForm(request.POST)
    else:
        form = DataFilterForm()
    if form['filter'].value()=='mh':
        values=Data.objects.filter(date__month=timezone.localdate().month)
    elif form['filter'].value()=='yr':
        values=Data.objects.filter(date__year=timezone.localdate().year)
    else:
        values=Data.objects.filter(date__week=timezone.localdate().isocalendar()[1])
    print(form['reading'].value(),type(form['reading'].value()))
    if form['reading'].value()==1 or form['reading'].value()=='1':
        b={(x.date.date(),x.temperature) for x in values}
    else:
        b={(x.date.date(),x.humidity) for x in values}
    b=sorted(list(b))
    max_values = (max(list(group)) for key, group in groupby(b,key=lambda x:x[0]))
    min_values = (min(list(group)) for key, group in groupby(b,key=lambda x:x[0]))
    combined_values = zip(max_values,min_values)
    reading=collections.namedtuple('Reading',['date','max_reading','min_reading'])
    values = [reading(x[0][0],x[0][1],x[1][1]) for x in combined_values]
    return render(request,'esp8266/test3.html',{"form":form,"values":values})
