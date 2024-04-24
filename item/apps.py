# Import AppConfig from django.apps, which is the base class for all app configurations in Django.
from django.apps import AppConfig

# Define a new configuration class named InventoryManagerConfig.
# This class inherits from AppConfig.
class InventoryManagerConfig(AppConfig):
    # Set the name of the application. This is a mandatory attribute.
    # 'name' is used by Django to identify the application.
    # It should match the Python path to the application, typically the name of the directory that holds the app.
    name = 'item'
