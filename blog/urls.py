from django.urls import path
from .views import MainPageView
from . import views

app_name = "blog"

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/new/", views.PostCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("posts/<int:pk>/comment/", views.add_comment, name="add_comment"),
    path(
        "posts/<int:post_pk>/comment/<int:comment_pk>/reply/",
        views.add_reply,
        name="add_reply",
    ),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "category/<slug:slug>/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path("tag/<str:slug>/", views.TagDetailView.as_view(), name="tag_detail"),
    path("search/", views.PostSearchView.as_view(), name="post_search"),
    path("comment/<int:pk>/delete/", views.blog_comment_delete, name="delete_comment"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path(
        "profile/update/<int:pk>/",
        views.ProfileUpdateView.as_view(),
        name="profile_update",
    ),
]
