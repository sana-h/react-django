from leads.models import Lead
from rest_framework import viewsets , permissions
from .serializers import Leadserializer

class LeadViewset(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class=Leadserializer
    permission_classes=[
        permissions.AllowAny
    ]
    