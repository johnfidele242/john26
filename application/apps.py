# apps.py
from django.apps import AppConfig

class TonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'application'

    def ready(self):
        import application.signals
