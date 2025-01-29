# Generated by Django 5.1.3 on 2025-01-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Full_name', models.CharField(max_length=300)),
                ('Username', models.CharField(max_length=15, unique=True)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]
