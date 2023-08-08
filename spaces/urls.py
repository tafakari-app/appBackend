from django.urls import path
from . import views



urlpatterns = [
    path("", views.Feeds.as_view(), name="feeds"),
    path("create-post/", views.CreatePost.as_view(), name="create_post"),
    path("<pk>/", views.FeedsDetails.as_view(), name="post_details"),
    path("like-post/<post_id>/", views.LikePost.as_view(), name="like_post"),
]
