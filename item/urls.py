# Import path function from django.urls to define URL patterns.
# Import views from the local views module where the view logic is defined.
from django.urls import path
from . import views

# Define the application namespace as 'item'. This allows you to use namespaced URLs in templates, which is useful for distinguishing URLs from different apps.
app_name = "item"

# Define a list of URL patterns. Each pattern is associated with a view and a name for easy reference.
urlpatterns = [
    # URL pattern for the index page which lists items and includes a form to create a new item.
    # It uses the ListAndCreate view and is accessible via both the root URL ('') and explicitly through '/create/'.
    path('', views.ListAndCreate.as_view(), name='index'),
    path('create/', views.ListAndCreate.as_view(), name='create'),
    # URL pattern for deleting an item. It expects a primary key (pk) for the item to identify which item to delete.
    # ItemDeleteView is likely set up to handle the deletion process.
    path('delete-item/<pk>/', views.ItemDeleteView.as_view(), name='delete'),
    # URL pattern for viewing details of a specific item. It also expects a primary key (pk).
    # ListAndDetail is likely a view that shows both details of a single item and a list of other items or related information.
    path('item/<pk>/', views.ListAndDetail.as_view(), name='details'),
    # URL pattern for a search functionality within the item app.
    # ItemSearchView is configured to handle search queries and display results.
    path('search/', views.ItemSearchView.as_view(), name='search')
]
