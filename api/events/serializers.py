from rest_framework import serializers
from events import models as event_model


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event_model.Event
        fields = '__all__'