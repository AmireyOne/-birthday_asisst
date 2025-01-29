
from django.urls import path 
from . import views

urlpatterns = [
    path('reminder_page', views.reminder_page , name="صفحه یاداور" ),
    path('SaveRemind', views.SaveRemind , name="ثبت یاداور" ),
    path('editRemind', views.editremind , name="ثبت یاداور" ),
    path('deleteRemind', views.deleteremind , name="ثبت یاداور" ),
    
]