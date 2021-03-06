"""sirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/weather/(?P<query>\+\w+)/', views.weather, name='weather'),
    url(r'^api/getweather/', views.getweather, name='getweather'),
    url(r'^api/soil/', views.soil, name='soil'),
    url(r'^api/jsonz/', views.jsonz, name='jsonz'),
    url(r'^api/test/(?P<query>\w+)/', views.test, name='test'),
    url(r'^api/watson/', views.main, name='watson'),
]
