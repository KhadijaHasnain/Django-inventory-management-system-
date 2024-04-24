
# Import necessary modules from Django's framework to handle settings, database migrations, models, and time utilities.
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

# Define a new migration class that Django will use to apply database changes.
class Migration(migrations.Migration):

    # Mark this migration as the initial one for the corresponding Django app.
    initial = True

    # List any dependencies this migration has on other migrations.
    # This ensures that migrations are applied in the correct order.
    dependencies = [
        ('store', '0001_initial'),   # Dependency on an initial migration in the 'store' app.
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    # List of operations to be performed by this migration.
    operations = [
        # Create a new model called 'Item' in the database.
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='Item name')),   # Name of the item, max length 100 chars.
                ('item_num', models.IntegerField(verbose_name='No. of units')), # Number of units available.
                ('date_stored', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of entry')), # Timestamp when item was stored.
                ('date_removed', models.DateTimeField(null=True)),  # Optional timestamp for when the item is removed.
                ('fragile', models.BooleanField(verbose_name='Fragile')),   # Boolean flag to indicate if the item is fragile.
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight')), # Weight of the item with precision.
                ('units', models.CharField(choices=[('kg', 'Kilograms'), ('g', 'Grams'), ('t', 'Tonnes')], max_length=20, verbose_name='Units')),   # Unit of measurement for weight.
                ('item_class', models.CharField(choices=[('A', 'Electronics'), ('B', 'Chemicals'), ('C', 'Books'), ('D', 'Clothing'), ('E', 'Food'), ('F', 'Other')], default='A', max_length=1, verbose_name='Item class')),   # Classification of the item.
                ('item_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Item ID')),    # Unique ID for the item.
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),  # Reference to the user who added the item, with CASCADE deletion policy.
                ('item_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store')),   # Reference to the store where the item is located, with CASCADE deletion policy.
            ],
        ),
    ]
