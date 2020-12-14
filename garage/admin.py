from django.contrib import admin
from .models import Car, Truck, Boat

# Register your models here.
admin.site.register(Car)
admin.site.register(Truck)
admin.site.register(Boat)