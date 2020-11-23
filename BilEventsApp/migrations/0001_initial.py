# Generated by Django 3.1.2 on 2020-11-22 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50)),
                ('club_description', models.TextField()),
                ('club_tags', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'ordering': ('club_name',),
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bilkent_id', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('pp', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
        migrations.CreateModel(
            name='ClubLeader',
            fields=[
                ('participant_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BilEventsApp.participant')),
            ],
            bases=('BilEventsApp.participant',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_place', models.TextField()),
                ('event_time', models.DateTimeField()),
                ('event_capacity', models.PositiveIntegerField(default=0)),
                ('event_description', models.TextField()),
                ('event_tags', models.CharField(max_length=200)),
                ('event_zoom_link', models.URLField(blank=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BilEventsApp.club')),
                ('participants', models.ManyToManyField(to='BilEventsApp.Participant')),
            ],
            options={
                'ordering': ('event_name',),
            },
        ),
        migrations.AddField(
            model_name='club',
            name='club_participants',
            field=models.ManyToManyField(to='BilEventsApp.Participant'),
        ),
        migrations.CreateModel(
            name='RecommendedEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BilEventsApp.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BilEventsApp.participant')),
            ],
            bases=('BilEventsApp.event',),
        ),
        migrations.AddField(
            model_name='club',
            name='club_leader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BilEventsApp.clubleader'),
        ),
    ]