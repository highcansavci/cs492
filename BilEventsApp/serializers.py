from rest_framework import serializers
from .models import Club, Event, RecommendedEvent, ClubLeader, Participant
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

class ClubLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubLeader
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
    @staticmethod
    def validate_email(email):
        """
        Check that the participant has a Bilkent domain name in the mail.
        """
        if re.search('@(ug|cs|ee|fen|unam|alumni|ug|bels|me|ctp|bim|tourism)?.bilkent.edu.tr$', email):
            return email
        else:
            raise serializers.ValidationError("You must have a valid BCC domain account.")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class RecommendedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedEvent
        fields = '__all__'