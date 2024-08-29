from django.urls import path
from . import views
from .views import UserSignupView, CustomLoginView, CustomPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

app_name = "accounts"

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="user_signup"),
    path("login/", CustomLoginView.as_view(), name="user_login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/update/", views.ProfileUpdateView.as_view(), name="profile_update"),
    path(
        "password_change/", CustomPasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
