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

    def get_queryset(self):
        return super().get_queryset().prefetch_related("tags")


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
        form.instance.user = self.request.user
        response = super().form_valid(form)
        tags = self.request.POST.get("tags", "").split(",")
        self.object.tags.clear()
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name.strip())
            self.object.tags.add(tag)
        return response


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/form.html"

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.tags.clear()
        tags = self.request.POST.get("tags", "").split(",")
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name.strip())
            self.object.tags.add(tag)
        return response

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


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


class CategoryDetailView(DetailView):
    model = Category
    template_name = "blog/category_detail.html"
    context_object_name = "category"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.object.posts.all().order_by("-created_at")
        paginator = Paginator(posts, self.paginate_by)
        page_number = self.request.GET.get("page")
        context["posts"] = paginator.get_page(page_number)
        return context


class TagDetailView(DetailView):
    model = Tag
    template_name = "blog/tag_detail.html"
    context_object_name = "tag"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.object.posts.all().order_by("-created_at")
        paginator = Paginator(posts, self.paginate_by)
        page_number = self.request.GET.get("page")
        context["posts"] = paginator.get_page(page_number)
        return context


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
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  # User 모델을 직접 사용
            comment.save()
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form})


@login_required
def add_reply(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    parent_comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.user = request.user
            reply.parent_comment = parent_comment
            reply.save()
            return redirect("blog:post_detail", pk=post_pk)
    else:
        form = CommentForm()
    return render(
        request, "blog/add_reply.html", {"form": form, "parent_comment": parent_comment}
    )


@login_required
def blog_comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:  # User 모델로 비교
        post_pk = comment.post.pk
        comment.delete()
        return redirect("blog:post_detail", pk=post_pk)
    else:
        # 권한이 없는 경우의 처리
        return redirect("blog:post_detail", pk=comment.post.pk)
