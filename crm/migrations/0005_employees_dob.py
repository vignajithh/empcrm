# Generated by Django 4.2.6 on 2023-11-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_rename_image_employees_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
