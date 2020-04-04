from rest_framework import serializers
from .models import Event

class CreateEventSerializer(serializers.Serializer):

    events_title = serializers.CharField(
        max_length=30
    )
    description = serializers.CharField(
        max_length=150
    )
    time_period = serializers.ChoiceField(
        choices=Event.TIME_PERIOD, allow_blank=False
    )
    event_date = serializers.DateTimeField()

    def create(self, validated_data):
        pass