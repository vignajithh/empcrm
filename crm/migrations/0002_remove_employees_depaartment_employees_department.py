# Generated by Django 4.2.6 on 2023-10-31 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='depaartment',
        ),
        migrations.AddField(
            model_name='employees',
            name='department',
            field=models.CharField(default=1000, max_length=200),
            preserve_default=False,
        ),
    ]
