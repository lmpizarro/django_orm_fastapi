# Generated by Django 3.1.2 on 2020-10-19 02:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0006_logger_severity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]