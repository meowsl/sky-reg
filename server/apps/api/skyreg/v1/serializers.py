from rest_framework import serializers
from apps.api.skyreg.models import RNDCabinets, KRDCabinets, SCHCabinets

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