from rest_framework import views, generics
from .serializers import (
  RNDCabinetsAPI,
  KRDCabinetsAPI,
  SCHCabinetsAPI,
  KRDScheduleAPI,
  RNDScheduleAPI,
  SCHScheduleAPI
  )
from apps.api.skyreg.models import (
  RNDCabinets,
  KRDCabinets,
  SCHCabinets,
  KRDSchedule,
  RNDSchedule,
  SCHSchedule
  )


class RNDCabinetsListAPI(generics.ListAPIView):
  queryset = RNDCabinets.objects.all()
  serializer_class = RNDCabinetsAPI

class KRDCabinetsListAPI(generics.ListAPIView):
  queryset = KRDCabinets.objects.all()
  serializer_class = KRDCabinetsAPI

class SCHCabinetsListAPI(generics.ListAPIView):
  queryset = SCHCabinets.objects.all()
  serializer_class = SCHCabinetsAPI

class KRDScheduleListAPI(generics.ListAPIView):
  queryset = KRDSchedule.objects.all()
  serializer_class = KRDScheduleAPI

class RNDScheduleListAPI(generics.ListAPIView):
  queryset = RNDSchedule.objects.all()
  serializer_class = RNDScheduleAPI

class SCHScheduleListAPI(generics.ListAPIView):
  queryset = SCHSchedule.objects.all()
  serializer_class = SCHScheduleAPI
