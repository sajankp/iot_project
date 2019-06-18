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
    path('', views.index, name = "index"),
    path('chart', views.chart, name = "chart"),
    path('test2', views.DataListView.as_view(), name="test2"),
    path('test', views.test, name="test"),
    path('test3',views.test3,name="test3"),
    path('sensor/<int:pk>', views.SensorDetailView.as_view(), name='sensor-detail'),
    path('appartement/<int:pk>', views.AppartementDetailView.as_view(), name='appartement-detail'),
    path('building/<int:pk>', views.BuildingDetailView.as_view(), name='building-detail'),
    path('buildings',views.BuildingListView.as_view(), name='building-list'),
]
