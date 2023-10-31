from django.shortcuts import render
from rest_framework import generics
from .v1.serializers import ApplicationsAPI, CabinetsAPI
from .models import Applications, Cabinets

class ApplicationsAPIView(generics.ListAPIView):
  queryset = Applications.objects.all()
  serializers_class = ApplicationsAPI

class ApplicationsCreateAPIView(generics.CreateAPIView):
  queryset = Applications.objects.all()
  serializers_class = ApplicationsAPI

class CabinetsAPIView(generics.ListAPIView):
  queryset = Cabinets.objects.all()
  serializer_class = CabinetsAPI