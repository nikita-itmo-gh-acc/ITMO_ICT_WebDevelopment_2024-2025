# Generated by Django 5.1.2 on 2024-11-20 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0004_hotelpicture_roompicture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='is_booked',
        ),
    ]