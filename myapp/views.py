from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# 블로그 첫 페이지
def home(request):
	recent_posts = Post.objects.order_by('-created_date')[:5]

	return render(request, 'blog/home.html', {'recent_posts': recent_posts})

# 포스트 목록 페이지
def post_list(request):
	posts = Post.objects.all().order_by('-created_date')
	paginator = Paginator(posts, 1)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	return render(request, 'blog/post_list.html', {'posts': posts})

# 포스트 상세 페이지
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)

	return render(request, 'blog/post_detail.html', {'post': post})

def	signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()

	return render(request, 'registration/signup.html', {'form': form})

@login_required
def post_create(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()

			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if post.author != request.user:
		return redirect('post_detail', pk=post.pk)
	
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()

			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)

	return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if post.author != request.user:
		return redirect('post_detail', pk=post.pk)

	if request.method == 'POST':
		post.delete()
		return redirect('post_list')
	return render(request, 'blog/post_confirm_remove.html', {'post': post})



