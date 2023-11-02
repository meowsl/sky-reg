from rest_framework import views, generics
from .serializers import ApplicationsAPI, PatientsCardsAPI
from apps.api.personals.models import Applications, PatientsCards

class ApplicationsAPIView(generics.ListAPIView):
  queryset = Applications.objects.all()
  serializer_class = ApplicationsAPI

class ApplicationsCreateAPIView(generics.CreateAPIView):
  serializers_class = ApplicationsAPI

class PatientsCardsAPIView(generics.ListAPIView):
  queryset = PatientsCards.objects.all()
  serializer_class = PatientsCardsAPI