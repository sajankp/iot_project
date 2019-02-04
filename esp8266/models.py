from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
import datetime

class Data(models.Model):
    value = models.CharField(max_length = 64)
    #date = models.DateTimeField(auto_now_add = True)
    #date = models.DateTimeField()
    date = models.DateTimeField()
    def __str__(self):
        date = datetime.datetime.strftime(self.date,"%D - %T")
        return f"{self.value} recorded on {date}"
