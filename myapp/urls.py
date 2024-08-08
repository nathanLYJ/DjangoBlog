from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	# 블로그 첫 페이지
	path('', views.home, name='home'),
	# 포스트 목록 페이지
	path('posts/', views.post_list, name='post_list'),
	# 포스트 상세 페이지
	path('post/<int:pk>/', views.post_detail, name='post_detail'), 
	# 포스트 작성 페이지
	path('post/new/', views.post_create, name='post_create'),
	# 포스트 수정 페이지
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	# 포스트 삭제 페이지
	path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),

	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', views.signup, name='signup'),
]