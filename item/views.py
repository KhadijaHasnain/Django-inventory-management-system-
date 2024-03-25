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

# View for updating an item
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "item/update_item.html"
    success_url = reverse_lazy('item:index')

# View for deleting an item
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('item:index')

# View for listing items and creating new items
class ListAndCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = [
        "name",
        "type",
        "serial",
        "cpu",
        "gpu",
        "ram",
    ]
    template_name = "item/create.html"
    success_url = reverse_lazy('item:index')

    def form_valid(self, form):
        # Set the added_by field to the current user
        form.instance.added_by = self.request.user
        # Update the number of items in the associated store
        store = Store.objects.get(name=form.instance.item_store).number_of_items
        Store.objects.filter(name=form.instance.item_store).update(number_of_items=store + form.instance.item_num)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ListAndCreate, self).get_context_data(**kwargs)
        # Add the item list to the context
        context["item_list"] = self.model.objects.all()
        return context

# View for listing and viewing details of an item
class ListAndDetail(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item/item_list.html"

# View for searching items
class ItemSearchView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "item/create.html"
