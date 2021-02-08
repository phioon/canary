from django.db import models


class Event(models.Model):
    id = models.CharField(max_length=200, editable=True, primary_key=True)
    variables = models.CharField(max_length=2048)

    def __str__(self):
        return self.message
