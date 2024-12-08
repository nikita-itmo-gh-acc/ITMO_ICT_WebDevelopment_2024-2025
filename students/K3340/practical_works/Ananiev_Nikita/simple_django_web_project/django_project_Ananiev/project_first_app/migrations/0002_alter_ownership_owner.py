# Generated by Django 5.1.2 on 2024-12-08 09:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownerships', to=settings.AUTH_USER_MODEL),
        ),
    ]
