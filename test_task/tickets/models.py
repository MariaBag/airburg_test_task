from django.db import models


class Station(models.Model):
    country = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class Passenger(models.Model):
    name = models.CharField(max_length=200)


class Ticket(models.Model):
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="destination_place")
    departure_place = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="departure_place")
    departure_date = models.DateTimeField()
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
