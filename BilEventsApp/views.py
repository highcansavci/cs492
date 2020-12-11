from .models import Club, Event, RecommendedEvent, Participant
from .serializers import CurrentParticipantSerializer, ClubSerializer, EventSerializer, RecommendedEventSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from django.contrib.auth import authenticate


# Create your views here.

class SelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_admin


class LeaderOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user in Club.objects.all()
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.club_leader or request.user.is_admin

class EventLeaderOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.club.club_leader or request.user.is_admin


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = CurrentParticipantSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]
    lookup_field = 'bilkent_id'


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def get(request):
        user = get_object_or_404(Participant, bilkent_id=request.GET['bilkent_id'])
        if user.password == request.GET['password']:
            serializer = CurrentParticipantSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    lookup_field = 'club_name'

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAdminUser]
        elif self.action in ('get', 'retrieve'):
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = [LeaderOrAdmin]
        return super(self.__class__, self).get_permissions()

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'event_name'

    def get_permissions(self):
        if self.action in ('get', 'retrieve'):
            self.permission_classes = [EventLeaderOrAdmin]
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(self.__class__, self).get_permissions()


class RecommendedEventViewSet(viewsets.ModelViewSet):
    queryset = RecommendedEvent.objects.all()
    serializer_class = RecommendedEventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'event_name'