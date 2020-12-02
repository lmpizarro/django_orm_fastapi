# Generated by Django 3.1.2 on 2020-10-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0005_auto_20201017_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='severity',
            field=models.CharField(choices=[('CR', 'Critical'), ('ER', 'Error'), ('WR', 'Warning'), ('IN', 'Info'), ('DG', 'Debug')], default='IN', max_length=2),
        ),
    ]
