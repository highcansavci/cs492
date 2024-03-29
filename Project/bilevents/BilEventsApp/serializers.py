from rest_framework import serializers
import django.core.serializers
from .models import Club, Event, RecommendedEvent, Participant, Rate
from django.shortcuts import get_object_or_404
import re


class PatchModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(PatchModelSerializer, self).__init__(*args, **kwargs)


class CurrentParticipantSerializer(PatchModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
    
    def validate_bilkent_id(self, value):
        """ Can't modify field's value after initial save """
        if self.instance and self.instance.bilkent_id != value:
            raise serializers.ValidationError("Changing Bilkent ID is not allowed.")
        return value
        
    @staticmethod
    def validate_email(email):
        """
        Check that the participant has a Bilkent domain name in the mail.
        """
        if re.search('@(ug|cs|ee|fen|unam|alumni|ug|bels|me|ctp|bim|tourism)?.bilkent.edu.tr$', email):
            return email
        else:
            raise serializers.ValidationError("You must have a valid BCC domain account.")


class ClubSerializer(PatchModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class ClubMainSerializer(ClubSerializer):
    class Meta:
        model = Club
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ClubSerializer, self).to_representation(instance)
        data['leader'] = CurrentParticipantSerializer(instance.leader).data
        del data['club_members']
        return data

class ClubMemberSerializer(ClubSerializer):
    class Meta:
        model = Club
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ClubSerializer, self).to_representation(instance)
        temp = []
        temp.append(CurrentParticipantSerializer(instance.leader).data)
        for pid in list(data['club_members']):
            queryset = Participant.objects.all()
            participant = get_object_or_404(queryset, pk=pid)
            temp.append(CurrentParticipantSerializer(participant).data)
        data['club_members'] = temp
        temp = data.copy()
        for key in temp.keys():
            if key != "club_members":
                del data[key]
        return data


class RateSerializer(serializers.ModelSerializer):
    event_name = serializers.ReadOnlyField(source='event.event_name')
    class Meta:
        model = Rate
        fields = ['event_name', 'event_score']

class EventSerializer(PatchModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventMainSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'event_place', 'event_time', 'event_points', 'event_max_capacity', 'event_description', 
                'event_tags', 'event_zoom_link', 'club', 'event_avg_score']
        read_only_fields = ['event_avg_score']

    def to_representation(self, instance):
        data = super(EventSerializer, self).to_representation(instance)
        data['club'] = ClubMainSerializer(instance.club).data
        return data


class EventParticipantSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = ['participants', 'event_current_capacity']

    def to_representation(self, instance):
        data = super(EventSerializer, self).to_representation(instance)
        temp = []
        for pid in list(data['participants']):
            queryset = Participant.objects.all()
            participant = get_object_or_404(queryset, pk=pid)
            temp.append(CurrentParticipantSerializer(participant).data)
        data['event_current_capacity'] = len(temp)
        data['participants'] = temp
        return data

class RecommendedEventSerializer(PatchModelSerializer):
    class Meta:
        model = RecommendedEvent
        fields = '__all__'
        
class RecommendedEventMainSerializer(RecommendedEventSerializer):
    class Meta:
        model = RecommendedEvent
        fields = ['event_name', 'event_place', 'event_time', 'event_points', 'event_max_capacity', 'event_description', 
                'event_tags', 'event_zoom_link', 'club', 'event_avg_score']
        read_only_fields = ['event_avg_score']

    def to_representation(self, instance):
        data = super(RecommendedEventSerializer, self).to_representation(instance)
        data['club'] = ClubMainSerializer(instance.club).data
        return data

"""class RecommendedEventParticipantSerializer(RecommendedEventSerializer):
    class Meta:
        model = RecommendedEvent
        fields = ['participants', 'event_current_capacity']

    def to_representation(self, instance):
        data = super(RecommendedEventSerializer, self).to_representation(instance)
        temp = []
        for pid in list(data['participants']):
            queryset = Participant.objects.all()
            participant = get_object_or_404(queryset, pk=pid)
            temp.append(CurrentParticipantSerializer(participant).data)
        data['participants'] = temp
        return data"""

class RecommendedEventUserSerializer(RecommendedEventSerializer):
    class Meta:
        model = RecommendedEvent
        fields = ['users']

    def to_representation(self, instance):
        data = super(RecommendedEventSerializer, self).to_representation(instance)
        temp = []
        for pid in list(data['users']):
            queryset = Participant.objects.all()
            participant = get_object_or_404(queryset, pk=pid)
            temp.append(CurrentParticipantSerializer(participant).data)
        data['users'] = temp
        return data
