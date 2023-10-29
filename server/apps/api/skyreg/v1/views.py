from rest_framework import views, generics
from .serializers import ApplicationsAPI
from apps.api.skyreg.models import Applications

class ApplicationsAPIView(generics.ListAPIView):
  queryset = Applications.objects.all()
  serializer_class = ApplicationsAPI

class ApplicationsCreateAPIView(generics.CreateAPIView):
  serializers_class = ApplicationsAPI

