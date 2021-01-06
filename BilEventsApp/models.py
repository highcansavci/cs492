from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db.models import Count
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


# Create your models here.

class Participant(models.Model):
    bilkent_id = models.PositiveIntegerField(primary_key = True, validators=[RegexValidator(regex='^[0-9]{8}$', message='Length has to be 8', code='nomatch')])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(unique = True, max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        ordering = ('bilkent_id',)
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Club(models.Model):
    club_name = models.CharField(unique=True, max_length=50)
    club_description = models.TextField()
    club_tags = models.CharField(max_length=200)
    logo = models.URLField(max_length=200, blank=True, null=True)
    leader = models.OneToOneField(
        Participant,
        on_delete=models.CASCADE,
    )
    club_members = models.ManyToManyField(Participant, blank=True, null=True, related_name='club_members')

    class Meta:
        ordering = ('club_name',)

    def __str__(self):
        return self.club_name

class EventInfo(models.Model):
    event_name = models.CharField(unique=True, max_length=50)
    event_place = models.TextField()
    event_time = models.DateTimeField()
    event_points = models.PositiveIntegerField(default=0)
    event_max_capacity = models.PositiveIntegerField(default=0)
    event_description = models.TextField(default="")
    event_tags = models.CharField(max_length=200)
    event_zoom_link = models.URLField(max_length=200, blank=True, null=True)  
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    event_current_capacity = models.PositiveIntegerField(default=0)
    participants = models.ManyToManyField(Participant, blank=True, null=True, through='Rate')
    event_avg_score = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

class Event(EventInfo):    
    def save(self, *args, **kwargs):
        if self.event_current_capacity < self.event_max_capacity:
            super().save(*args, **kwargs)
        else:
            raise ValidationError(_('Cannot exceed the maximum capacity'), code='max')
            
    class Meta:
        ordering = ('event_time',)
        
    def __str__(self):
        return self.event_name


class RecommendedEvent(EventInfo):
    users = models.ManyToManyField(Participant, blank=True, null=True, related_name='recommended_users')
    def save(self, *args, **kwargs):
        if timezone.now() < self.event_time:
            if self.event_current_capacity < self.event_max_capacity:
                super().save(*args, **kwargs)
            else:
                raise ValidationError(_('Cannot exceed the maximum capacity'), code='max')
        else:
            raise ValidationError(_('Cannot recommend the past event'), code='past')
    
    class Meta:
        ordering = ('event_time',)
        
    def __str__(self):
        return self.event_name

class Rate(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(EventInfo, on_delete=models.CASCADE)
    event_score = models.PositiveIntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )