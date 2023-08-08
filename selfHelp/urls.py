from . import views
from django.urls import path


urlpatterns = [
    path("", views.LibraryView.as_view(), name="library"),
]
