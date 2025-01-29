from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_page , name="صفحه اصلی"),
    path('panel', views.panel , name="پنل کاربری"),
    path('SaveComment', views.Save_Comment , name="ثبت نظر"),
    path('Logout', views.Logout , name="خروج از حساب"),
    path('SaveInformation', views.Save_information , name="ثبت اطلاعات کاربری"),
    path('SaveAdress', views.Save_Adress , name="ثبت آدرس"),
    path('SendMessageManagement', views.Save_message , name="ثبت آدرس"),
  
]
