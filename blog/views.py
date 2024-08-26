from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Post


# 메인 페이지
class MainPageView(TemplateView):
    template_name = "blog/main.html"


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
