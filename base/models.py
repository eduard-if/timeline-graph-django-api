from django.db import models
from django.contrib.auth.models import User

import uuid

from colorfield.fields import ColorField


class Timeline(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    imageUrl = models.URLField(max_length=1000, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bgColor = ColorField(format='hex')
    textColor = ColorField(format='hex')
    titleColor = ColorField(format='hex')
    borderColor = ColorField(format='hex')

    def __str__(self):
        return self.title


class Item(models.Model):
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    startDate = models.DateTimeField(null=False, blank=False)
    endDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
