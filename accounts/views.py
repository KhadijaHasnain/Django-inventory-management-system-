# Importing necessary modules
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import CustomAuthenticationForm, EmployeeCreationForm
from django.contrib.auth.models import User
from .models import Employee

# Create your views here.

# View for user signup
class UserCreateView(CreateView):
    form_class = EmployeeCreationForm  # Using EmployeeCreationForm for user creation
    template_name = "accounts/signup.html"  # Template for signup page
    success_url = reverse_lazy('item:index')  # Redirect URL after successful signup

# View for custom login
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm  # Using CustomAuthenticationForm for login
    template_name = 'accounts/login.html'  # Template for login page

# View for user profile
class UserDetailView(LoginRequiredMixin, DetailView):
    model = Employee  # Using Employee model for user profile
    template_name = "accounts/profile.html"  # Template for profile page
    # LoginRequiredMixin ensures user is logged in to access this view

# View for user logout
class UserLogOutView(LogoutView):
    model = Employee  # Using Employee model for logout view
    template_name = 'accounts/logout.html'  # Template for logout page
