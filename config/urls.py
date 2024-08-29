from django.contrib import admin
from django.urls import path, include
from blog.views import MainPageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainPageView.as_view(), name="main"),
    path("blog/", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
