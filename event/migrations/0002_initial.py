# Generated by Django 4.2.3 on 2023-10-07 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('space', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='eventparticipation',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='event.eventcategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='space.location'),
        ),
        migrations.AddField(
            model_name='event',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='event.tags'),
        ),
        migrations.AddField(
            model_name='transactionhistory',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.project'),
        ),
        migrations.AddField(
            model_name='project',
            name='goal_kind',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='event.goalkind'),
        ),
        migrations.AddField(
            model_name='contributionparticipation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.project'),
        ),
        migrations.AddField(
            model_name='attendanceactivity',
            name='participation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.attendableeventparticipation'),
        ),
        migrations.CreateModel(
            name='VolunteerParticipation',
            fields=[
                ('attendableeventparticipation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.attendableeventparticipation')),
                ('granted_manager_access', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('event.attendableeventparticipation',),
        ),
        migrations.CreateModel(
            name='InitiativeParticipation',
            fields=[
                ('attendableeventparticipation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.attendableeventparticipation')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.initiative')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('event.attendableeventparticipation',),
        ),
    ]
