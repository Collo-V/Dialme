from django.db import models


class Notifications(models.Model):
    user_num = models.CharField(max_length=10)
    notif=models.CharField(max_length=150)
    ifread=models.IntegerField()


# Create your models here.
