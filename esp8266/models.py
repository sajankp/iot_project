from datetime import datetime
from uuid import uuid4

from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
from esp8266 import config


class CommonBaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    objects = models.manager

    class Meta:
        abstract = True


class CommonLargeDataBaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    objects = models.manager

    class Meta:
        abstract = True


class Data(CommonLargeDataBaseModel):
    date = models.DateTimeField(default=timezone.now)
    temperature = models.PositiveSmallIntegerField(validators=[MaxValueValidator(150)], default=0)
    humidity = models.PositiveSmallIntegerField(validators=[MaxValueValidator(150)], default=0)
    sensor = models.ForeignKey('Sensor', on_delete=models.SET_NULL, null=True)

    @property
    def month(self):
        return self.date.month

    @property
    def year(self):
        return self.date.year

    @property
    def day(self):
        return self.date.day

    def __str__(self):
        date = datetime.strftime(self.date, "%D - %T")
        return f"Temperature: {self.temperature} and Humidity: {self.humidity} recorded on {date}"

    class Meta:
        ordering = ['-date']


class Sensor(CommonLargeDataBaseModel):
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    key = models.UUIDField(
        default=uuid4,
        help_text="Unique ID for security and identification purposes")
    description = models.TextField(
        max_length=100,
        help_text="Enter a description on sensor location",
        null=True, )
    is_outdoor = models.BooleanField(
        choices=[(True, "Outdoor"), (False, "Indoor")],
        default=False,
        help_text="The location of sensor",
    )
    apartment = models.ForeignKey('Apartment', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Sensor located at {self.description}"

    def get_absolute_url(self):
        """Return the url to access detail record for each Sensor"""
        return reverse('sensor-detail', args=[self.id])

    class Meta:
        ordering = ['-created_date']


class Apartment(CommonBaseModel):
    """represent many addresses within one building"""
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(
        max_length=200,
        help_text="Full Name", )
    mobile_number = models.BigIntegerField(
        help_text="Mobile number of owner", )
    field_1 = models.CharField(
        max_length=200,
        help_text="Flat, House no., Building, Company, Apartment :", )
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.field_1}'

    def get_absolute_url(self):
        """Return the url to access detail record for each Apartment"""
        return reverse('apartment-detail', args=[self.id])

    class Meta:
        ordering = ['building', 'field_1']


class Building(CommonBaseModel):
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    description = models.TextField(
        max_length=200,
        help_text="Enter a description about the building",
        null=True, )
    building_name = models.CharField(
        max_length=100,
        help_text="Building name", )
    field_2 = models.CharField(
        max_length=100,
        help_text="Area, Colony, Street, Sector, Village: ", )
    landmark = models.CharField(
        max_length=100,
        help_text="Landmark e.g. near apollo hospital: ", )
    town = models.CharField(
        max_length=100,
        help_text="Town/City: ", )
    state = models.CharField(
        max_length=2,
        choices=config.STATES,
        help_text="State", )
    pin_code = models.IntegerField(validators=[RegexValidator(r'[1-9]{1}[0-9]{2}\\s{0, 1}[0-9]{3}$')], default=676121)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)

    def __str__(self):
        return f"{self.building_name} in {self.town}"

    def get_absolute_url(self):
        """Return the url to access detail record for each Building"""
        return reverse('building-detail', args=[self.id])

    class Meta:
        ordering = ['state', 'town', 'created_date']
