from django.contrib import admin
from .models import Data, Sensor, Appartement, Building
# Register your models here.


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['date','humidity','temperature','sensor']
    fields = ['date','humidity','temperature','sensor']
    list_filter = ['date','sensor']


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["key","description","appartement","is_outdoor","created_date","last_modified_date"]
    fields = ["key","description","appartement","is_outdoor"]
    # fields = ["Security Key","Description","Appartement",("Created Date","Last Modified")]
    list_filter = ['appartement','created_date','last_modified_date']

class SensorInline(admin.TabularInline):
    model = Sensor
    extra = 1
    def has_change_permission(self,request,obj=None):
        return False


@admin.register(Appartement)
class AppartementAdmin(admin.ModelAdmin):
    list_display = ["name","field_1","building","created_date","last_modified_date"]
    fields = ["name",("field_1","building")]
    #fields = ["Owner Name",("House Name","Building"),("Created Date","Last Modified")]
    list_filter = ['building','created_date','last_modified_date']
    inlines = [SensorInline]

class AppartementInline(admin.TabularInline):
    model = Appartement
    extra = 1
    def has_change_permission(self,request, obj=None):
        return False


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['field_2','town','state','description']
    fields = ['building_name','field_2',('town','state'),'description','pin_code','latitude','longitude','landmark']
    list_filter = ["state"]
    inlines = [AppartementInline]
