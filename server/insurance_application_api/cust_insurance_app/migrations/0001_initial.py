# Generated by Django 4.0.4 on 2022-05-15 12:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustId', models.IntegerField(unique=True)),
                ('Gender', models.CharField(max_length=10, null=True)),
                ('Income_Group', models.CharField(max_length=500, null=True)),
                ('Region', models.CharField(max_length=100, null=True)),
                ('Marital_status', models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PolicyId', models.IntegerField(unique=True)),
                ('Purchase_date', models.DateField(blank=True, editable=False)),
                ('Fuel', models.CharField(max_length=100, null=True)),
                ('VEHICLE_SEGMENT', models.CharField(max_length=100, null=True)),
                ('Premium', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000000), django.core.validators.MinValueValidator(0)])),
                ('Bodily_Injury_Liability', models.BooleanField(blank=True, default=False)),
                ('Personal_Injury_Protection', models.BooleanField(blank=True, default=False)),
                ('Property_Damage_Liability', models.BooleanField(blank=True, default=False)),
                ('Collision', models.BooleanField(blank=True, default=False)),
                ('Comprehensive', models.BooleanField(blank=True, default=False)),
                ('CustId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cust_insurance_app.customerdetails')),
            ],
        ),
    ]
