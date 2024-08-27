from django.urls import path
from . import views
from .views import UserSignupView, CustomLoginView

app_name = "accounts"

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="user_signup"),
    path("login/", CustomLoginView.as_view(), name="user_login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]
