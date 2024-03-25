# Django imports
from django.urls import path
# Project imports
from . import views

# App namespace
app_name = "accounts"

# URL patterns for account-related views
urlpatterns = [
    # URL pattern for user signup
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    
    # URL pattern for user login
    path('login/', views.CustomLoginView.as_view(), name='login'),
    
    # URL pattern for user logout
    path('logout/', views.LogoutView.as_view(), name="logout"),
    
    # URL pattern for user profile view
    path('profile/<pk>', views.UserDetailView.as_view(), name='profile'),
]
