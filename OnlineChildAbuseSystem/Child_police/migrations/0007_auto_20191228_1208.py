# Generated by Django 2.2.6 on 2019-12-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Child_police', '0006_auto_20191228_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policeregistrationmodel',
            name='contact_number',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='policeregistrationmodel',
            name='police_station_id',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
    ]
