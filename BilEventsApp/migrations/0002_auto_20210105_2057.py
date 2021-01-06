# Generated by Django 3.1.2 on 2021-01-05 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BilEventsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='event_avg_score',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
