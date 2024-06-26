# Generated by Django 5.0.1 on 2024-03-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0002_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='EngGroup',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='EngType',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='airfield',
            name='AFFAA',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='airfield',
            name='City',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='airfield',
            name='Notes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='airfield',
            name='UserEdit',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='Cargo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='DateIssued',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='DateValid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
