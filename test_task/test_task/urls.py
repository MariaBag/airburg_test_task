from django.urls import include, path
from rest_framework import routers

from tickets.views import StationViewSet, PassengerViewSet, TicketsViewSet

router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)
router.register(r'passengers', PassengerViewSet)
router.register(r'tickets', TicketsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
