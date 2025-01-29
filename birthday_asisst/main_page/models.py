from django.db import models
from django.contrib.auth.models import User
from django_jalali.db.models import jDateField

# from django_jalali.db import models as jmodels

# Create your models here.

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    Full_name=models.CharField(max_length=300 , verbose_name="نام کامل")
    Comment_message=models.TextField(max_length=2000 , verbose_name="متن نظر")
    Phone=models.TextField(max_length=15 , null=True , verbose_name="شماره تلفن")
    Approved = models.BooleanField(default=False , verbose_name="حالت نمایش")
    Created_at = models.DateField( verbose_name="نوشته شده در")

    # def __str__(self):
    #     return f"{self.Full_name} | {self.Comment_message} | {self.Approved}"

    class Meta :
        verbose_name="نظر"
        verbose_name_plural="نظرات"



class Information(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="کاربر")
    Phone=models.CharField(max_length=15 , verbose_name="شماره تلفن")
    Email=models.EmailField(max_length=200 , verbose_name="ایمیل")
    Birthday = models.DateField(verbose_name="تاریخ تولد" )
    class Meta :
        verbose_name="اطلاعات"
        verbose_name_plural="اطلاعات ها"
       

class Adress(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="کاربر")
    adress=models.TextField(max_length=3000 , verbose_name="آدرس")
    class Meta :
        verbose_name="آدرس"
        verbose_name_plural="آدرس ها"


class Manage_Contact(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="کاربر")
    Title = models.CharField(max_length=300 , verbose_name="موضوع")
    Caption = models.TextField(verbose_name="متن")
    Created_at = models.DateField(auto_now_add=True , verbose_name="نوشته شده در ")

    class Meta :
        verbose_name="پیام مدیریت"
        verbose_name_plural="پیام های مدیریت"