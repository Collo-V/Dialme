from django.urls import path
from django.conf.urls import url,include
from . import views

app_name="users"

urlpatterns=[
    url(r'^registration/',views.registration,name='registration'),
    url(r'^login/',views.signin,name="login"),
    url(r'^logout/$',views.signout,name="logout")
]