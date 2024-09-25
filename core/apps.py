from django.apps import AppConfig
from django.conf import settings


class CoreConfig(AppConfig):
    name = "core"

    def ready(self):
        # Create a unique index on the email field when the app starts
        collection = settings.MONGO_COLLECTION
        # Ensure that the email index is unique
        collection.create_index("email", unique=True)
