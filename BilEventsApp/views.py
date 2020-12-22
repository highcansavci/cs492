from .models import Club, Event, RecommendedEvent, Participant
from .serializers import CurrentParticipantSerializer, ClubSerializer, EventSerializer, RecommendedEventSerializer, ClubMemberSerializer, ClubMainSerializer, EventMainSerializer, EventParticipantSerializer, RecommendedEventMainSerializer, RecommendedEventParticipantSerializer, RecommendedEventUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from django.core.exceptions import SuspiciousOperation


# Create your views here.

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = CurrentParticipantSerializer
    #permission_classes = [IsAuthenticated | IsAdminUser]
    lookup_field = 'bilkent_id'

    def perform_update(self, serializer):
        serializer.save()


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def get(request):
        if str(request.GET['bilkent_id']).isdigit() and len(str(request.GET['bilkent_id'])) == 8:
            user = get_object_or_404(Participant, bilkent_id=request.GET['bilkent_id'])
            if user.password == request.GET['password']:
                serializer = CurrentParticipantSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

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
    serializer_class = ClubMainSerializer
    lookup_field = 'club_name'

class ClubMembersView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def get(request):
        club = get_object_or_404(Club, club_name=request.GET['club_name'])
        serializer = ClubMemberSerializer(club)
        return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventMainSerializer
    lookup_field = 'event_name'

class EventParticipantsView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def get(request):
        event = get_object_or_404(Event, event_name=request.GET['event_name'])
        serializer = EventParticipantSerializer(event)
        return Response(serializer.data)

class SelectedEventsView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def get(request):
        participant = get_object_or_404(Participant, bilkent_id=request.GET['bilkent_id'])
        selected_events = participant.event_participants.all()
        serializer = EventMainSerializer(selected_events, many=True)
        return Response(serializer.data)

class RecommendedEventViewSet(viewsets.ModelViewSet):
    queryset = RecommendedEvent.objects.all()
    serializer_class = RecommendedEventMainSerializer
    lookup_field = 'event_name'

class RecommendedEventParticipantsView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def get(request):
        recommended_event = get_object_or_404(RecommendedEvent, event_name=request.GET['event_name'])
        serializer = RecommendedEventParticipantSerializer(recommended_event)
        return Response(serializer.data)

class RecommendedEventUsersView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def get(request):
        recommended_event = get_object_or_404(RecommendedEvent, event_name=request.GET['event_name'])
        serializer = RecommendedEventUserSerializer(recommended_event)
        return Response(serializer.data)