from django.contrib import admin
from .models import Participant, Club, Event, RecommendedEvent
# Register your models here.

admin.site.register(Participant)
admin.site.register(Club)
admin.site.register(Event)
admin.site.register(RecommendedEvent)