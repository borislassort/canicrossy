# Generated by Django 4.2.7 on 2023-11-24 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canicrossy', '0007_dog_remove_athlete_dog_ident_remove_athlete_dog_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'verbose_name': 'participation', 'verbose_name_plural': 'participations'},
        ),
        migrations.AlterField(
            model_name='participant',
            name='dog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='canicrossy.dog', verbose_name='chien'),
        ),
    ]