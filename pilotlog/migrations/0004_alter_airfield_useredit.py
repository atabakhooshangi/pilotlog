# Generated by Django 5.0.1 on 2024-03-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0003_aircraft_enggroup_aircraft_engtype_airfield_affaa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airfield',
            name='UserEdit',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]