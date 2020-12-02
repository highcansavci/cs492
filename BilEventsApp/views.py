from .models import Club, Event, RecommendedEvent, Participant
from .serializers import CurrentParticipantSerializer, ClubSerializer, EventSerializer, RecommendedEventSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes

# Create your views here.

class SelfOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_admin


class LeaderOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user in ClubLeader.objects.all()
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.club_leader or request.user.is_admin

class EventLeaderOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.club.club_leader or request.user.is_admin


class ParticipantViewSet(viewsets.ViewSet):

    @permission_classes([IsAuthenticated | IsAdminUser])
    def list(self, request):
        participants = Participant.objects.all()
        print(participants)
        serializer = CurrentParticipantSerializer(participants, many=True)
        return Response(serializer.data)

    @permission_classes([IsAdminUser])
    def create(self, request):
        serializer = CurrentParticipantSerializer(data=request.data)
        if serializer.is_valid() and CurrentParticipantSerializer.validate_email(request.data['email']):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated | IsAdminUser])
    def retrieve(self, request, pk=None):
        queryset = Participant.objects.all()
        participant = get_object_or_404(queryset, pk=pk)
        data = {
            'id': participant.id, 
            'bilkent_id': participant.bilkent_id,
            'first_name': participant.first_name,
            'last_name': participant.last_name,
            'email': participant.email, 
            'password': participant.password
        }
        serializer = CurrentParticipantSerializer(participant, data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @permission_classes([SelfOrAdmin])
    def update(self, request, pk=None):
        participant = Participant.objects.get(pk=pk)
        serializer = CurrentParticipantSerializer(participant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([SelfOrAdmin])
    def partial_update(self, request, pk=None):
        participant = Participant.objects.get(pk=pk)
        serializer = CurrentParticipantSerializer(participant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([SelfOrAdmin])
    def destroy(self, request, pk=None):
        participant = Participant.objects.get(pk=pk)
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClubViewSet(viewsets.ViewSet):

    @permission_classes([IsAuthenticated | IsAdminUser])
    def list(self, request):
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

    @permission_classes([IsAdminUser])
    def create(self, request):
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated | IsAdminUser])
    def retrieve(self, request, pk=None):
        queryset = Club.objects.all()
        club = get_object_or_404(queryset, pk)
        data = {
            'id': club.id,
            'club_name': club.club_name, 
            'club_description': club.club_description,
            'logo': club.logo,
            'club_leader': club.club_leader,
            'club_participants': club.club_participants
        }
        serializer = ClubSerializer(club, data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @permission_classes([LeaderOrAdmin])
    def update(self, request, pk=None):
        club = Club.objects.get(pk=pk)
        serializer = ClubSerializer(leader, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([LeaderOrAdmin])
    def partial_update(self, request, pk=None):
        club = Club.objects.get(pk=pk)
        serializer = ClubSerializer(leader, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([LeaderOrAdmin])
    def destroy(self, request, pk=None):
        club = Club.objects.get(pk=pk)
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventViewSet(viewsets.ViewSet):

    @permission_classes([IsAuthenticated | IsAdminUser])
    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @permission_classes([EventLeaderOrAdmin])
    def create(self, request):
        self.check_object_permissions(self.request, request.data)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated | IsAdminUser])
    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk)
        data = {
            'id': event.id, 
            'event_name':  event.event_name,
            'event_place':  event.event_place,
            'event_time':  event.event_time,
            'event_capacity':  event.event_capacity, 
            'event_description':  event.event_description,
            'event_tags':  event.event_tags,
            'event_zoom_link':  event.event_zoom_link ,
            'participants': event.participants, 
            'club': event.club
        }
        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @permission_classes([EventLeaderOrAdmin])
    def update(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([EventLeaderOrAdmin])
    def partial_update(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([EventLeaderOrAdmin])
    def destroy(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecommendedEventViewSet(viewsets.ViewSet):

    @permission_classes([IsAuthenticated | IsAdminUser])
    def list(self, request):
        recevents = RecommendedEvent.objects.all()
        serializer = RecommendedEventSerializer(recevents, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated | IsAdminUser])
    def retrieve(self, request, pk=None):
        queryset = RecommendedEvent.objects.all()
        recevent = get_object_or_404(queryset, pk)
        data = {
            'id': recevent.id, 
            'event_name':  recevent.event_name,
            'event_place':  recevent.event_place,
            'event_time':  recevent.event_time,
            'event_capacity':  recevent.event_capacity, 
            'event_description':  recevent.event_description,
            'event_tags':  recevent.event_tags,
            'event_zoom_link':  recevent.event_zoom_link ,
            'participants': recevent.participants, 
            'club': recevent.club
        }
        serializer = RecommendedEventSerializer(recevent, data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @permission_classes([IsAuthenticated | IsAdminUser])
    def destroy(self, request, pk=None):
        recevent = RecommendedEvent.objects.get(pk=pk)
        recevent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)