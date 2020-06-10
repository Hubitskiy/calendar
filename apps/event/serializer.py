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
