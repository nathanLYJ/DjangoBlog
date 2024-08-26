from django.contrib import admin
from django.urls import path, include
from blog.views import MainPageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainPageView.as_view(), name="main"),
    path("blog/", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
]
