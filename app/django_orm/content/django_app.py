import django
import django.apps


class DjangoConfig(django.apps.AppConfig):
    name = "app.django"
    verbose_name = "app Django App"
    label = "app_django"
