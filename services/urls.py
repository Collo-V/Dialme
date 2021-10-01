from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from . import mpesa

app_name="services"
urlpatterns = [
   url(r'^$',views.services,name="homepage"),
   url(r'^topup$',views.TopUp,name="topup"),
   url(r'^bundles$',views.Bundles,name="bundles"),
   url(r'^okoa',views.Okoa,name='okoa'),
   url(r'^sms',views.SMS,name='sms'),
   url(r'^mpesa$',views.Mpesa,name="mpesa"),
   url(r'^mpesa/send-money',mpesa.sendmoney,name="sendmoney"),
   url(r'^mpesa/withdraw',mpesa.withdraw,name="withdraw"),
   url(r'^mpesa/paybill',mpesa.paybill,name="paybill"),
   url(r'^mpesa/airtime',mpesa.airtime,name="airtime")
]