"""iot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post', views.store, name = 'store'),
    path("",views.index, name = "index"),
    path('building/<int:pk>', views.BuildingDetailView.as_view(), name='building-detail'),
    path('apartment/<int:pk>', views.ApartmentDetailView.as_view(), name='apartment-detail'),
    path('sensor/<int:pk>', views.SensorDetailView.as_view(), name='sensor-detail'),
    path('sensor/<int:pk>/graph1', views.graph_per_day, name="graph_per_day"),
    path('sensor/<int:pk>/graph2',views.graph_max_min,name="graph_max_min"),
    ]
