from django.urls import path
from .views import MainPageView, PostListView

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("posts/", PostListView.as_view(), name="post_list"),
]
