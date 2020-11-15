from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ClubLeader(User):
    def __str__(super):
        return super.username

class Club(models.Model):
    club_name = models.CharField(max_length=50)
    club_description = models.TextField()
    club_tags = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="images/", null=True, blank=True)
    club_leader = models.OneToOneField(
        ClubLeader,
        on_delete=models.CASCADE,
    )
    club_participants = models.ManyToManyField(User)

    class Meta:
        ordering = ('club_name',)

    def __str__(self):
        return self.club_name

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_place = models.TextField()
    event_time = models.DateTimeField()
    event_capacity = models.PositiveIntegerField(default=0)
    event_description = models.TextField()
    event_tags = models.CharField(max_length=200)
    event_zoom_link = models.URLField(max_length=200, blank=True, null=True)
    participants = models.ManyToManyField(User)
    club = models.ForeignKey(Club, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('event_name',)
        
    def __str__(self):
        return self.event_name

class RecommendedEvent(Event):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.event_name

