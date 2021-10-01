from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self,user_num,fname,lname,password,mpin,**extra_fields):
        if not user_num:raise ValueError(_("The number must be set"))
        user=self.model(user_num=user_num,fname=fname,**extra_fields)
        user.set_password(password)
        user.save()

    def create_superuser(self,user_num,fname,lname,password,mpin,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_super",True)
        extra_fields.setdefault("is_active",True)
        return self.create_user(user_num, fname, lname, password, mpin, **extra_fields)


    pass