# DjangoBlog Project


## 목표
  1. 협업 - 간접체험 주어진 UI, CSS, 요구사항 등 똑같히 구현하려고 노력했습니다. (쉬울거라고 예상했지만 의외로 정말 너무 힘들었습니다)
  2. 기본 CBV - 대부분, 일부FBV
  3. 3단계
    * 구현 완료 - 메인페이지, 회원가입 기능, 로그인 기능, 게시글 작성 기능 구현, 게시글 목록 기능 구현, 게시글 상세보기 기능 구현, 게시글 검색 기능 구현, 게시글 수정 기능 구현, 게시글 삭제 기능 구현, 회원 관련 추가 기능, 댓글 기능, 정적 파일 정리.
    * 미구현 - 번역기능, html 17개 (한글/영어)
    * 선택사항 - 배포X, AI요약 기능O.

## 기능 명세
### 1. 사용자 관리
  * 회원가입
  * 로그인/로그아옷
  * 프로필&프로필 수정
  * 비밀번호 변경

### 2. 블로그 관리
  * 포스트 생성/수정/삭제
  * 이미지/파일 업로드
  * 카테고리 분류(관리자), 태그 분류(사용자)
  * 조회수 기능, 작성일 최신순
  * 댓글, 답글 (유저인증-삭제)
  * 검색 기능

### 3. AI 도우미
  * AI 요약

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

## ERD
[![ERD](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/DjangoBlog_ERD.PNG)](https://dbdiagram.io/d/66cd67353f611e76e993d6c2)

## WBS
[![WBS](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/DjangoBlog_WBS.PNG)](https://github.com/users/nathanLYJ/projects/3/views/2)

## Main
![Main](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/main%ED%99%94%EB%A9%B4.PNG)

## Blog
![blog_logout](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%9B%84%20blog%20%ED%99%94%EB%A9%B4.PNG)

## Blog_detail $ Blog_edit 폼 동일
![blog_detail](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/%ED%8F%AC%EC%8A%A4%ED%8A%B8%20%ED%99%94%EB%A9%B4.PNG)

## Blog_detail_user 타인 포스트 시점
![blog_detail1](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/%EB%B8%94%EB%A1%9C%EA%B7%B8%20%EC%83%81%EC%84%B8%2C%20%EB%8C%93%EA%B8%80%2C%20%EB%8B%B5%EA%B8%80.PNG)

## Blog_detail_user 본인 포스트 시점
![blog_detail2](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/post_detail_user2.PNG)

## Blog_signup
![blog_signup](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/%ED%9A%8C%EC%9B%90%20%EA%B0%80%EC%9E%85.PNG)

## 마지막 느낌점
   * 목표 요구한 결과물 -> 기능 테스트 -> 기획안 작성, 수정 -> 기능확인 -> 기획안 수정... -> CSS는 요구사항의Repo를 대부분사용했고 일부 커스텀 해서작성했습니다. -> 발표내용 준비.
   * 기획안 수정& 점검에 시간 많이 소비했고, 트러블 슈팅를 끊임없이 했습니다, Commits 나중에 깜빡해서 덩어리체로 올라가고...(commits 스트레스 - 나중에 자동완성)
   * 초반에 tailwind사용해서 UI 만들었지만, 잘 활용하지못해 화면이 단순했었고, 다시 Repo양식을 가져와 일일이 적용했습니다.  CSS 틀있어도 이걸html 적용하느라 시행착오 많이 겪었습니다.  
![사용언어](https://github.com/nathanLYJ/NathanLYJ/blob/main/attackment/%EC%82%AC%EC%9A%A9%20%EC%96%B8%EC%96%B4.PNG)
   * SQL데이터 송신 수신을 실전에서 많이 배운웠습니다
   * 평소에 몰랐던 부분을 배움&복습하고&점검 하는 경험, html/css/tailwind 많이 배웠습니다.



