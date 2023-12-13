# Generated by Django 4.2.7 on 2023-11-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canicrossy', '0002_athlete_dog_race_alter_athlete_dog_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='athlete',
            name='first_name',
            field=models.CharField(default='', max_length=200, verbose_name='prénom'),
            preserve_default=False,
        ),
    ]