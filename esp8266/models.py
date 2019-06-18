from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator
from uuid import uuid4
# Create your models here.

class Data(models.Model):
    date = models.DateTimeField(default = timezone.now)
    temperature = models.PositiveSmallIntegerField(validators=[MaxValueValidator(150)],default = 0)
    humidity = models.PositiveSmallIntegerField(validators=[MaxValueValidator(150)],default = 0)
    sensor = models.ForeignKey('Sensor',on_delete=models.SET_NULL, null=True)

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
        date = datetime.strftime(self.date,"%D - %T")
        return f"Temperature: {self.temperature} and Humidity: {self.humidity} recorded on {date}"

    class Meta:
        ordering = ['-date']


class Sensor(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    key = models.UUIDField(
        default=uuid4,
        help_text="Unique ID for security and identification purposes")
    description = models.TextField(
        max_length=100,
        help_text="Enter a description on sensor location",
        null = True,)
    is_outdoor = models.BooleanField(
        choices=[(True,"Outdoor"),(False,"Indoor")],
        default=False,
        help_text="The location of sensor",
        )
    appartment = models.ForeignKey('Appartment', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"sensor located at {self.description}"

    class Meta:
        ordering = ['-created_date']

class Appartment(models.Model):
    """represent many adresses within one building"""
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(
        max_length=200,
        help_text="Full Name",)
    mobile_number=models.BigIntegerField(
        help_text="Mobile number of owner",)
    field_1=models.CharField(
            max_length=200,
            help_text="Flat, House no., Building, Company, Apartment :",)
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.field_1}'
    class Meta:
        ordering = ['building','field_1']

class Building(models.Model):
    STATES=[('AN', 'Andaman and Nicobar Islands'),
            ('AP', 'Andhra Pradesh'),
            ('AR', 'Arunachal Pradesh'),
            ('AS', 'Assam'),
            ('BR', 'Bihar'),
            ('CH', 'Chandigarh'),
            ('CT', 'Chhattisgarh'),
            ('DN', 'Dadra and Nagar Haveli'),
            ('DD', 'Daman and Diu'),
            ('DL', 'Delhi'),
            ('GA', 'Goa'),
            ('GJ', 'Gujarat'),
            ('HR', 'Haryana'),
            ('HP', 'Himachal Pradesh'),
            ('JK', 'Jammu and Kashmir'),
            ('JH', 'Jharkhand'),
            ('KA', 'Karnataka'),
            ('KL', 'Kerala'),
            ('LD', 'Lakshadweep'),
            ('MP', 'Madhya Pradesh'),
            ('MH', 'Maharashtra'),
            ('MN', 'Manipur'),
            ('ML', 'Meghalaya'),
            ('MZ', 'Mizoram'),
            ('NL', 'Nagaland'),
            ('OR', 'Odisha, Orissa'),
            ('PY', 'Puducherry'),
            ('PB', 'Punjab'),
            ('RJ', 'Rajasthan'),
            ('TN', 'Tamil Nadu'),
            ('SK', 'Sikkim'),
            ('TG', 'Telangana'),
            ('TR', 'Tripura'),
            ('UP', 'Uttar Pradesh'),
            ('UT', 'Uttarakhand,Uttaranchal'),
            ('WB', 'West Bengal'),]
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    description = models.TextField(
        max_length=200,
        help_text="Enter a description about the building",
        null=True,)
    building_name = models.CharField(
        max_length=100,
        help_text="Building name",)
    field_2=models.CharField(
        max_length=100,
        help_text="Area, Colony, Street, Sector, Village: ",)
    landmark=models.CharField(
        max_length=100,
        help_text="Landmark e.g. near apollo hospital: ",)
    town=models.CharField(
        max_length=100,
        help_text="Town/City: ",)
    state=models.CharField(
        max_length=2,
        choices=STATES,
        help_text="State",)
    pincode=models.IntegerField(validators=[MaxValueValidator(999999)],default = 676121)
    latitude=models.DecimalField(max_digits=9, decimal_places=7, null=True)
    longitude=models.DecimalField(max_digits=10, decimal_places=7, null=True)
    def __str__(self):
        return f"{self.building_name} in {self.town}"
