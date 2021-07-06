from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Statement(models.Model):
    code=models.CharField(max_length=10,primary_key=True)
    user_num=models.CharField(max_length=10)
    transaction=models.CharField(max_length=15)
    amount=models.FloatField()
    trans_cost=models.FloatField()
    agent=models.CharField(max_length=10,null=True)
    recipient=models.CharField(max_length=10,null=True)
    paybill=models.CharField(max_length=10,null=True)
    account=models.CharField(max_length=10,null=True)
    trans_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.user_num},{self.code}"

