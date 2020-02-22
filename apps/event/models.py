from django.db import models
from django.conf import settings


class Event(models.Model):
    events_title = models.CharField(
        verbose_name='Events name',
        max_length=30
    )
    description = models.TextField(
        verbose_name='Events description',
        max_length=150
    )
    date_to_send_invitations = models.DateTimeField(
        verbose_name='date and time to send invitation',
        auto_now_add=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field='id',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.events_title

# Create your models here.
