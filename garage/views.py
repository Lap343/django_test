from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CarSerializer, TruckSerializer, BoatSerializer
from .models import Car, Truck, Boat


class CarView(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.request.user.car.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TruckView(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.request.user.truck.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BoatView(viewsets.ModelViewSet):
    serializer_class = BoatSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.request.user.boat.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
