from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
    OPEN = "OPEN",
    CLOSED = "CLOSED",


class Advertisement(models.Model):
    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )








