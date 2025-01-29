from django.shortcuts import render
from main_page.Userauth import Userauths
from django.http import HttpResponseRedirect
from .models import Remind_member
from django.contrib.auth.models import User
from django.http import HttpResponse
import jdatetime
from datetime import date, timedelta , datetime
from main_page.models import Information
import http
import json

# Create your views here.

import jdatetime
from datetime import date

def reminder_page(request):
    user_at = Userauths().StateLog(request=request)
    if user_at["State"] == True:
        name = user_at["User"].first_name
        remind = Remind_member.objects.filter(user=user_at["User"].id)
        if len(remind) != 0:
            data = True
        else:
            data = False    
        today = date.today()
        birthday_data = []
        today_birthday_data = []
        for member in remind:
            birth_date = member.Date_remind
            # تبدیل تاریخ میلادی به شمسی
            jalali_date = convert_gregorian_to_jalali(birth_date)

            # استفاده از تاریخ میلادی برای محاسبه تاریخ تولد بعدی
            next_birthday = birth_date.replace(year=today.year)

            # اگر تاریخ تولد امسال گذشته باشد، سال بعد را در نظر می‌گیریم
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            
            days_remaining = (next_birthday - today).days - 1

             # محاسبه سن
            age = today.year - birth_date.year
            if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
                age -= 1  # اگر هنوز تولد فرد در سال جاری نرسیده است

            # تعیین رنج سنی
            if age <= 2:
                age_range = "شیرخوار"
            elif 2 <= age <= 7:
                age_range = "کودک"
            elif 8 <= age <= 13:
                age_range = "نونهال"
            elif 14 <= age <= 17:
                age_range = "نوجوان"
            elif 18 <= age <= 40:
                age_range = "جوان"
            elif 41 <= age <= 65:
                age_range = "میان سال"
            else:
                age_range = "کهن سال"
          

            # اگر روزهای مانده برابر با 0 است، مقدار آن را "امروز" قرار می‌دهیم
            if days_remaining <= 0:
                birthday_data.append({
                    "name": member.Full_name,
                    "birth_date": jalali_date,
                    "days_remaining": "امروز",  # نوشتن "امروز"
                    "age": age,
                    "age_range": age_range,
                    "date_befor": member.Befor_day_remind,
                    "id": member.id
                })
            else:
                today_birthday_data.append({
                    "name": member.Full_name,
                    "birth_date": jalali_date,
                    "days_remaining": days_remaining,
                    "age": age,
                    "age_range": age_range,
                    "date_befor": member.Befor_day_remind,
                    "id": member.id
                })

        # ابتدا ردیف‌های مربوط به تولدهای امروز را اضافه می‌کنیم
        birthday_data.extend(today_birthday_data)

        # مرتب‌سازی داده‌ها بر اساس روز مانده به تولد
        birthday_data.sort(key=lambda x: x['days_remaining'] if isinstance(x['days_remaining'], int) else -1)


        return render(request=request, template_name="reminder.html", context={"user": user_at , "username" : name , "remind": remind, "birthday_data": birthday_data , "data":data}  )
    else:
        return HttpResponseRedirect("/auth")

def convert_jalali_to_gregorian(jalali_date):
    """
    تبدیل تاریخ جلالی به میلادی
    """
    try:
        year, month, day = map(int, jalali_date.split('-'))
        jalali_date = jdatetime.date(year, month, day)
        gregorian_date = jalali_date.togregorian()
        return gregorian_date.strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Error converting date: {e}")
        return None
    

def convert_gregorian_to_jalali(gregorian_date):
    """
    تبدیل تاریخ میلادی به جلالی
    """
    try:
        # تاریخ میلادی باید به صورت شیء datetime وارد شود
        jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)  # استفاده از متد fromgregorian برای تبدیل
        # تبدیل میلادی به جلالی
        return jalali_date.strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Error converting date: {e}")
        return None

    
def SaveRemind(request):
    if request.method == "POST":
        # گرفتن کاربر لاگین شده
        user_at = Userauths().StateLog(request=request)
        full_name = request.POST.get("name")
        date = request.POST.get("date")  # تاریخ شمسی
        day_befor = request.POST.get("remind")
        formid = request.POST.get("id")
        
        # تبدیل تاریخ شمسی به میلادی
        gregorian_date = convert_jalali_to_gregorian(date)
        if not gregorian_date:
            return HttpResponse("Invalid date format", status=400)
        
        # بررسی وجود داده مشابه
        exists = Remind_member.objects.filter(
            user=user_at["User"].id, 
            Full_name=full_name, 
            Date_remind=gregorian_date
        ).exists()

        if exists:
            return HttpResponse("Duplicate data")  # اگر داده تکراری است، false برگردان

        # ایجاد شیء جدید و ذخیره‌سازی
        print(formid)
        if formid == "0":
            Remind = Remind_member(
                user=user_at["User"],
                Full_name=full_name,
                Date_remind=gregorian_date,  # استفاده از تاریخ میلادی
                Befor_day_remind=day_befor
            )
            Remind.save()
            return HttpResponse("true")
        
        else:
            obj=Remind_member.objects.filter(id = formid).first()
            obj.Full_name=full_name,
            obj.Date_remind=gregorian_date,
            obj.Befor_day_remind=day_befor,
            obj.save()
            return HttpResponse("edit true")
        

def editremind(request):        
    if request.method == "POST":
            # گرفتن کاربر لاگین شده
            user_at = Userauths().StateLog(request=request)
            full_name = request.POST.get("name")
            date = request.POST.get("date")  # تاریخ شمسی
            day_befor = request.POST.get("remind")
            formid = request.POST.get("id")
            
            # تبدیل تاریخ شمسی به میلادی
            gregorian_date = convert_jalali_to_gregorian(date)
            if not gregorian_date:
                return HttpResponse("Invalid date format", status=400)
            
            # بررسی وجود داده مشابه
            exists = Remind_member.objects.filter(
                user=user_at["User"].id, 
                Full_name=full_name, 
                Date_remind=gregorian_date
            ).exists()

            if exists:
                return HttpResponse("Duplicate data")  # اگر داده تکراری است، false برگردان   
            
            
            obj=Remind_member.objects.filter(id = formid).first()
            
            obj.Full_name=full_name
            obj.Date_remind=gregorian_date
            obj.Befor_day_remind=day_befor
            obj.save()
            return HttpResponse("edit true")  
           
       
def deleteremind(request):
    if request.method == "POST":
        formid = request.POST.get("id")
        obj=Remind_member.objects.filter(id = formid).first()
        obj.delete()
        return HttpResponse("true")
    else:
        return HttpResponse("false")       
            
    
        