# Generated by Django 5.1.2 on 2024-12-08 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrior',
            name='profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warriors', to='warriors_app.profession', verbose_name='Профессия'),
        ),
    ]
