# defines all Django models
from datetime import datetime, timezone
from django.db import models

from app.django_orm import utils

utils.ensure_django()

def get_current_datetime():
    return datetime.now(timezone.utc)

class MALANRawResource(models.Model):
    location = models.TextField(null=True, blank=True)
    last_updated = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    aid_type = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    animals = models.TextField(null=True, blank=True)
    volunteers_needs = models.TextField(null=True, blank=True)
    accepting = models.TextField(null=True, blank=True)
    providing = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    closed = models.BooleanField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)


