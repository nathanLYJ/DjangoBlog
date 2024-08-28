from django.urls import path
from .views import (
    MainPageView,
)
from . import views

app_name = "blog"

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/new/", views.PostCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "category/<slug:slug>/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path("tag/<slug:slug>/", views.TagDetailView.as_view(), name="tag_detail"),
    path("search/", views.PostSearchView.as_view(), name="post_search"),
    path(
        "comment/<int:pk>/delete/",
        views.blog_comment_delete,
        name="blog_comment_delete",
    ),
]
