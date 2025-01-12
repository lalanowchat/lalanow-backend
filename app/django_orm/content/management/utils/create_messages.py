from pathlib import Path
import importlib.resources
import pandas as pd

import django.db
import django.db.models

from app import data
from app.django_orm.content import models as django_models


def load_messages():
    messages_file = importlib.resources.files(data) / "dummy_chat_messages.csv"

    messages_df = pd.read_csv(messages_file)

    for index, row in messages_df.iterrows():
        contact_uuid = row["contact_uuid"]
        text = row["text"]
        created_at = row["created_at"]

        django_models.Message.objects.get_or_create(
            contact_uuid=contact_uuid, text=text, created_at=created_at
        )
        message_count = django_models.Message.objects.all().count()
    return message_count
