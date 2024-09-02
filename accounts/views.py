from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeView as DjangoPasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from .models import UserProfile


class UserSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/user_signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        messages.success(self.request, "환영합니다! 회원가입이 완료되었습니다.")
        return redirect(self.success_url)

    success_url = reverse_lazy("blog:post_list")


class CustomLoginView(LoginView):
    template_name = "accounts/user_login.html"

    def get_success_url(self):
        return reverse_lazy("blog:post_list")

    def form_invalid(self, form):
        messages.error(self.request, "로그인에 실패했습니다. 다시 시도해주세요.")
        return super().form_invalid(form)


logout = LogoutView.as_view()


class ProfileView(TemplateView):
    template_name = "blog/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ["introduction", "image", "nickname", "address", "birth_date"]
    template_name = "blog/profile_update.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, user=self.request.user)

    def test_func(self):
        return True

    def form_valid(self, form):
        return super().form_valid(form)


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy(
        "accounts:profile"
    )

    def form_valid(self, form):
        messages.success(self.request, "비밀번호가 성공적으로 변경되었습니다.")
        return super().form_valid(form)
