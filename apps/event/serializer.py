from rest_framework import serializers


class CreateEventSerializer(serializers.Serializer):

    events_title = serializers.CharField(
        max_length=30
    )
    description = serializers.CharField(
        max_length=150
    )
