from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView

signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/user_signup.html",
    # success_url = settings.LOGIN_URL,
    success_url="blog:post_list",
)

login = LoginView.as_view(
    template_name="accounts/user_login.html",
    success_url="blog:post_list",
)
logout = LogoutView.as_view()


@login_required
def profile(request):
    return render(request, "accounts/profile.html")
