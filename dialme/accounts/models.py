from django.db import models
from django.db.models.fields.related import OneToOneField
import sys,os

sys.path.append("C:\\Users\\Collins\\desktop\\collo v\\python\\onlineussd")
sys.path.append("..")
# Create your models here.
from users.models import Regusers
class Accounts(models.Model):
    user_num = models.OneToOneField(Regusers,primary_key=True,on_delete=models.CASCADE,related_name="accounts")
    airtime = models.FloatField(default=0)
    bundles = models.FloatField(default=0)
    bonga =models.FloatField(default=0)
    sms = models.FloatField(default=0)
    okoa_limit = models.FloatField(default=0)
    okoa_taken = models.FloatField(default=0)
    okoa_bal = models.FloatField(default=0)
    mpesa = models.FloatField(default=0)


    def __str__(self):
        return f"{self.user_num}"


class Agent(models.Model):
    agentnum=models.CharField(max_length=6,primary_key=True)
    agentname=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.agentnum} {self.agentname}"


class AgentAcount(models.Model):
    agentnum=models.OneToOneField(Agent,primary_key=True,on_delete=models.CASCADE,related_name="agent")
    agentfloat=models.FloatField()
    
    