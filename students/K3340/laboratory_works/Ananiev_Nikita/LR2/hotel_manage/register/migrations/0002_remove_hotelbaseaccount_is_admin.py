# Generated by Django 5.1.2 on 2024-11-10 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelbaseaccount',
            name='is_admin',
        ),
    ]