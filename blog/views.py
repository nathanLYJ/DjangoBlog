from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# 메인 페이지
class MainPageView(TemplateView):
    template_name = "blog/main.html"


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, "blog/blog_list.html", {"posts": posts})


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/form.html"  # CreateView에서 폼 템플릿을 사용

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/form.html"  # UpdateView에서도 동일한 폼 템플릿 사용


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/post_delete.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
