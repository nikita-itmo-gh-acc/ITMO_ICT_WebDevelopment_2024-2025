# Generated by Django 5.1.2 on 2024-11-16 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_add_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]