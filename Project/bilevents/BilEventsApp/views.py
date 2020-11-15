from django.contrib.auth.models import User 
from .models import Club, Event, RecommendedEvent, ClubLeader
from .serializers import CurrentUserSerializer, ClubSerializer, ClubLeaderSerializer, EventSerializer, RecommendedEventSerializer
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


class UserViewSet(viewsets.ViewSet):

    @permission_classes([IsAuthenticated | IsAdminUser])
    def list(self, request):
        users = User.objects.all().exclude(is_superuser=True)
        serializer = CurrentUserSerializer(users, many=True)
        return Response(serializer.data)

    @permission_classes([IsAdminUser])
    def create(self, request):
        print(request.data["email"])
        serializer = CurrentUserSerializer(data=request.data)
        print(request.data['email'])
        if serializer.is_valid() and CurrentUserSerializer.validate_email(request.data['email']):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated | IsAdminUser])
    def retrieve(self, request, pk=None):
        queryset = User.objects.all().exclude(is_superuser=True)
        participant = get_object_or_404(queryset, pk=pk)
        serializer = CurrentUserSerializer(participant, {'password': participant.password})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @permission_classes([SelfOrAdmin])
    def update(self, request, pk=None):
        participant = User.objects.get(pk=pk)
        serializer = CurrentUserSerializer(participant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([SelfOrAdmin])
    def partial_update(self, request, pk=None):
        participant = User.objects.get(pk=pk)
        serializer = CurrentUserSerializer(participant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([SelfOrAdmin])
    def destroy(self, request, pk=None):
        participant = User.objects.get(pk=pk)
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClubLeaderViewSet(viewsets.ViewSet):

    @permission_classes([IsAdminUser])
    def list(self, request):
        leaders = ClubLeader.objects.all().exclude(is_superuser=True)
        serializer = ClubLeaderSerializer(leaders, many=True)
        return Response(serializer.data)

    @permission_classes([IsAdminUser])
    def create(self, request):
        serializer = ClubLeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([SelfOrAdmin])
    def retrieve(self, request, pk=None):
        queryset = ClubLeader.objects.all().exclude(is_superuser=True)
        leader = get_object_or_404(queryset, pk)
        serializer = ClubLeaderSerializer(leader)
        return Response(serializer.data)

    @permission_classes([SelfOrAdmin])
    def update(self, request, pk=None):
        leader = ClubLeader.objects.get(pk=pk)
        serializer = ClubLeaderSerializer(leader, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([SelfOrAdmin])
    def partial_update(self, request, pk=None):
        leader = ClubLeader.objects.get(pk=pk)
        serializer = ClubLeaderSerializer(leader, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([SelfOrAdmin])
    def destroy(self, request, pk=None):
        leader = ClubLeader.objects.get(pk=pk)
        leader.delete()
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
        serializer = ClubSerializer(club)
        return Response(serializer.data)

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
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated | IsAdminUser])
    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

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
        serializer = EventSerializer(recevent)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated | IsAdminUser])
    def destroy(self, request, pk=None):
        recevent = ReconmmendedEvent.objects.get(pk=pk)
        recevent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)