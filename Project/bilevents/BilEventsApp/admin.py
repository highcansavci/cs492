from django.contrib import admin
from .models import ClubLeader, Club, Event, RecommendedEvent
# Register your models here.

admin.site.register(ClubLeader)
admin.site.register(Club)
admin.site.register(Event)
admin.site.register(RecommendedEvent)