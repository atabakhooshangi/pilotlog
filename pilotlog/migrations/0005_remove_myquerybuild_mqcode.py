# Generated by Django 5.0.1 on 2024-03-30 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0004_alter_airfield_useredit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myquerybuild',
            name='mQCode',
        ),
    ]
