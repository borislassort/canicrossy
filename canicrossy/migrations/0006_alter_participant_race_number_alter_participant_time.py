# Generated by Django 4.2.7 on 2023-11-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canicrossy', '0005_alter_athlete_birth_date_alter_athlete_dog_race_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='race_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='dossard'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='time',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='chrono (hh:mm:ss)'),
        ),
    ]
