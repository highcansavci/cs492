from django.urls import path, include
from django.conf.urls import url
from .views import ParticipantViewSet, ClubViewSet, EventViewSet, LoginView, RegisterView, ClubMembersView, RecommendedEventsView, SelectedEventsView, ClubLeaderView, SelectedPastEventsView, EventParticipantsView, RateEventsView
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls.static import static
from django.conf import settings


router = SimpleRouter()
router.register(r'participants', ParticipantViewSet, basename='participants')
router.register(r'clubs', ClubViewSet, basename='clubs')
router.register(r'events', EventViewSet, basename='events')


urlpatterns = [
    path(r'viewset/', include(router.urls)),
    path(r'viewset/<pk>/', include(router.urls)),
    path(r'auth/login', LoginView.as_view()),
    path(r'auth/register', RegisterView.as_view()),
    path(r'club/members', ClubMembersView.as_view()),
    path(r'event/participants', EventParticipantsView.as_view()),
    path(r'viewset/participants/<pk>/recommended_events', RecommendedEventsView.as_view()),
    path(r'viewset/participants/<pk>/selected_events', SelectedEventsView.as_view()),
    path(r'viewset/participants/<pk>/rate_events', RateEventsView.as_view()),
    path(r'viewset/participants/<pk>/leader', ClubLeaderView.as_view()),
    path(r'viewset/participants/<pk>/past_events', SelectedPastEventsView.as_view()),
]
