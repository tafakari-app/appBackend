from django.urls import path
from . import views

urlpatterns = [
    path("", views.JournalsAPiView.as_view(), name="journals"),
    path("create-Journal/", views.CreateJournal.as_view(), name="create-journal"),
    path("<pk>/", views.getJournalDetials.as_view(), name="details"),
]


