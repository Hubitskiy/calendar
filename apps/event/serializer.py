from rest_framework import serializers
from .models import Event
from .utils import DateSendInvitation
from datetime import datetime
from rest_framework.exceptions import ValidationError
import pytz


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
    event_date = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S'
    )

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def validate(self, data):
        date_send_invitations = DateSendInvitation(data)

        if date_send_invitations() < datetime.now(tz=pytz.UTC):
            raise ValidationError("Sending date cannot be less than the current")

        return super().validate(data)


class RetrieveEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        depth = 0

    def update(self, instance, validated_data):
        instance.events_title = validated_data.get("events_title", instance.events_title)
        instance.description = validated_data.get("description", instance.description)
        instance.time_period = validated_data.get("time_period", instance.time_period)
        instance.event_date = validated_data.get("event_date", instance.event_date)
        instance.is_sent = validated_data.get("is_sent", instance.is_sent)
        instance.is_ended = validated_data.get("is_ended", instance.is_ended)
        instance.save()
        return instance
