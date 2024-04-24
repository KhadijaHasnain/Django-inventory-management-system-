# Import the models module from django.db which provides the building blocks for defining database schema as Python classes.
# Import the pre_save signal from django.db.models.signals which provides hooks into various stages of a model's lifecycle.
from django.db import models
from django.db.models.signals import pre_save
# Import the unique_item_id_generator function from the local utils module.
# This function is assumed to generate a unique identifier for an item.
from .utils import unique_item_id_generator

# Define the Item model, which will represent items in the database.
class Item(models.Model):
    # Static choices to enforce data integrity and ease form rendering for various fields of the model.
    DEVICE_TYPE_CHOICES = [
        ('Mobile Device', 'Mobile Device'),
        ('Non-Portable PC', 'Non-Portable PC'),
        ('Laptop', 'Laptop'),
        ('Standalone Headset', 'Standalone Headset'),
    ]

    # Choices for CPU
    CPU_CHOICES = [
        ('I7-7700HQ', 'I7-7700HQ'),
        ('I7-8750H', 'I7-8750H'),
        ('M2 10C', 'M2 10C'),
        ('BCM2711C0', 'BCM2711C0'),
        ('6-Core Intel Core I5', '6-Core Intel Core I5'),
    ]

    # Choices for GPU
    GPU_CHOICES = [
        ('GTX 1070', 'GTX 1070'),
        ('RTX 2070', 'RTX 2070'),
    ]

    # Choices for RAM
    RAM_CHOICES = [
        ('32', '32'),
        ('16', '16'),
    ]

    # Fields to store various properties of each item. Some fields use the above choices.
    name = models.CharField(max_length=100, null=True, verbose_name="Device name")
    type = models.CharField(max_length=100, null=True, choices=DEVICE_TYPE_CHOICES, verbose_name="Device type")
    serial = models.CharField(max_length=100, null=True, verbose_name="Device Serial")
    cpu = models.CharField(max_length=100, null=True, choices=CPU_CHOICES, verbose_name="CPU")
    gpu = models.CharField(max_length=100, null=True, choices=GPU_CHOICES, verbose_name="GPU")
    ram = models.CharField(max_length=100, null=True, choices=RAM_CHOICES, verbose_name="RAM")
    item_id = models.CharField(max_length=10, verbose_name="Item ID", primary_key=True, null=False)

    # Define a string representation for instances of this model which returns the item ID.
    def __str__(self):
        return self.item_id  # String representation of the Item object

# Define a function to handle the pre_save signal for the Item model.
# This function will generate a unique item_id if it is not already set.
def pre_save_create_item_id(sender, instance, *args, **kwargs):
    if not instance.item_id:
        instance.item_id = unique_item_id_generator(instance)

# Connect the pre_save_create_item_id function to the pre_save signal for the Item model.
# This setup ensures the unique ID is generated just before the item is saved to the database.
pre_save.connect(pre_save_create_item_id, sender=Item)
