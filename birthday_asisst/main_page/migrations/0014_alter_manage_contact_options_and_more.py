# Generated by Django 5.1.3 on 2025-01-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_manage_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manage_contact',
            options={'verbose_name': 'پیام مدیریت', 'verbose_name_plural': 'پیام های مدیریت'},
        ),
        migrations.AlterField(
            model_name='manage_contact',
            name='Caption',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='manage_contact',
            name='Created_at',
            field=models.DateField(auto_now_add=True, verbose_name='نوشته شده در '),
        ),
        migrations.AlterField(
            model_name='manage_contact',
            name='Title',
            field=models.CharField(max_length=300, verbose_name='موضوع'),
        ),
    ]
