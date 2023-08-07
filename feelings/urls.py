from django.urls import path
from . import views


urlpatterns = [
    path("", views.FeelingsAPIView.as_view(), name="feelings"),
]
