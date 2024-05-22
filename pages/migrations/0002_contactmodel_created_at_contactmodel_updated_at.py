# Generated by Django 5.0.6 on 2024-05-22 16:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]