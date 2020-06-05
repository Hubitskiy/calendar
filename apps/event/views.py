from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializer import CreateEventSerializer, RetrieveEventSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .utils import DateSendInvitation
from .custom_permission import IsSelfUser
from .models import Event


class EventCreateView(CreateAPIView):

    serializer_class = CreateEventSerializer
    permission_classes = [IsAuthenticated]

    def _perform_create(self, serializer):
        validated_data = serializer.validated_data
        get_date_to_send_invitation = DateSendInvitation(validated_data)
        validated_data["user"] = self.request.user
        validated_data["date_to_send_invitations"] = get_date_to_send_invitation()
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_event = self._perform_create(serializer)
        serializer = RetrieveEventSerializer(created_event)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class RetrieveView(RetrieveAPIView):

    serializer_class = RetrieveEventSerializer
    permission_classes = [IsAuthenticated, IsSelfUser]
    queryset = Event.objects


class ListView(ListModelMixin, GenericViewSet):

    serializer_class = RetrieveEventSerializer
    permission_classes = [IsAuthenticated]
    queryset = Event.objects

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
