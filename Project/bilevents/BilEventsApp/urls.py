from django.urls import path, include
from .views import UserViewSet, ClubLeaderViewSet, ClubViewSet, EventViewSet, RecommendedEventViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('participants', UserViewSet, basename='participants')
router.register('leaders', ClubLeaderViewSet, basename='leaders')
router.register('clubs', ClubViewSet, basename='clubs')
router.register('events', EventViewSet, basename='events')
router.register('recommendedevents', RecommendedEventViewSet, basename='recommendedevents')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls))
]