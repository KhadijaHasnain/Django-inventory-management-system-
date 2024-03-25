from django.template import RequestContext
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from mixins import AjaxableFormMixin  # Assuming AjaxableFormMixin is defined in the 'mixins' module
from .models import Store

# Create your views here.

# View for creating a store
class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['name', 'capacity', 'store_users']  # Fields to display in the form
    template_name = "store/create.html"  # Template for the create store page
    success_url = reverse_lazy('store:create')  # Redirect URL after successful creation

    def form_valid(self, form):
        # Set the manager of the store to the current user
        form.instance.manager = self.request.user
        return super().form_valid(form)

# View for displaying store details
class StoreDetailView(LoginRequiredMixin, DetailView):
    model = Store
    template_name = "store/details.html"  # Template for displaying store details

# View for deleting a store
class StoreDeleteView(LoginRequiredMixin, AjaxableFormMixin, DeleteView):
    model = Store
    success_url = reverse_lazy('store:list')  # Redirect URL after successful deletion
