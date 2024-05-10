from datetime import datetime
from random import randint

from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

from .models import Station, Passenger, Ticket
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_staff=False,
            is_superuser=False
        )
        return user


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


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['destination', 'departure_place', 'departure_date', 'passenger', 'price']
        read_only_fields = ['price', 'passenger']

    def validate(self, data):
        if data["departure_place"] == data["destination"]:
            raise serializers.ValidationError({"destination": "destination place is the same as departure"})

        if data["departure_date"] < datetime.today().date():
            raise serializers.ValidationError({"departure_date": "departure_date can't be in the past"})
        return data

    def create(self, validated_data):
        validated_data['price'] = randint(100, 500)
        return super().create(validated_data)


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    tickets = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ticket-detail'
    )

    class Meta:
        model = Passenger
        fields = ['user_id', 'tickets']
