from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .models import Ticket, Station, Passenger
from .serializers import PassengerSerializer, StationSerializer, TicketSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [permissions.IsAdminUser]


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAdminUser]


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        passenger = Passenger.objects.filter(user_id=self.request.user.id)
        if not passenger:
            passenger = Passenger.objects.create(user_id=self.request.user.id)
        else:
            passenger = passenger[0]

        serializer.save(passenger=passenger)
