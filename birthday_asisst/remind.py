from reminder.models import Remind_member
from datetime import date
from main_page.models import Information
import http
import json
import schedule
import time
import os
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_asisst.settings')
django.setup()



def send_reminder_sms():
   
    remind = Remind_member.objects.all()
    today = date.today()
    for item in remind:
        birth_date = item.Date_remind
        birthday = birth_date.replace(year=today.year)
        if today == birthday:
            
            obj = Information.objects.filter(user=item.user).first()
            phone_number = obj.Phone
            message=f"امروز تولد {item.Full_name} یادت نره بهش تبریک بگی💕"
            # conn = http.client.HTTPSConnection("api.sms.ir")
            # payload = json.dumps({
            #     "lineNumber": 30007487130754,
            #     "messageTexts": [
            #     message,  
            #     ],
            #     "mobiles": [
            #     phone_number,
            #     ],
            #     "senddatetime": None
            # })
            # headers = {
            #     'Content-Type': 'application/json',
            #     'Accept': 'text/plain',
            #     'X-API-KEY': 'YtEKfmrrr5Fxpyl8CQYX8nqWaKDYWMD24SSnsq0eXNSVRiNZ'
            # }
            # conn.request("POST", "/v1/send/likeToLike", payload, headers)
            # res = conn.getresponse()
            # data = res.read()
            # print(data.decode("utf-8"))
            print(message)


# زمان‌بندی اجرای تابع
# schedule.every().day.at("08:00").do(send_reminder_sms)  # اجرا هر روز ساعت 8 صبح


schedule.every(5).minutes.do(send_reminder_sms)  # اجرا هر روز ساعت 8 صبح



# اجرای وظایف زمان‌بندی‌شده
while True:
    schedule.run_pending()  # وظایف زمان‌بندی‌شده را اجرا کن
    time.sleep(1)  # کاهش مصرف منابع
