from django.db import models


class Event(models.Model):
    id = models.CharField(max_length=200, editable=True, primary_key=True)


class Realtime(models.Model):
    id = models.CharField(max_length=200, editable=True, primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    language = models.CharField(max_length=8)
    message = models.CharField(max_length=2048)

    def __str__(self):
        return self.message
