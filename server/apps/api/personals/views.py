from django.shortcuts import render
from v1.serializers import ApplicationsAPI,PatientsCardsAPI
from .models import Applications, PatientsCards

class ApplicationsAPIView(generics.ListAPIView):
  queryset = Applications.objects.all()
  serializers_class = ApplicationsAPI

class ApplicationsCreateAPIView(generics.CreateAPIView):
  queryset = Applications.objects.all()
  serializers_class = ApplicationsAPI

class PatientsCardsAPIView(generics.ListAPIView):
  queryset = PatientsCards.objects.all()
  serializer_class = PatientsCardsAPI