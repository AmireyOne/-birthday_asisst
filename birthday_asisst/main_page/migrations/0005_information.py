# Generated by Django 5.1.3 on 2024-11-20 13:44

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_comment_phone_alter_comment_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=200)),
                ('Birthday', django_jalali.db.models.jDateField(verbose_name='تاریخ تولد')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
