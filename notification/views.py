from django.db.models import Q
from django.http import HttpResponse
from django.core import serializers as django_serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from . import serializers
from collections import OrderedDict
import json

from .classes.NotificationManager import NotificationManager



@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def event_listener(request):
    payload = request.body
    data = json.loads(payload)
    res_obj = {'status': status.HTTP_200_OK}

    if data['eventid'].startswith('notification'):
        notification_manager(data)

    return Response(status=res_obj['status'])


def notification_manager(data):
    notification = NotificationManager()
    notification.notificationmanager(data)
