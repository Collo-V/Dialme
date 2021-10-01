from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

app_name="services"
urlpatterns = [
   url(r'^$',views.services,name="homepage"),
]