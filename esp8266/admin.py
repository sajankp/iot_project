from django.contrib import admin
from .models import Data
# Register your models here.

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['date','humidity','temperature']
    fields = ['Date','Humidity','Temperature']
    list_filter = ['date']
