from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('event_listener/', views.event_listener, name='event_listener'),
]
