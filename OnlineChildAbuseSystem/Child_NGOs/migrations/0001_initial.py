# Generated by Django 2.2.6 on 2019-12-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NGORegistrationModel',
            fields=[
                ('ngo_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('ngo_place', models.CharField(max_length=70)),
                ('ngo_volunteer_name', models.CharField(max_length=70)),
                ('mandal', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=70, unique=True)),
                ('Ngo_mail', models.EmailField(max_length=254)),
                ('complete_address', models.TextField(default=True)),
                ('password', models.CharField(max_length=70)),
                ('status', models.CharField(default=True, max_length=50)),
                ('Date_of_join', models.DateField(auto_now=True)),
            ],
        ),
    ]
