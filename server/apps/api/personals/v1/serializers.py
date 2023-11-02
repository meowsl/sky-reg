from rest_framework import serializers
from apps.api.personals.models import Applications, PatientsCards

class ApplicationsAPI(serializers.ModelSerializer):

  class Meta:
    model = Applications
    fields = "__all__"

class PatientsCardsAPI(serializers.ModelSerializer):

  class Meta:
    model = PatientsCards
    fields = "__all__"
