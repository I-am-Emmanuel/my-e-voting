# Generated by Django 4.1.3 on 2023-02-28 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feds', '0007_rename_phone_number_citizens_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citizens',
            old_name='email_field',
            new_name='email',
        ),
    ]