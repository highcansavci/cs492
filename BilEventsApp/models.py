from django.db import models
from django.core.validators import RegexValidator
from django.db.models import Count
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
    club_name = models.CharField(max_length=50, unique=True)
    club_description = models.TextField()
    club_tags = models.CharField(max_length=200)
    logo = models.URLField(max_length=200, blank=True, null=True)
    leader = models.OneToOneField(
        Participant,
        on_delete=models.CASCADE,
    )
    participants = models.ManyToManyField(Participant, related_name='club_participants')

    class Meta:
        ordering = ('club_name',)
        unique_together = ('club_name', 'logo', 'leader')

    def __str__(self):
        return self.club_name

class Event(models.Model):
    event_name = models.CharField(unique=True, max_length=50)
    event_place = models.TextField()
    event_time = models.DateTimeField()
    event_points = models.PositiveIntegerField(default=0)
    event_max_capacity = models.PositiveIntegerField(default=0)
    event_description = models.TextField(default="")
    event_tags = models.CharField(max_length=200)
    event_zoom_link = models.URLField(max_length=200, blank=True, null=True)
    participants = models.ManyToManyField(Participant, blank=True, null=True, related_name='event_participants')
    club = models.ForeignKey(Club, blank=True, null=True, on_delete=models.CASCADE)
    event_current_capacity = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        print(Participant.objects.all().annotate(event_count=models.Count('event_participants')).count())
        self.event_current_capacity = Participant.objects.all().annotate(event_count=Count('event_participants')).count()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('event_time',)
        unique_together = ('event_name',)
        
    def __str__(self):
        return self.event_name

class RecommendedEvent(models.Model):
    event_name = models.CharField(unique=True, max_length=50)
    event_place = models.TextField()
    event_points = models.PositiveIntegerField(default=0)
    event_time = models.DateTimeField()
    event_max_capacity = models.PositiveIntegerField(default=0)
    event_description = models.TextField(default="")
    event_tags = models.CharField(max_length=200)
    event_zoom_link = models.URLField(max_length=200, blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(Participant, on_delete=models.CASCADE)
    class Meta:
        ordering = ('event_time',)
        unique_together = ('event_name',)
        
    def __str__(self):
        return self.event_name

