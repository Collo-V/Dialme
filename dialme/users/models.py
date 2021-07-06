
from django.db import models
from django.db.models.base import Model
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager
import datetime
#

class Regusers(models.Model):
    user_num=models.CharField(max_length=10,primary_key=True,)
    first_name=models.CharField(max_length=15,)
    last_name=models.CharField(max_length=15,)
    password=models.CharField(max_length=8,)    
    mpin=models.CharField(max_length=4,)
    regdate=models.DateTimeField(auto_now_add=True,)
   
    
    def __str__(self):
        return f"{self.user_num},{self.first_name} {self.last_name}"
# Create your models here.
