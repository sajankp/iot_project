from django.contrib import admin
from .models import Data, Sensor, Apartment, Building
# Register your models here.


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['date','humidity','temperature','sensor']
    fields = ['date','humidity','temperature','sensor']
    list_filter = ['date','sensor']


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["key","description","apartment","is_outdoor","created_date","last_modified_date"]
    fields = ["key","description","apartment","is_outdoor"]
    list_filter = ['apartment','created_date','last_modified_date']

class SensorInline(admin.TabularInline):
    model = Sensor
    extra = 1
    def has_change_permission(self,request,obj=None):
        return False


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ["name","field_1","building","created_date","last_modified_date"]
    fields = ["name",("field_1","building")]
    #fields = ["Owner Name",("House Name","Building"),("Created Date","Last Modified")]
    list_filter = ['building','created_date','last_modified_date']
    inlines = [SensorInline]

class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1
    def has_change_permission(self,request, obj=None):
        return False


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['field_2','town','state','description']
    fields = ['building_name','field_2',('town','state'),'description','pin_code','latitude','longitude','landmark']
    list_filter = ["state"]
    inlines = [ApartmentInline]
