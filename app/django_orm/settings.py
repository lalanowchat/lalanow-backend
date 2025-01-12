import environ
import os

env = environ.Env(DEBUG=(bool, False))

from dotenv import load_dotenv

load_dotenv()

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_TZ = True

DATABASES = {"default": env.db()}

# see: https://docs.djangoproject.com/en/4.2/ref/databases/#connection-management
CONN_HEALTH_CHECKS = True
CONN_MAX_AGE = 20  # I believe the default Postgres timeout is 30 seconds
INSTALLED_APPS = ["app.django_orm.content.config.DjangoConfig"]
