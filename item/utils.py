from django.utils.crypto import get_random_string
import re
from django.db.models import Q

# Function to generate a random string
def random_string_generator():
    return get_random_string(length=10, allowed_chars="ABCDEF0123456789")

# Function to generate a unique item ID
def unique_item_id_generator(instance):
    # Generate a random string
    item_new_id = random_string_generator()

    # Get the class of the instance
    Item = instance.__class__

    # Check if any other item with the same ID exists
    qs_exists = Item.objects.filter(item_id=item_new_id).exists()

    # If another item with the same ID exists, generate a new ID
    if qs_exists:
        return unique_item_id_generator(instance)
    
    # Return the unique item ID
    return item_new_id
