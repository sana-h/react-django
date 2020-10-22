from rest_framework import serializers
from leads.models import Lead
  

class Leadserializer (serializers.ModelSerializer):
    class Meta:
        model =Lead
        fields= "_all_"