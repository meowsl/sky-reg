from rest_framework import views, generics
from .serializers import ApplicationsAPI, CabinetsAPI
from apps.api.skyreg.models import Applications, Cabinets

class ApplicationsAPIView(generics.ListAPIView):
  queryset = Applications.objects.all()
  serializer_class = ApplicationsAPI

class ApplicationsCreateAPIView(generics.CreateAPIView):
  serializers_class = ApplicationsAPI

class CabinetsAPIView(generics.ListAPIView):
  queryset = Cabinets.objects.all()
  serializer_class = CabinetsAPI

