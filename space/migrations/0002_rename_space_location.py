# Generated by Django 4.2.3 on 2023-09-13 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_interests'),
        ('event', '0005_event_event_image_directory'),
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Space',
            new_name='Location',
        ),
    ]