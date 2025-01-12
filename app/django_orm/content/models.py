# defines all Django models
from datetime import datetime, timezone
from django.db import models

from app.django_orm import utils

utils.ensure_django()


def get_current_datetime():
    return datetime.now(timezone.utc)

