# Generated by Django 5.1.2 on 2024-12-09 15:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('places', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('places__lte', 4)), name='places <= 4'), models.CheckConstraint(condition=models.Q(('places__gte', 1)), name='places >= 1')],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=4, unique=True)),
                ('area', models.IntegerField()),
                ('is_occupied', models.BooleanField(default=False)),
                ('is_cleaned', models.BooleanField(default=True)),
                ('floor', models.IntegerField()),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel_api.roomtype')),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('number__regex', '\\d{3,4}')), name='number_constraint'), models.CheckConstraint(condition=models.Q(('floor__gte', 0)), name='floor_constraint')],
            },
        ),
        migrations.CreateModel(
            name='RoomTypePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_price', models.IntegerField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='hotel_api.roomtype')),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('day_price__gt', 0)), name='price > 0')],
            },
        ),
    ]
