# jobs_integration/views.py

from rest_framework import viewsets
from .models import IntegratedJob
from .serializers import IntegratedJobSerializer

class IntegratedJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IntegratedJob.objects.all()
    serializer_class = IntegratedJobSerializer
