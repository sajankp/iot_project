# Generated by Django 2.1.7 on 2019-05-01 03:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('esp8266', '0007_auto_20190501_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]