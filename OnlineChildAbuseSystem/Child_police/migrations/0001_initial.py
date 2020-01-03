# Generated by Django 2.2.6 on 2019-12-28 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceRegistrationModel',
            fields=[
                ('police_station_id', models.IntegerField(primary_key=True, serialize=False)),
                ('station_place', models.CharField(max_length=70)),
                ('station_ci_name', models.CharField(max_length=70)),
                ('mandal', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('station_mail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=70)),
                ('Date_of_join', models.DateField(auto_now=True)),
            ],
        ),
    ]
