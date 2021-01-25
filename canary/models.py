from django_engine import settings
from django.db import models


class NotificationRealtime(models.Model):
    id = models.CharField(max_length=200, editable=False, primary_key=True, unique=True)
    language = models.CharField(max_length=8)
    message = models.CharField(max_length=2048)

    objects = models.Manager()

    def __str__(self):
        return self.message
