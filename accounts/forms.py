# Importing necessary modules
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Employee

# Custom form for creating an employee, extending UserCreationForm
class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # Extending Meta class of UserCreationForm
        model = Employee  # Setting model to Employee
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']  # Fields to be displayed in the form for creating an employee

# Custom form for authentication, extending AuthenticationForm
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:  # Defining meta options for the form
        model = Employee  # Setting model to Employee
        fields = ['username', 'password']  # Fields to be displayed in the authentication form
