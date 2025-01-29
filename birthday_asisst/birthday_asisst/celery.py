from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تنظیمات پروژه Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_asisst.settings')

app = Celery('birthday_asisst')

# تنظیمات Celery برای استفاده از Redis به‌عنوان Broker
app.config_from_object('django.conf:settings', namespace='CELERY')

# بارگذاری tasks از تمام اپ‌های نصب‌شده
app.autodiscover_tasks()



