from django.urls import path
from . import views
from .views import UserSignupView, LoginView

app_name = "accounts"

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="user_signup"),
    path(
        "login/",
        LoginView.as_view(template_name="accounts/user_login.html"),
        name="user_login",
    ),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]
