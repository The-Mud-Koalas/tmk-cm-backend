# Generated by Django 4.2.3 on 2023-10-07 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='current_num_of_participants',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='current_num_of_volunteers',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='min_num_of_volunteers',
            field=models.PositiveIntegerField(default=0),
        ),
    ]