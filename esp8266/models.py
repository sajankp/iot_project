from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
import datetime

class Data(models.Model):
    value = models.CharField(max_length = 64)
    date = models.DateTimeField()

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
        return f"{self.value} recorded on {date}"
