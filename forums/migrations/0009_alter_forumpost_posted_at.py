# Generated by Django 4.2.3 on 2023-10-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0008_alter_forumpost_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
