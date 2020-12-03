from django.apps import AppConfig


class ClientAppConfig(AppConfig):
    name = 'client_app'


default_app_config = 'client.apps.MyAppConfig'