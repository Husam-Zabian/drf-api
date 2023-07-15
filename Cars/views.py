from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

# Create your views here.


class CarsList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer