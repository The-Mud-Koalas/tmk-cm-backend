# Generated by Django 4.2.3 on 2023-10-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='initial_location_track_prompt',
            field=models.BooleanField(default=False),
        ),
    ]