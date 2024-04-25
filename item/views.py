# Import necessary Django classes for various view types and authentication.
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Item
from store.models import Store

# A view to update an existing item. Requires the user to be logged in.
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "item/update_item.html" # Specifies the template used to render the update form.
    success_url = reverse_lazy('item:index')    # Redirects to the 'index' URL of the 'item' app on successful update.

# A view to delete an existing item. Requires the user to be logged in.
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('item:index')    # Redirects to the 'index' URL of the 'item' app on successful deletion.

# A view that combines listing items and creating a new item. Requires the user to be logged in.
class ListAndCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = [
        "name",
        "type",
        "serial",
        "cpu",
        "gpu",
        "ram",
    ]   # Fields included in the creation form.
    template_name = "item/create.html"  # Specifies the template used for the view.
    success_url = reverse_lazy('item:index')    # Redirects to the 'index' URL of the 'item' app on successful creation.

    def form_valid(self, form):
        # Logic to handle when the form is valid.
        form.instance.added_by = self.request.user  # Automatically set the user who added the item.
        # Increase the number of items in the store associated with the item being created.
        store = Store.objects.get(name=form.instance.item_store).number_of_items
        Store.objects.filter(name=form.instance.item_store).update(number_of_items=store + form.instance.item_num)
        return super().form_valid(form)

    # Added additional context to the template.
    def get_context_data(self, **kwargs):
        context = super(ListAndCreate, self).get_context_data(**kwargs)
        # Add the item list to the context
        context["item_list"] = self.model.objects.all()
        return context

# A view for listing all items and viewing details of a specific item. Requires the user to be logged in.
class ListAndDetail(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item/item_list.html"   # Specifies the template used to render the item details.

# A view to search for items based on certain criteria. Requires the user to be logged in.
class ItemSearchView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "item/create.html"  # Likely a typo, should be a template for listing or searching items.
