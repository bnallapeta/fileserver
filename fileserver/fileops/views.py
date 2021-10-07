from django.shortcuts import render
from rest_framework import viewsets

from .models import Files
from .serializers import FilesSerializer

class FilesViewSet(viewsets.ModelViewSet):
    serializer_class = FilesSerializer
    queryset = Files.objects.all()