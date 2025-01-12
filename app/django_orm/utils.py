import os
import threading

import django
import django.conf


DJANGO_SETUP_SEMAPHORE = threading.Semaphore()


def ensure_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.django_orm.settings")
    # This approach is slightly unreasonable, but prevents Django setup problems if ensure_django() is called while importing content/models.py.
    # Only one call to ensure_django() will acquire the semaphore at a time; the rest will terminate without taking an action.
    # Code calling ensure_django() should NOT acquire this semaphore.
    if DJANGO_SETUP_SEMAPHORE.acquire(blocking=False):
        if not django.conf.settings.configured:
            django.setup()
            assert django.apps.apps.ready, "Apps not ready, despite setup."
