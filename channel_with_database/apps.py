from django.apps import AppConfig


class ChannelWithDatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'channel_with_database'
