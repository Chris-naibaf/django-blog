from django.urls import path
from . import views  # We import our created views to map them to a URL

# Mapping views
urlpatterns = [
    # Path url, view to execute, name of the path
    path("", views.index, name="index"),
]
