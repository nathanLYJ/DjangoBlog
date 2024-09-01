# DjangoBlog Project

## ERD
[![ERD](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/DjangoBlog_ERD.PNG)](https://dbdiagram.io/d/66cd67353f611e76e993d6c2)

## WBS
[![WBS](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/DjangoBlog_WBS.PNG)](https://github.com/users/nathanLYJ/projects/3/views/2)

## Main
![Main](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/main%ED%99%94%EB%A9%B4.PNG)

## Blog
![blog_logout](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%9B%84%20blog%20%ED%99%94%EB%A9%B4.PNG)

## Blog_detail
![blog_detail](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/%EB%B8%94%EB%A1%9C%EA%B7%B8%20%EC%83%81%EC%84%B8%2C%20%EB%8C%93%EA%B8%80%2C%20%EB%8B%B5%EA%B8%80.PNG)

## Blog_signup
![blog_signup](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/%ED%9A%8C%EC%9B%90%20%EA%B0%80%EC%9E%85.PNG)


## URL 구조
주어진 Django URL 패턴들을 표로 정리하겠습니다. 각 앱의 `app_name`과 함께 해당 URL 패턴들을 정리하겠습니다.

| **App Name** | **URL Pattern** | **View** | **Name** |
|--------------|-----------------|----------|----------|
| **accounts** | `signup/` | `UserSignupView.as_view()` | `user_signup` |
| **accounts** | `login/` | `CustomLoginView.as_view()` | `user_login` |
| **accounts** | `logout/` | `views.logout` | `logout` |
| **accounts** | `profile/` | `views.ProfileView.as_view()` | `profile` |
| **accounts** | `profile/update/` | `views.ProfileUpdateView.as_view()` | `profile_update` |
| **accounts** | `password_change/` | `CustomPasswordChangeView.as_view()` | `password_change` |
| **accounts** | `password_change/done/` | `PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html")` | `password_change_done` |
| **blog** | `""` | `MainPageView.as_view()` | `main` |
| **blog** | `posts/` | `views.PostListView.as_view()` | `post_list` |
| **blog** | `posts/new/` | `views.PostCreateView.as_view()` | `post_new` |
| **blog** | `posts/<int:pk>/` | `views.PostDetailView.as_view()` | `post_detail` |
| **blog** | `posts/<int:pk>/edit/` | `views.PostUpdateView.as_view()` | `post_edit` |
| **blog** | `posts/<int:pk>/delete/` | `views.PostDeleteView.as_view()` | `post_delete` |
| **blog** | `posts/<int:pk>/comment/` | `views.add_comment` | `add_comment` |
| **blog** | `posts/<int:post_pk>/comment/<int:comment_pk>/reply/` | `views.add_reply` | `add_reply` |
| **blog** | `category/<int:pk>/` | `views.CategoryDetailView.as_view()` | `category_detail` |
| **blog** | `search/` | `views.PostSearchView.as_view()` | `post_search` |
| **blog** | `comment/<int:pk>/delete/` | `views.blog_comment_delete` | `delete_comment` |
| **chatgpt** | `chat/` | `views.ChatView.as_view()` | `chatgpt` |
| **config** | `admin/` | `admin.site.urls` | N/A |
| **config** | `""` | `MainPageView.as_view()` | `main` |
| **config** | `blog/` | `include("blog.urls")` | `블로그 uurl` |
| **config** | `accounts/` | `include("accounts.urls")` | `계정 url` |
| **config** | `chatgpt/` | `include("chatgpt.urls")` | `AI url` |
