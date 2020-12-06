from rest_framework import serializers
import django.core.serializers
from .models import Club, Event, RecommendedEvent, Participant
from django.shortcuts import get_object_or_404
import re


class CurrentParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
    @staticmethod
    def validate_email(email):
        """
        Check that the participant has a Bilkent domain name in the mail.
        """
        if re.search('@(ug|cs|ee|fen|unam|alumni|ug|bels|me|ctp|bim|tourism)?.bilkent.edu.tr$', email):
            return email
        else:
            raise serializers.ValidationError("You must have a valid BCC domain account.")

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ClubSerializer, self).to_representation(instance)
        data['leader'] = CurrentParticipantSerializer(instance.leader).data
        temp = []
        for pid in list(data['participants']):
            queryset = Participant.objects.all()
            participant = get_object_or_404(queryset, pk=pid)
            temp.append(CurrentParticipantSerializer(participant).data)
        data['participants'] = temp
        return data

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super(ClubSerializer, self).to_representation(instance)
        data['club'] = CurrentParticipantSerializer(instance.club).data
        temp = []
        for pid in list(data['participants']):
            queryset = Participant.objects.all()
            participant = get_object_or_404(queryset, pk=pid)
            temp.append(CurrentParticipantSerializer(participant).data)
        data['participants'] = temp
        return data

class RecommendedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedEvent
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super(ClubSerializer, self).to_representation(instance)
        data['club'] = CurrentParticipantSerializer(instance.club).data
        temp = []
        for pid in list(data['participants']):
            queryset = Participant.objects.all()
            participant = get_object_or_404(queryset, pk=pid)
            temp.append(CurrentParticipantSerializer(participant).data)
        data['participants'] = temp
        return data
