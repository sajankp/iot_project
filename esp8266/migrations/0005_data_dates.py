# Generated by Django 2.0.10 on 2019-02-01 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('esp8266', '0004_remove_data_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='dates',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
