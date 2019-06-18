# Generated by Django 2.1.7 on 2019-06-18 14:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('esp8266', '0008_auto_20190501_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Full Name', max_length=200)),
                ('mobile_number', models.BigIntegerField(help_text='Mobile number of owner')),
                ('field_1', models.CharField(help_text='Flat, House no., Building, Company, Apartment :', max_length=200)),
            ],
            options={
                'ordering': ['building', 'field_1'],
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(help_text='Enter a description about the building', max_length=200, null=True)),
                ('building_name', models.CharField(help_text='Building name', max_length=100)),
                ('field_2', models.CharField(help_text='Area, Colony, Street, Sector, Village: ', max_length=100)),
                ('landmark', models.CharField(help_text='Landmark e.g. near apollo hospital: ', max_length=100)),
                ('town', models.CharField(help_text='Town/City: ', max_length=100)),
                ('state', models.CharField(choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('CT', 'Chhattisgarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha, Orissa'), ('PY', 'Puducherry'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UT', 'Uttarakhand,Uttaranchal'), ('WB', 'West Bengal')], help_text='State', max_length=2)),
                ('pincode', models.IntegerField(default=676121, validators=[django.core.validators.MaxValueValidator(999999)])),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('key', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for security and identification purposes')),
                ('description', models.TextField(help_text='Enter a description on sensor location', max_length=100, null=True)),
                ('is_outdoor', models.BooleanField(choices=[(True, 'Outdoor'), (False, 'Indoor')], default=False, help_text='The location of sensor')),
                ('appartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='esp8266.Appartment')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='appartment',
            name='building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='esp8266.Building'),
        ),
        migrations.AddField(
            model_name='data',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='esp8266.Sensor'),
        ),
    ]