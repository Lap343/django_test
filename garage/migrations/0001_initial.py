# Generated by Django 3.1.4 on 2020-12-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('length', models.CharField(max_length=20)),
                ('width', models.CharField(max_length=50)),
                ('hin', models.CharField(max_length=50)),
                ('current_hours', models.IntegerField()),
                ('service_interval', models.CharField(max_length=50)),
                ('next_service', models.DateField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('vin', models.CharField(max_length=50)),
                ('current_mileage', models.IntegerField()),
                ('service_interval', models.CharField(max_length=50)),
                ('next_service', models.DateField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('bed_length', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=50)),
                ('vin', models.CharField(max_length=50)),
                ('current_mileage', models.IntegerField()),
                ('service_interval', models.CharField(max_length=50)),
                ('next_service', models.DateField(max_length=50)),
            ],
        ),
    ]
