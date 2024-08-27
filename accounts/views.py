from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


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
        # 로그인 성공 후 이동할 URL을 반환합니다.
        return reverse_lazy("blog:post_list")

    def form_invalid(self, form):
        messages.error(self.request, "로그인에 실패했습니다. 다시 시도해주세요.")
        return super().form_invalid(form)


logout = LogoutView.as_view()


def profile(request):
    return render(request, "accounts/profile.html")
