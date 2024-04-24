# Import the admin module from Django's built-in 'contrib' package.
from django.contrib import admin
# Import the Item model from the local 'models' module within the same application.
from .models import Item
# Register your models here.
# This line makes the Item model accessible via the Django admin interface.
# By registering the model, you enable CRUD operations on Item instances from the admin panel.
admin.site.register(Item)
