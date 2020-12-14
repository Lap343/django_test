from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    owner = models.ForeignKey(User, related_name="car", on_delete=models.CASCADE, null=True, editable=False)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    seats = models.IntegerField()
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=50)
    current_mileage = models.IntegerField()
    service_interval = models.CharField(max_length=50)
    next_service = models.DateField(max_length=50)

    def __str__(self):
        return self.make + ', ' + self.model

class Truck(models.Model):
    owner = models.ForeignKey(User, related_name="truck", on_delete=models.CASCADE, null=True, editable=False)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    seats = models.IntegerField()
    bed_length = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=50)
    current_mileage = models.IntegerField()
    service_interval = models.CharField(max_length=50)
    next_service = models.DateField(max_length=50)

    def __str__(self):
        return self.make + ', ' + self.model


class Boat(models.Model):
    owner = models.ForeignKey(User, related_name="boat", on_delete=models.CASCADE, null=True, editable=False)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    length = models.CharField(max_length=20)
    width = models.CharField(max_length=50)
    hin = models.CharField(max_length=50)
    current_hours = models.IntegerField()
    service_interval = models.CharField(max_length=50)
    next_service = models.DateField(max_length=50)

    def __str__(self):
        return self.make + ', ' + self.model