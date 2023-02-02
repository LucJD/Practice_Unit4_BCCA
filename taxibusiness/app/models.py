from django.db import models

# Create your models here.
class Taxi(models.Model):
    capacity = models.IntegerField()
    passengers = models.IntegerField()
    fare = models.FloatField()
    taxi_number = models.IntegerField(primary_key=True, default=111)
    taxi_type = models.TextField()
    notes = models.TextField()
    occupied = models.BooleanField()

    def is_occupied(self):
        return self.passengers != 0


def create_taxi(capacity, passengers, fare, type, notes=""):
    taxi = Taxi(
        capacity=capacity, passengers=passengers, fare=fare, taxi_type=type, notes=notes
    )
    taxi.occupied = taxi.is_occupied()

    top = Taxi.objects.all().last()
    if top != None:
        taxi.taxi_number = top.taxi_number + 11
    taxi.save()
    return taxi


def get_taxi(taxi_number):
    try:
        return Taxi.objects.get(taxi_number=taxi_number)
    except Taxi.DoesNotExist:
        raise ValueError("Taxi does not exist")


def send_taxi(taxi_number, passengers):
    taxi = get_taxi(taxi_number)
    if passengers > taxi.capacity or taxi.occupied == True:
        raise ValueError("Taxi occupied or too many passengers.")
    else:
        taxi.passengers = passengers
        taxi.occupied = taxi.is_occupied()
    taxi.save()
    return taxi


def end_fare(taxi_number, distance):
    taxi = get_taxi(taxi_number)
    if not taxi.occupied:
        raise ValueError("Taxi is not on fare.")
    else:

        taxi.passengers = 0
        taxi.occupied = taxi.is_occupied()

    taxi.save()
    return taxi.fare * distance


def remove_taxi(taxi_number):
    taxi = get_taxi(taxi_number)
    taxi.delete()


def find_available_taxis(capacity=0):
    available_taxis = Taxi.objects.filter(occupied=False)
    if capacity != 0:
        available_taxis = Taxi.objects.filter(capacity__gte=capacity, occupied=False)
    return available_taxis
