from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.
import datetime

class Data(models.Model):
    date = models.DateTimeField(default = timezone.now)
    temperature = models.PositiveSmallIntegerField(validators=[MaxValueValidator(150)],default = 0)
    humidity = models.PositiveSmallIntegerField(validators=[MaxValueValidator(150)],default = 0)

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
        date = datetime.datetime.strftime(self.date,"%D - %T")
        return f"Temperature: {self.temperature} and Humidity: {self.humidity} recorded on {date}"
