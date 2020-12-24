from django.urls import path, include
from django.conf.urls import url
from .views import ParticipantViewSet, ClubViewSet, EventViewSet, RecommendedEventViewSet, LoginView, RegisterView, ClubMembersView, EventParticipantsView, RecommendedEventParticipantsView, RecommendedEventUsersView, SelectedEventsView
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls.static import static
from django.conf import settings


router = SimpleRouter()
router.register(r'participants', ParticipantViewSet, basename='participants')
router.register(r'clubs', ClubViewSet, basename='clubs')
router.register(r'events', EventViewSet, basename='events')
router.register(r'recommendedevents', RecommendedEventViewSet, basename='recommendedevents')

urlpatterns = [
    path(r'viewset/', include(router.urls)),
    path(r'viewset/<pk>/', include(router.urls)),
    path(r'auth/login', LoginView.as_view()),
    path(r'auth/register', RegisterView.as_view()),
    path(r'club/members', ClubMembersView.as_view()),
    path(r'event/participants', EventParticipantsView.as_view()),
    path(r'viewset/participants/<pk>/recommended_events', RecommendedEventParticipantsView.as_view()),
    path(r'viewset/users/<pk>/recommended_events', RecommendedEventUsersView.as_view()),
    path(r'viewset/participants/<pk>/selected_events', SelectedEventsView.as_view())
]
