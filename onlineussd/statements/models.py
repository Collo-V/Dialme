from django.db import models

class Statements(models.Model):
    user_num = models.CharField(max_length=10)
    statements=models.CharField(max_length=500)
    sdate=models.DateTimeField(auto_now_add=True)


# Create your models here.
