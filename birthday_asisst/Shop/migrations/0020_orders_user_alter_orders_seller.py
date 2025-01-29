# Generated by Django 5.1.3 on 2025-01-20 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0019_alter_questions_product_id_orders_sellerwallet'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_orders', to=settings.AUTH_USER_MODEL, verbose_name='فروشنده'),
        ),
    ]
