# Generated by Django 4.2.6 on 2023-11-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_remove_employees_depaartment_employees_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
