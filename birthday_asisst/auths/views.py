from django.shortcuts import render
from .forms import Login_form , Singup_form
from django.contrib.auth import authenticate , login 
from django.contrib.auth.models import User
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse
import secrets
import http.client
import json
from main_page.models import Information
from .models import Otp

# Create your views here.


# تابع رندر کردن صفحه ورود و ثبت نام

def Login_SingUp (request):
    form_login=Login_form()
    form_singup=Singup_form()
    return render(request=request , template_name="Login_singin.html" , context={"form_login" : form_login , "form_singup" : form_singup})

# تابع رندر کردن صفحه برای ارسال کد

def forget_password (request):
   
    return render(request=request , template_name="forget_password.html" )


# تابع رندر کردن صفحه برای اپدبت رمز عبور

def pass_edit (request):
    otp = request.POST.get("code")
    passes = request.POST.get("pass")
    pass_again = request.POST.get("pass_again")
    phone = request.session.get('phone_number')

    user = Information.objects.get(Phone = phone)
    users_id = user.user_id

    user_otp = Otp.objects.filter(phone = phone).first()

    if otp == user_otp.otp :
        if passes == pass_again :
            
            user_person = User.objects.filter(id = users_id).first()
            user_person.set_password(passes)
            user_person.save()
            user_otp.delete()
            return HttpResponse("true")

        else:
            user_otp.delete()
            return HttpResponse("wrong_pass")
    else:
        user_otp.delete()
        return HttpResponse("wrong_code")





def send_code (request):

    phone = request.POST.get("phone")

    exsist_phone = Information.objects.filter(Phone = phone).exists()
    if exsist_phone == True :

        random_number = secrets.randbelow(89999) + 10000
        message = f"کد تایید شما : {random_number} "
        resualt = send_sms(message , phone)
        response_dict = json.loads(resualt)
        status = response_dict["status"]

    
        if status == 1 :
            new_Otp = Otp(phone = phone , otp = random_number)
            new_Otp.save()
            request.session['phone_number'] = phone
            return HttpResponse("true")
        else :
            return HttpResponse("not_send_code")
    else :
        return HttpResponse("not_valid")   




def send_sms( message , phone):
    conn = http.client.HTTPSConnection("api.sms.ir")
    payload = json.dumps({
        "lineNumber": 30007487130754,
        "messageTexts": [
          message,  
        ],
        "mobiles": [
          phone,
        ],
        "senddatetime": None
      })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'X-API-KEY': 'YtEKfmrrr5Fxpyl8CQYX8nqWaKDYWMD24SSnsq0eXNSVRiNZ'
      }
    conn.request("POST", "/v1/send/likeToLike", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return(data.decode("utf-8"))


# تابع چک کردن وجود یوزر برای ورود  

def Chek_Login (request):
    form_login=Login_form(request.POST)
    if form_login.is_valid():
        username=form_login.data["Username"]
        password=form_login.data["Password"]
        user=authenticate(request=request , username=username , password=password)
        if user is not None :
            login(request , user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("no")


# تابع افزودن کاربر

def SingUp_User (request):
    if request.method == "POST":
        form_singup=Singup_form(request.POST)
        exist_username = User.objects.filter(username=form_singup.data["Username"]).all()
        if len(exist_username) > 0 :
            return HttpResponse("exist")
        elif form_singup.data["Password"] != form_singup.data["Password_again"] :
            return HttpResponse("repetedly")
        else:
            user = User.objects.create_user(username=form_singup.data["Username"] , email="" , password=form_singup.data["Password"] )
            user.first_name=form_singup.data["Full_Name"]
            user.save()
            logins=Chek_Login(request)
            return logins
        
    else:
        return HttpResponse("warning")    
