from rest_framework import views, generics
from .serializers import (
  ApplicationsAPI,
  KRDScheduleAPI,
  RNDScheduleAPI,
  SCHScheduleAPI,
  CabinetsAPI
  )
from apps.api.personals.models import (
  Applications,
  KRDSchedule,
  RNDSchedule,
  SCHSchedule,
  Cabinets
  )

from django_filters.rest_framework import DjangoFilterBackend

class ApplicationsCreateAPIView(generics.CreateAPIView):
  serializer_class = ApplicationsAPI

class ApplicationsAPIView(generics.ListAPIView):
  queryset = Applications.objects.all()
  serializer_class = ApplicationsAPI
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['date', 'typepr', 'city']

class ApplicationsUpdateAPIViev(generics.UpdateAPIView):
  queryset = Applications.objects.all()
  serializer_class = ApplicationsAPI

class KRDScheduleListAPI(generics.ListAPIView):
  queryset = KRDSchedule.objects.all()
  serializer_class = KRDScheduleAPI

class RNDScheduleListAPI(generics.ListAPIView):
  queryset = RNDSchedule.objects.all()
  serializer_class = RNDScheduleAPI

class SCHScheduleListAPI(generics.ListAPIView):
  queryset = SCHSchedule.objects.all()
  serializer_class = SCHScheduleAPI

class CabinetsListAPI(generics.ListAPIView):
  queryset = Cabinets.objects.all()
  serializer_class = CabinetsAPI