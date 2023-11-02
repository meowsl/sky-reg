from rest_framework import views, generics
from .serializers import RNDCabinetsAPI, KRDCabinetsAPI, SCHCabinetsAPI
from apps.api.skyreg.models import RNDCabinets, KRDCabinets, SCHCabinets


class RNDCabinetsAPIView(generics.ListAPIView):
  queryset = RNDCabinets.objects.all()
  serializer_class = RNDCabinetsAPI

class KRDCabinetsAPIView(generics.ListAPIView):
  queryset = KRDCabinets.objects.all()
  serializer_class = KRDCabinetsAPI

class SCHCabinetsAPIView(generics.ListAPIView):
  queryset = SCHCabinets.objects.all()
  serializer_class = SCHCabinetsAPI

