# Generated by Django 3.1.2 on 2020-12-06 18:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('bilkent_id', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^[0-9]{8}$')])),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('pp', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('bilkent_id',),
                'unique_together': {('bilkent_id', 'first_name', 'last_name', 'email')},
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50, unique=True)),
                ('club_description', models.TextField()),
                ('club_tags', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('leader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BilEventsApp.participant')),
                ('participants', models.ManyToManyField(related_name='club_participants', to='BilEventsApp.Participant')),
            ],
            options={
                'ordering': ('club_name',),
                'unique_together': {('club_name', 'logo', 'leader')},
            },
        ),
        migrations.CreateModel(
            name='RecommendedEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50, unique=True)),
                ('event_place', models.TextField()),
                ('event_time', models.DateTimeField()),
                ('event_capacity', models.PositiveIntegerField(default=0)),
                ('event_description', models.TextField(default='')),
                ('event_tags', models.CharField(max_length=200)),
                ('event_zoom_link', models.URLField(blank=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BilEventsApp.club')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BilEventsApp.participant')),
            ],
            options={
                'ordering': ('event_time',),
                'unique_together': {('event_name',)},
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50, unique=True)),
                ('event_place', models.TextField()),
                ('event_time', models.DateTimeField()),
                ('event_capacity', models.PositiveIntegerField(default=0)),
                ('event_description', models.TextField(default='')),
                ('event_tags', models.CharField(max_length=200)),
                ('event_zoom_link', models.URLField(blank=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BilEventsApp.club')),
                ('participants', models.ManyToManyField(blank=True, null=True, to='BilEventsApp.Participant')),
            ],
            options={
                'ordering': ('event_time',),
                'unique_together': {('event_name',)},
            },
        ),
    ]
