from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from events import serializers as event_serializers
from events import models as event_model

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing event instances.
    """
    serializer_class = event_serializers.EventSerializer
    queryset = event_model.Event.objects.all()

    