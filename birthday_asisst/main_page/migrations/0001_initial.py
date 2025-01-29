# Generated by Django 5.1.3 on 2024-11-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Full_name', models.CharField(max_length=300)),
                ('Comment_message', models.TextField(max_length=2000)),
                ('stars', models.IntegerField(choices=[(1, '1 ستاره'), (2, '2 ستاره'), (3, '3 ستاره'), (4, '4 ستاره'), (5, '5 ستاره')])),
                ('Created', models.DateField()),
            ],
        ),
    ]
