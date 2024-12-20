# Generated by Django 5.1.2 on 2024-12-10 11:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('patronymic', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
                ('working_status', models.CharField(max_length=30)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='work_api.employee')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='work_api.position')),
            ],
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('is_done', models.BooleanField(default=False)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_schedule', to='work_api.contract')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_schedule', to='hotel_api.room')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_history', to='work_api.position')),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('salary__gt', 0)), name='salary > 0')],
            },
        ),
    ]
