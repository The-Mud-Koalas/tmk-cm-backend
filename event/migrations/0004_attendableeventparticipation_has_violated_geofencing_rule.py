# Generated by Django 4.2.3 on 2023-10-08 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_attendableeventparticipation_has_attended'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendableeventparticipation',
            name='has_violated_geofencing_rule',
            field=models.BooleanField(default=False),
        ),
    ]