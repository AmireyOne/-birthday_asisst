from django import forms
from django_jalali.forms import jDateField
from django_jalali.admin.widgets import AdminjDateWidget




class Comment_main(forms.Form):

    def __init__(self , *args , **kwargs):
        super(Comment_main , self).__init__(*args , **kwargs)
        for item in Comment_main.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

    Full_name=forms.CharField(max_length=200 , required=True ,widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید'}  ) , label="نام و نام خانوادگی")
    Phone=forms.CharField(max_length=15 , required=True ,widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن خود را وارد کنید'}  ) , label="شماره تلفن")
    Message=forms.CharField(  required=True ,widget=forms.Textarea(attrs={'placeholder': 'نظرات خود راجب سایت را بنویسید'}  ) , label="نظر")





    
       
        
   