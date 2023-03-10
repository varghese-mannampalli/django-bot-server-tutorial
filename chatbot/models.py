from __future__ import unicode_literals

from django.db import models

class Buttons (models.Model):
    text = models.CharField(max_length=31)
    calls = models.IntegerField()

    def __str__(self):
        return self.name
