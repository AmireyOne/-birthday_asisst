# Generated by Django 5.1.3 on 2025-01-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0022_orders_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='ref_id',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
