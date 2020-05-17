from rest_framework.generics import CreateAPIView
from .serializer import CreateEventSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .event_services import DateSendInvitationService
from logging import warning


class EventCreateView(CreateAPIView):

    serializer_class = CreateEventSerializer
    permission_classes = [IsAuthenticated]

    def _perform_create(self, serializer):
        validated_data = serializer.validated_data
        dates = DateSendInvitationService.get_time_and_event_date(validated_data)
        validated_data['date_to_send_invitations'] = dates()
        validated_data['user'] = self.request.user
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        validate = serializer.is_valid()

        if validate is not True:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        self._perform_create(serializer)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        return self.create(request)


