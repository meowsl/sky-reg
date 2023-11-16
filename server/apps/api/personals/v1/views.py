from rest_framework import views, generics
from .serializers import ApplicationsAPI
from apps.api.personals.models import Applications

class ApplicationsCreateAPIView(generics.CreateAPIView):
  serializer_class = ApplicationsAPI

class ApplicationsAPIView(generics.ListAPIView):
  queryset = Applications.objects.all()
  serializer_class = ApplicationsAPI


