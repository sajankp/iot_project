# Generated by Django 2.0.10 on 2019-02-01 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp8266', '0003_auto_20190201_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='date',
        ),
    ]
