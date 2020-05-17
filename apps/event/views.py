from rest_framework.generics import CreateAPIView
from .serializer import CreateEventSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .utils import DateSendInvitation


class EventCreateView(CreateAPIView):

    serializer_class = CreateEventSerializer
    permission_classes = [IsAuthenticated]

    def _perform_create(self, serializer):
        validated_data = serializer.validated_data
        add_date_to_send_invitation = DateSendInvitation(validated_data)
        add_date_to_send_invitation()
        validated_data['user'] = self.request.user
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._perform_create(serializer)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        return self.create(request)
