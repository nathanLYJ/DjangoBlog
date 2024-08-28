from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag
from .forms import PostForm, CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from .models import Comment
from django.core.paginator import Paginator
from django.db import transaction


# 메인 페이지
class MainPageView(TemplateView):
    template_name = "blog/main.html"


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    ordering = ["-created_at"]
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self):
        obj = super().get_object()
        Post.objects.filter(pk=obj.pk).update(view_count=F("view_count") + 1)
        return obj

    def get_queryset(self):
        return super().get_queryset().prefetch_related("tags")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/form.html"

    def form_valid(self, form):
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()

            if "category" in form.cleaned_data:
                self.object.category = form.cleaned_data["category"]

            if "tags" in form.cleaned_data:
                self.object.tags.set(form.cleaned_data["tags"])

            self.object.save()

            return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/form.html"

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)

        # tags 처리
        if "tags" in form.cleaned_data:
            self.object.tags.set(form.cleaned_data["tags"])

        return response


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/post_delete.html"

    def test_func(self):
        return self.request.user == self.get_object().user


class CategoryListView(ListView):
    model = Category
    template_name = "blog/category_list.html"
    context_object_name = "categories"


class PaginatedDetailView(DetailView):
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.object.posts.all().order_by("-created_at")
        paginator = Paginator(posts, self.paginate_by)
        page_number = self.request.GET.get("page")
        context["posts"] = paginator.get_page(page_number)
        return context


class CategoryDetailView(PaginatedDetailView):
    model = Category
    template_name = "blog/category_detail.html"
    context_object_name = "category"


class TagDetailView(PaginatedDetailView):
    model = Tag
    template_name = "blog/tag_detail.html"
    context_object_name = "tag"


class PostSearchView(ListView):
    model = Post
    template_name = "blog/post_search.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()


@login_required
def blog_comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
        comment.delete()
    return redirect("blog:post_detail", pk=comment.post.pk)
