# Generated by Django 4.2.3 on 2023-10-08 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContributionReview',
        ),
        migrations.DeleteModel(
            name='ParticipationVolunteeringReview',
        ),
    ]