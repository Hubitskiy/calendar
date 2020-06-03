from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from .serializer import CreateEventSerializer, RetrieveEventSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .utils import DateSendInvitation
from logging import warning
from .models import Event


class EventCreateView(CreateAPIView):

    serializer_class = CreateEventSerializer
    permission_classes = [IsAuthenticated]

    def _perform_create(self, serializer):
        validated_data = serializer.validated_data
        get_date_to_send_invitation = DateSendInvitation(validated_data)
        validated_data["user"] = self.request.user
        validated_data["date_to_send_invitations"] = get_date_to_send_invitation()
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class RetrieveView(RetrieveModelMixin, GenericViewSet):

    serializer_class = RetrieveEventSerializer
    permission_classes = [IsAuthenticated]
    queryset = Event.objects

    def retrieve(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
