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
        get_date_to_send_invitation = DateSendInvitation(validated_data)
        date_to_send_invitation = get_date_to_send_invitation()
        validated_data["user"] = self.request.user
        validated_data["date_to_send_invitations"] = date_to_send_invitation
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data ,status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request)
