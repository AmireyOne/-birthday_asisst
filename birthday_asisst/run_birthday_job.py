import os
import django
from birthday_asisst.remind import send_reminder_sms 

# مقداردهی تنظیمات پروژه Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_asisst.settings')
django.setup()



# اجرای تابع
if __name__ == "__main__":
    send_reminder_sms()
