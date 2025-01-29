from __future__ import absolute_import, unicode_literals

# به محض شروع پروژه، Celery را بارگذاری کن
from .celery import app as celery_app

__all__ = ('celery_app',)
