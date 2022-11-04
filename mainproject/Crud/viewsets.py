from rest_framework import viewsets
from . import models
from . import serializers

class ReportViewset(viewsets.ModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer


# List(), retrieve(), create(), update(), destroy()