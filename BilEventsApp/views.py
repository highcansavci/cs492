from .models import Club, Event, RecommendedEvent, Participant
from .serializers import CurrentParticipantSerializer, ClubSerializer, EventSerializer, RecommendedEventSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from django.contrib.auth import authenticate


# Create your views here.

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

class RegisterView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def post(request):
        serializer = CurrentParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    lookup_field = 'club_name'

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'event_name'

class RecommendedEventViewSet(viewsets.ModelViewSet):
    queryset = RecommendedEvent.objects.all()
    serializer_class = RecommendedEventSerializer
    lookup_field = 'event_name'