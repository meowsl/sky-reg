from rest_framework import views, generics
from .serializers import ApplicationsAPI
from apps.api.personals.models import Applications
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
