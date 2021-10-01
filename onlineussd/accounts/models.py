from django.db import models
from django.db.models.fields.related import OneToOneField
import sys,os

sys.path.append("C:\\Users\\Collins\\desktop\\collo v\\python\\onlineussd")
sys.path.append("..")
# Create your models here.
from regusers.models import Regusers
class Accounts(models.Model):
    user_num = models.OneToOneField(Regusers,primary_key=True,on_delete=models.CASCADE,)
    airtime = models.DecimalField(max_digits=5 ,decimal_places=2,default=0)
    bundles = models.DecimalField(max_digits=5 ,decimal_places=2,default=0)
    bonga =models.DecimalField(max_digits=5 ,decimal_places=2,default=0)
    sms = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    okoa_limit = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    okoa_taken = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    okoa_bal = models.DecimalField(max_digits=5 ,decimal_places=2,default=0)
    mpesa = models.DecimalField(max_digits=6 ,decimal_places=2,default=0)

    
    