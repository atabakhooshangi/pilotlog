# Generated by Django 5.0.1 on 2024-03-29 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
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
                'db_table': 'Aircraft',
            },
        ),
        migrations.CreateModel(
            name='Airfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('AFCat', models.PositiveIntegerField(blank=True, null=True)),
                ('AFCode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('AFIATA', models.CharField(blank=True, max_length=10, null=True)),
                ('AFICAO', models.CharField(blank=True, max_length=10, null=True)),
                ('AFName', models.CharField(blank=True, max_length=100, null=True)),
                ('TZCode', models.PositiveIntegerField()),
                ('Latitude', models.IntegerField(blank=True, null=True)),
                ('ShowList', models.BooleanField()),
                ('AFCountry', models.IntegerField(blank=True, null=True)),
                ('Longitude', models.IntegerField(blank=True, null=True)),
                ('NotesUser', models.CharField(blank=True, max_length=100, null=True)),
                ('RegionUser', models.IntegerField(blank=True, null=True)),
                ('ElevationFT', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Airfield',
            },
        ),
        migrations.CreateModel(
            name='ImagePic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('FileExt', models.CharField(blank=True, max_length=50, null=True)),
                ('ImgCode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('FileName', models.CharField(blank=True, max_length=50, null=True)),
                ('LinkCode', models.CharField(blank=True, max_length=50, null=True)),
                ('Img_Upload', models.BooleanField()),
                ('Img_Download', models.BooleanField()),
            ],
            options={
                'db_table': 'ImagePic',
            },
        ),
        migrations.CreateModel(
            name='LimitRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('LTo', models.DateField(blank=True, null=True)),
                ('LFrom', models.DateField(blank=True, null=True)),
                ('LType', models.IntegerField(blank=True, null=True)),
                ('LZone', models.IntegerField(blank=True, null=True)),
                ('LMinutes', models.IntegerField(blank=True, null=True)),
                ('LimitCode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('LPeriodCode', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'LimitRules',
            },
        ),
        migrations.CreateModel(
            name='MyQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('mQCode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('QuickView', models.BooleanField()),
                ('ShortName', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'myQuery',
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('Notes', models.CharField(blank=True, max_length=100, null=True)),
                ('Active', models.BooleanField()),
                ('Company', models.CharField(blank=True, max_length=100, null=True)),
                ('FavList', models.BooleanField()),
                ('UserAPI', models.CharField(blank=True, max_length=100, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('LinkedIn', models.CharField(blank=True, max_length=100, null=True)),
                ('PilotRef', models.CharField(blank=True, max_length=100, null=True)),
                ('PilotCode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('PilotName', models.CharField(blank=True, max_length=100, null=True)),
                ('PilotEMail', models.CharField(blank=True, max_length=100, null=True)),
                ('PilotPhone', models.CharField(blank=True, max_length=100, null=True)),
                ('Certificate', models.CharField(blank=True, max_length=100, null=True)),
                ('PhoneSearch', models.CharField(blank=True, max_length=100, null=True)),
                ('PilotSearch', models.CharField(blank=True, max_length=100, null=True)),
                ('RosterAlias', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Pilot',
            },
        ),
        migrations.CreateModel(
            name='SettingConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('Data', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Group', models.CharField(blank=True, max_length=100, null=True)),
                ('ConfigCode', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'db_table': 'SettingConfig',
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
                ('Aircraft', models.ForeignKey(db_column='AircraftCode', on_delete=django.db.models.deletion.DO_NOTHING, to='pilotlog.aircraft', to_field='AircraftCode')),
            ],
            options={
                'db_table': 'Flight',
            },
        ),
        migrations.CreateModel(
            name='MyQueryBuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_Modified', models.IntegerField()),
                ('Build1', models.CharField(blank=True, max_length=100, null=True)),
                ('Build2', models.CharField(blank=True, max_length=100, null=True)),
                ('Build3', models.CharField(blank=True, max_length=100, null=True)),
                ('Build4', models.CharField(blank=True, max_length=100, null=True)),
                ('mQBCode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('mQCode', models.ForeignKey(db_column='mQCode', on_delete=django.db.models.deletion.DO_NOTHING, to='pilotlog.myquery', to_field='mQCode')),
            ],
            options={
                'db_table': 'myQueryBuild',
            },
        ),
    ]
