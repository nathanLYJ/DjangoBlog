from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "chatgpt"

urlpatterns = [
    path("chat/", views.ChatView.as_view(), name="chatgpt"),  # 채팅 URL
]
