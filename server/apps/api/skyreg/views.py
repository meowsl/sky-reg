from django.shortcuts import render
from rest_framework import generics
from .v1.serializers import ApplicationsAPI, RNDCabinetsAPI, KRDCabinetsAPI, SCHCabinetsAPI
from .models import Applications, RNDCabinets, KRDCabinets, SCHCabinets


class RNDCabinetsAPIView(generics.ListAPIView):
  queryset = RNDCabinets.objects.all()
  serializer_class = RNDCabinetsAPI

class KRDCabinetsAPIView(generics.ListAPIView):
  queryset = KRDCabinets.objects.all()
  serializer_class = KRDCabinetsAPI

class SCHCabinetsAPIView(generics.ListAPIView):
  queryset = SCHCabinets.objects.all()
  serializer_class = SCHCabinetsAPI