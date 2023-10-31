from rest_framework import serializers
from apps.api.skyreg.models import Applications, Cabinets

class ApplicationsAPI(serializers.ModelSerializer):

  class Meta:
    model = Applications
    fields = "__all__"

class CabinetsAPI(serializers.ModelSerializer):

  class Meta:
    model = Cabinets
    fields = "__all__"