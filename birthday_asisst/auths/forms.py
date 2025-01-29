from django import forms

class Login_form (forms.Form):

    def __init__(self , *args , **kwargs):
        super(Login_form , self).__init__(*args , **kwargs)
        for item in Login_form.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

    Username=forms.CharField(  required=True ,widget=forms.TextInput(attrs={'placeholder': 'نام کاربری یا ایمیل خود را وارد کنید'}  ))
    Password=forms.CharField(  required=True ,widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد کنید '}  ))




class Singup_form (forms.Form):

    def __init__(self , *args , **kwargs):
        super(Singup_form , self).__init__(*args , **kwargs)
        for item in Singup_form.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

    Full_Name=forms.CharField(max_length=200 , required=True ,widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید'}  ) )
    Username=forms.CharField(  required=True ,widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}  ))
    Password=forms.CharField(  required=True ,widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد کنید '}  ))
    Password_again=forms.CharField(  required=True ,widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را تکرار کنید '}  ))