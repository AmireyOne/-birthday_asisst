from django.db import models



class Otp(models.Model):
    id = models.AutoField(primary_key= True)
    phone = models.CharField(max_length= 12 , verbose_name="تلفن کاربر")
    otp = models.CharField(max_length=6 , verbose_name="کد تایید")
