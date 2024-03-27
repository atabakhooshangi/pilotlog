# Generated by Django 5.0.1 on 2024-01-29 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirCraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('Fin', models.CharField(blank=True, max_length=100, null=True)),
                ('Sea', models.BooleanField(default=False)),
                ('TMG', models.BooleanField(default=False)),
                ('Efis', models.BooleanField(default=False)),
                ('FNPT', models.IntegerField(blank=True, null=True)),
                ('Make', models.CharField(blank=True, max_length=100, null=True)),
                ('Run2', models.BooleanField(default=False)),
                ('Class', models.IntegerField(blank=True, null=True)),
                ('Model', models.CharField(blank=True, max_length=100, null=True)),
                ('Power', models.IntegerField(blank=True, null=True)),
                ('Seats', models.IntegerField(blank=True, null=True)),
                ('Active', models.BooleanField(default=False)),
                ('Kg5700', models.BooleanField(default=False)),
                ('Rating', models.CharField(blank=True, max_length=100, null=True)),
                ('Company', models.CharField(blank=True, max_length=100, null=True)),
                ('Complex', models.BooleanField(default=False)),
                ('CondLog', models.IntegerField(blank=True, null=True)),
                ('FavList', models.BooleanField(default=False)),
                ('Category', models.IntegerField()),
                ('HighPerf', models.BooleanField(default=False)),
                ('SubModel', models.CharField(blank=True, null=True)),
                ('Aerobatic', models.BooleanField(default=False)),
                ('RefSearch', models.CharField(blank=True, null=True)),
                ('Reference', models.CharField(blank=True, null=True)),
                ('Tailwheel', models.BooleanField(default=False)),
                ('DefaultApp', models.IntegerField(blank=True, null=True)),
                ('DefaultLog', models.IntegerField(blank=True, null=True)),
                ('DefaultOps', models.IntegerField(blank=True, null=True)),
                ('DeviceCode', models.IntegerField(blank=True, null=True)),
                ('AircraftCode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('DefaultLaunch', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-Record_Modified',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('PF', models.BooleanField(default=False)),
                ('Pax', models.IntegerField(blank=True, null=True)),
                ('Fuel', models.IntegerField(blank=True, null=True)),
                ('DeIce', models.BooleanField(default=False)),
                ('Route', models.CharField(blank=True, max_length=250, null=True)),
                ('ToDay', models.IntegerField(blank=True, null=True)),
                ('minU1', models.IntegerField(blank=True, null=True)),
                ('minU2', models.IntegerField(blank=True, null=True)),
                ('minU3', models.IntegerField(blank=True, null=True)),
                ('minU4', models.IntegerField(blank=True, null=True)),
                ('minXC', models.IntegerField(blank=True, null=True)),
                ('ArrRwy', models.CharField(blank=True, max_length=250, null=True)),
                ('DepRwy', models.CharField(blank=True, max_length=250, null=True)),
                ('LdgDay', models.IntegerField(blank=True, null=True)),
                ('LiftSW', models.IntegerField(blank=True, null=True)),
                ('P1Code', models.CharField(blank=True, max_length=250, null=True)),
                ('P2Code', models.CharField(blank=True, max_length=250, null=True)),
                ('P3Code', models.CharField(blank=True, max_length=250, null=True)),
                ('P4Code', models.CharField(blank=True, max_length=250, null=True)),
                ('Report', models.CharField(blank=True, max_length=250, null=True)),
                ('TagOps', models.CharField(blank=True, max_length=250, null=True)),
                ('ToEdit', models.BooleanField(default=False)),
                ('minAIR', models.IntegerField(blank=True, null=True)),
                ('minCOP', models.IntegerField(blank=True, null=True)),
                ('minIFR', models.IntegerField(blank=True, null=True)),
                ('minIMT', models.IntegerField(blank=True, null=True)),
                ('minPIC', models.IntegerField(blank=True, null=True)),
                ('minREL', models.IntegerField(blank=True, null=True)),
                ('minSFR', models.IntegerField(blank=True, null=True)),
                ('ArrCode', models.CharField(blank=True, max_length=250, null=True)),
                ('DateUTC', models.CharField(blank=True, max_length=250, null=True)),
                ('DepCode', models.CharField(blank=True, max_length=250, null=True)),
                ('HobbsIn', models.IntegerField(blank=True, null=True)),
                ('Holding', models.IntegerField(blank=True, null=True)),
                ('Pairing', models.CharField(blank=True, max_length=250, null=True)),
                ('Remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('SignBox', models.IntegerField(blank=True, null=True)),
                ('ToNight', models.IntegerField(blank=True, null=True)),
                ('UserNum', models.IntegerField(blank=True, null=True)),
                ('minDUAL', models.IntegerField(blank=True, null=True)),
                ('minEXAM', models.IntegerField(blank=True, null=True)),
                ('CrewList', models.CharField(blank=True, max_length=250, null=True)),
                ('DateBASE', models.DateField(blank=True, null=True)),
                ('FuelUsed', models.IntegerField(blank=True, null=True)),
                ('HobbsOut', models.IntegerField(blank=True, null=True)),
                ('LdgNight', models.IntegerField(blank=True, null=True)),
                ('NextPage', models.BooleanField(default=False)),
                ('TagDelay', models.CharField(blank=True, max_length=250, null=True)),
                ('Training', models.CharField(blank=True, max_length=250, null=True)),
                ('UserBool', models.BooleanField(default=False)),
                ('UserText', models.CharField(blank=True, max_length=250, null=True)),
                ('minINSTR', models.IntegerField(blank=True, null=True)),
                ('minNIGHT', models.IntegerField(blank=True, null=True)),
                ('minPICUS', models.IntegerField(blank=True, null=True)),
                ('minTOTAL', models.IntegerField(blank=True, null=True)),
                ('ArrOffset', models.IntegerField(blank=True, null=True)),
                ('DateLOCAL', models.DateField(blank=True, null=True)),
                ('DepOffset', models.IntegerField(blank=True, null=True)),
                ('TagLaunch', models.CharField(blank=True, max_length=250, null=True)),
                ('TagLesson', models.CharField(blank=True, max_length=250, null=True)),
                ('ToTimeUTC', models.IntegerField(blank=True, null=True)),
                ('ArrTimeUTC', models.IntegerField(blank=True, null=True)),
                ('BaseOffset', models.IntegerField(blank=True, null=True)),
                ('DepTimeUTC', models.IntegerField(blank=True, null=True)),
                ('FlightCode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('LdgTimeUTC', models.IntegerField(blank=True, null=True)),
                ('FuelPlanned', models.IntegerField(blank=True, null=True)),
                ('NextSummary', models.BooleanField(default=False)),
                ('TagApproach', models.CharField(blank=True, max_length=250, null=True)),
                ('ArrTimeSCHED', models.IntegerField(blank=True, null=True)),
                ('DepTimeSCHED', models.IntegerField(blank=True, null=True)),
                ('FlightNumber', models.CharField(blank=True, max_length=250, null=True)),
                ('FlightSearch', models.CharField(blank=True, max_length=250, null=True)),
                ('AircraftCode', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pilotlog.aircraft', to_field='AircraftCode')),
            ],
            options={
                'ordering': ('-Record_Modified',),
                'abstract': False,
            },
        ),
    ]
