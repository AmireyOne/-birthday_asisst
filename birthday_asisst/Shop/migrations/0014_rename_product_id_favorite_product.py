# Generated by Django 5.1.3 on 2025-01-02 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_alter_commentlike_id_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='Product_id',
            new_name='Product',
        ),
    ]
