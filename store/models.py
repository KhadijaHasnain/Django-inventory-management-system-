from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_store_id_generator
from accounts.models import Employee  # Importing Employee model from accounts app

# Store model definition
class Store(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Store name")  # Name of the store
    capacity = models.IntegerField(default=0, verbose_name="Capacity")  # Capacity of the store
    number_of_items = models.IntegerField(default=0)  # Number of items in the store
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="Manager")  # Manager of the store
    store_id = models.CharField(max_length=10, primary_key=True, null=False)  # Unique identifier for the store
    store_users = models.ManyToManyField(Employee)  # Users associated with the store

    def __str__(self):
        return self.name  # String representation of the store

# Signal function to generate unique store ID before saving
def pre_save_create_store_id(sender, instance, *args, **kwargs):
    if not instance.store_id:
        instance.store_id = unique_store_id_generator(instance)

# Connecting the signal to the Store model's pre_save event
pre_save.connect(pre_save_create_store_id, sender=Store)
