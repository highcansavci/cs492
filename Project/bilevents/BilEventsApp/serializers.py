from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Club, Event, RecommendedEvent, ClubLeader
import re


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
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

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class ClubLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubLeader
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
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