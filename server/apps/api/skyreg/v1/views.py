from rest_framework import views, generics
from .serializers import (
  KRDScheduleAPI,
  RNDScheduleAPI,
  SCHScheduleAPI,
  CabinetsAPI
  )
from apps.api.skyreg.models import (
  KRDSchedule,
  RNDSchedule,
  SCHSchedule,
  Cabinets
  )


# Расписание по городам
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
