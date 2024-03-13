from rest_framework import serializers
from apps.api.personals.models import (
  Applications,
  KRDSchedule,
  RNDSchedule,
  SCHSchedule,
  Cabinets
)

class ApplicationsAPI(serializers.ModelSerializer):
  class Meta:
    model = Applications
    fields = "__all__"

class KRDScheduleAPI(serializers.ModelSerializer):
  class Meta:
    model = KRDSchedule
    fields = "__all__"

class RNDScheduleAPI(serializers.ModelSerializer):
  class Meta:
    model = RNDSchedule
    fields = "__all__"

class SCHScheduleAPI(serializers.ModelSerializer):
  class Meta:
    model = SCHSchedule
    fields = "__all__"

class CabinetsAPI(serializers.ModelSerializer):
  city = serializers.CharField(source='get_city_display', read_only=True)
  class Meta:
    model = Cabinets
    fields = "__all__"