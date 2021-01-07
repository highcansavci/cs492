from .models import Club, Event, RecommendedEvent, Participant, Rate
from .serializers import CurrentParticipantSerializer, ClubSerializer, EventSerializer, RecommendedEventSerializer, RecommendedEventMainSerializer, ClubMemberSerializer, ClubMainSerializer, EventMainSerializer, EventParticipantSerializer, RecommendedEventUserSerializer, RateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from django.core.exceptions import SuspiciousOperation, ObjectDoesNotExist
from django.utils import timezone

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


class ClubLeaderView(APIView):
    authentication_classes = ()
    permission_classes = ()
    def get(self, request, pk):
        try:
            leader = get_object_or_404(Participant, bilkent_id=pk)
            club = leader.club
            serializer = ClubMainSerializer(club)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventMainSerializer
    lookup_field = 'event_name'

    def create(self, request, *args, **kwargs):
        club = get_object_or_404(Club, club_name=request.data['club'])
        request.data['club'] = club.id 
        response = super().create(request, *args, **kwargs)
        instance = response.data
        return Response({'status': 'success', 'club name': instance['club']})
    

class PastEventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventMainSerializer
    lookup_field = 'event_name'
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(event_time__lt=timezone.now())
        return query_set


class EventParticipantsView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        event = get_object_or_404(Event, event_name=request.GET['event_name'])
        serializer = EventParticipantSerializer(event)
        return Response(serializer.data)

    def post(self, request):
        participant_list = []
        event = get_object_or_404(Event, event_name=request.data['event_name'])
        if event.event_time < timezone.now():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if type(request.data['participants']) == int:
            participant_list.append(request.data['participants'])
        elif type(request.data['participants']) == list:
            participant_list.extend(request.data['participants'])
        event.participants.set(participant_list) 
        serializer = EventParticipantSerializer(event, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        event = get_object_or_404(Event, event_name=request.data['event_name'])
        if event.event_time < timezone.now():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        participant_list = [participant.bilkent_id for participant in event.participants.all()]
        if type(request.data['participants']) == int:
            participant_list.append(request.data['participants'])
        elif type(request.data['participants']) == list:
            participant_list.extend(request.data['participants'])
        event.participants.set(participant_list) 
        serializer = EventParticipantSerializer(event, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        event = get_object_or_404(Event, event_name=request.data['event_name'])
        if event.event_time < timezone.now():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if type(request.data['participants']) == int:
            participant_list = [participant.bilkent_id for participant in event.participants.all() if request.data['participants'] != participant.bilkent_id]
        elif type(request.data['participants']) == list:
            participant_list = [participant.bilkent_id for participant in event.participants.all() if not(participant.bilkent_id  in request.data['participants'])]
        event.participants.set(participant_list) 
        serializer = EventParticipantSerializer(event, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelectedEventsView(APIView):
    authentication_classes = ()
    permission_classes = ()
    
    def get(self, request, pk):
        participant = get_object_or_404(Participant, bilkent_id=pk)
        selected_events = participant.eventinfo_set.all()
        serializer = EventMainSerializer(selected_events, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        event = get_object_or_404(Event, event_name=request.data['event_name'])
        participant_list = []
        participant = get_object_or_404(Participant, bilkent_id=pk)
        participant_list.append(participant)
        event.participants.set(participant_list) 
        serializer = EventParticipantSerializer(event, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        event = get_object_or_404(Event, event_name=request.data['event_name'])
        participant_list = [participant.bilkent_id for participant in event.participants.all()]
        participant = int(pk)
        if not(participant in participant_list):
            participant_list.append(participant)
        else:
            return Response(status=status.HTTP_409_CONFLICT)
        print(participant_list)
        event.participants.set(participant_list) 
        serializer = EventParticipantSerializer(event, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        event = get_object_or_404(Event, event_name=request.data['event_name'])
        participant_list = [participant.bilkent_id for participant in event.participants.all()]
        participant = int(pk)
        if participant in participant_list:
            participant_list.remove(participant)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        event.participants.set(participant_list) 
        serializer = EventParticipantSerializer(event, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SelectedPastEventsView(APIView):
    authentication_classes = ()
    permission_classes = ()
    
    def get(self, request, pk):
        participant = get_object_or_404(Participant, bilkent_id=pk)
        selected_events = participant.eventinfo_set.filter(event_time__lt=timezone.now())
        serializer = EventMainSerializer(selected_events, many=True)
        return Response(serializer.data)
    

class RateEventsView(APIView):
    authentication_classes = ()
    permission_classes = ()
    
    def get(self, request, pk):
        participant = get_object_or_404(Participant, bilkent_id=pk)
        rate_events = Rate.objects.filter(participant=participant)
        serializer = RateSerializer(rate_events, many=True)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        participant = get_object_or_404(Participant, bilkent_id=pk)
        selected_event = get_object_or_404(Event, event_name=request.data['event_name'])
        if selected_event.event_time < timezone.now():
            rate_events = Rate.objects.get(participant=participant, event=selected_event)
            if rate_events.event_score == 0:
                rate_events.event_score = request.data['event_score']
                serializer = RateSerializer(rate_events, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    raters = Rate.objects.filter(event=selected_event, event_score__gt=0).count()
                    temp = (selected_event.event_avg_score * raters + request.data['event_score']) / (raters + 1)
                    Event.objects.filter(event_name=selected_event.event_name).update(event_avg_score=temp)
                    return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RecommendedEventViewSet(viewsets.ModelViewSet):
    queryset = RecommendedEvent.objects.all()
    serializer_class = RecommendedEventMainSerializer
    lookup_field = 'event_name'


class RecommendedEventsView(APIView):
    authentication_classes = ()
    permission_classes = ()
    
    def get(self, request, pk):
        user = get_object_or_404(Participant, bilkent_id=pk)
        recommended_events = user.recommended_users.all()
        serializer = RecommendedEventMainSerializer(recommended_events, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        user = get_object_or_404(Participant, bilkent_id=pk)
        recevent = get_object_or_404(RecommendedEvent, event_name=request.data['event_name'])
        recevent.users = user
        serializer = RecommendedEventUserSerializer(recevent, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        recevent = get_object_or_404(RecommendedEvent, event_name=request.data['event_name'])
        user_list = [user.bilkent_id for user in recevent.users.all()]
        user = int(pk)
        if not(user in user_list):
            user_list.append(participant)
        else:
            return Response(status=status.HTTP_409_CONFLICT)
        request.data['users'] = user_list
        serializer = RecommendedEventUserSerializer(recevent, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        recevent = get_object_or_404(RecommendedEvent, event_name=request.data['event_name'])
        user_list = [user.bilkent_id for user in recevent.users.all()]
        user = int(pk)
        if user in user_list:
            user_list.remove(user)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request.data['users'] = user_list
        serializer = RecommendedEventUserSerializer(recevent, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)