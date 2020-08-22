from django.shortcuts import render
from rest_framework import viewsets
from .models import Status, Procedure
from .serializers import StatusSerializer, ProcedureSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer