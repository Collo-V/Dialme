from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Regusers

admin.site.register(Regusers)