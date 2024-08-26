from django.urls import path
from .views import (
    MainPageView,
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
)
from . import views

app_name = "blog"

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/new/", PostCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("tag/<str:tag>/", views.blog_tag, name="blog_tag"),
    # path(
    #     "<int:pk>/comment_delete/",
    #     views.blog_comment_delete,
    #     name="blog_comment_delete",
    # ),
    # path(
    #     "<int:pk>/comment_delete/",
    #     views.blog_comment_delete,
    #     name="blog_comment_delete",
    # ),
    # path(
    #     "<int:post_id>/<int:user_id>/subscribe/",
    #     views.blog_subscribe,
    #     name="blog_subscribe",
    # ),
    # path(
    #     "<int:post_id>/<int:user_id>/unsubscribe/",
    #     views.blog_unsubscribe,
    #     name="blog_unsubscribe",
    # ),
]
