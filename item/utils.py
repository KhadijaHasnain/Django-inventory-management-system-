# Import get_random_string from django.utils.crypto to generate a random sequence of characters.
from django.utils.crypto import get_random_string
import re
from django.db.models import Q

# Function to generate a random string, which serves as a part of the unique identifier.
def random_string_generator():
        # The function returns a string of 10 characters long, chosen from the specified set of uppercase letters and numbers.
    return get_random_string(length=10, allowed_chars="ABCDEF0123456789")

# The function returns a string of 10 characters long, chosen from the specified set of uppercase letters and numbers.
def unique_item_id_generator(instance):
    # Generate a random string to be potentially used as a unique item ID.
    item_new_id = random_string_generator()

    # Retrieve the class of the instance. This allows the function to be model-agnostic, working with any Django model instance.
    Item = instance.__class__

    # Check if there is an existing record in the database with the same item ID.
    qs_exists = Item.objects.filter(item_id=item_new_id).exists()

    # If a record with the same item ID already exists, recursively call the function to generate a new ID.
    # This recursion will continue until a unique ID is generated.
    if qs_exists:
        return unique_item_id_generator(instance)
    
    # Return the unique item ID after confirming it's unique.
    return item_new_id
