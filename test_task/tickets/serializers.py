from datetime import datetime

from rest_framework.validators import UniqueTogetherValidator

from .models import Station, Passenger, Ticket
from rest_framework import serializers


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['country', 'area', 'name']
        validators = [
            UniqueTogetherValidator(
                queryset=Station.objects.all(),
                fields=['country', 'area', 'name']
            )
        ]


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = ['name']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['destination', 'departure_place', 'departure_date', 'passenger', 'price']

    def validate(self, data):
        if data["departure_place"] == data["destination"]:
            raise serializers.ValidationError({"destination": "destination place is the same as departure"})

        if data["departure_date"] < datetime.today().date():
            raise serializers.ValidationError({"departure_date": "departure_date can't be in the past"})
        return data
