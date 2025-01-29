from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Remind_member(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="کاربر")
    Full_name=models.CharField(max_length=100 , verbose_name="نام یادآور")
    Date_remind=models.DateField( verbose_name="تاریخ تولد")
    Befor_day_remind=models.IntegerField( verbose_name="یادآوری در این تعداد روز قبل")

    class Meta :
        verbose_name="یادآور"
        verbose_name_plural="یادآوری ها"
    