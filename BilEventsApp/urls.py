from django.urls import path, include
from .views import ParticipantViewSet, ClubLeaderViewSet, ClubViewSet, EventViewSet, RecommendedEventViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'participants', ParticipantViewSet, basename='participants')
router.register(r'leaders', ClubLeaderViewSet, basename='leaders')
router.register(r'clubs', ClubViewSet, basename='clubs')
router.register(r'events', EventViewSet, basename='events')
router.register(r'recommendedevents', RecommendedEventViewSet, basename='recommendedevents')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]