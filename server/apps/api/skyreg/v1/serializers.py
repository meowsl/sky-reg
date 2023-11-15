from rest_framework import serializers
from apps.api.skyreg.models import (
  RNDCabinets,
  KRDCabinets,
  SCHCabinets,
  KRDSchedule,
  RNDSchedule,
  SCHSchedule,
  Cabinets)

# Кабинеты
class RNDCabinetsAPI(serializers.ModelSerializer):
  class Meta:
    model = RNDCabinets
    fields = "__all__"

class KRDCabinetsAPI(serializers.ModelSerializer):
  class Meta:
    model = KRDCabinets
    fields = "__all__"

class SCHCabinetsAPI(serializers.ModelSerializer):
  class Meta:
    model = SCHCabinets
    fields = "__all__"

# Расписание
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
  class Meta:
    model = Cabinets
    fields = "__all__"