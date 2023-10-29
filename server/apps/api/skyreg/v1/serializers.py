from rest_framework import serializers
from apps.api.skyreg.models import Applications

class ApplicationsAPI(serializers.ModelSerializer):

  class Meta:
    model = Applications
    fields = "__all__"
