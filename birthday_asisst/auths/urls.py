
from django.urls import path
from . import views

urlpatterns = [

    path('', views.Login_SingUp , name="ورود و ثبت نام"),
    path('ChekLogin', views.Chek_Login , name="بررسی ورود"),
    path('Singup_User', views.SingUp_User , name=" ثبت نام "),
    path('forget_password', views.forget_password , name="فراموشی رمز عبور"),
    path('pass_edit', views.pass_edit , name="تغییر رمز عبور"),
    path('sendcode', views.send_code , name="ارسال کد فراموشی رمز عبور"),
]
