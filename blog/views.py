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


# 포스트 리스트
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10  # 페이지당 10개의 포스트


# 포스트 상세
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_object(self):
        with transaction.atomic():
            obj = self.model.objects.select_for_update().get(pk=self.kwargs["pk"])
            obj.view_count = F("view_count") + 1
            obj.save()

            # 업데이트된 객체를 다시 가져옵니다
            obj.refresh_from_db()

        return obj


# 포스트 생성
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# 포스트 수정
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


# 포스트 삭제
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/post_delete.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user


# 카테고리 리스트
class CategoryListView(ListView):
    model = Category
    template_name = "blog/category_list.html"
    context_object_name = "categories"


# 카테고리 상세
class CategoryDetailView(DetailView):
    model = Category
    template_name = "blog/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = self.object.posts.all()
        return context


# 태그 리스트
class TagListView(ListView):
    model = Tag
    template_name = "blog/tag_list.html"
    context_object_name = "tags"


# 태그 상세
class TagDetailView(DetailView):
    model = Tag
    template_name = "blog/tag_detail.html"
    context_object_name = "tag"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = self.object.posts.all().order_by("-created_at")

        paginator = Paginator(posts, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["posts"] = page_obj
        context["total_posts"] = posts.count()

        related_tags = (
            Tag.objects.filter(posts__in=posts).exclude(pk=self.object.pk).distinct()
        )
        context["related_tags"] = related_tags

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
def blog_comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
        comment.delete()
    return redirect("blog:post_detail", pk=comment.post.pk)


@login_required
def blog_subscribe(request, post_id, user_id):
    # 구독 로직 구현
    pass


@login_required
def blog_unsubscribe(request, post_id, user_id):
    # 구독 취소 로직 구현
    pass
