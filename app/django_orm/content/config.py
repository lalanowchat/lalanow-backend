import django.apps


class DjangoConfig(django.apps.AppConfig):
    name = "app.django_orm.content"
    verbose_name = "app Django App"
    label = "app_django_orm"
    default_auto_field = "django.db.models.BigAutoField"
