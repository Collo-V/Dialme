
from django import urls
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   url('admin/', admin.site.urls),
   url(r'^services/',include("services.urls")),
   url(r'^users/',include("users.urls")),
   url(r"^accounts/",include("accounts.urls")),
   url(r'^$',views.homepage),
]

urlpatterns+=staticfiles_urlpatterns()