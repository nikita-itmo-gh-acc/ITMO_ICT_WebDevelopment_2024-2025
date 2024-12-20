# Generated by Django 5.1.2 on 2024-12-10 11:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(default=django.utils.timezone.now)),
                ('from_town', models.CharField(max_length=30)),
                ('check_in_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('full_days', models.IntegerField(default=0)),
                ('state', models.CharField(max_length=30)),
                ('payment_status', models.CharField(max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel_api.room')),
            ],
        ),
    ]
