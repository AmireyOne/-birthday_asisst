# Generated by Django 5.1.3 on 2024-12-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_products_selected_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='Caption',
            field=models.TextField(max_length=1000),
        ),
    ]
