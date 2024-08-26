from django.contrib.auth.models import User
from django.db import models


# 프로필 모델
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    introduction = models.TextField(blank=True)
    image = models.ImageField(upload_to="profile_images", blank=True)
    real_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nickname or self.user.username


# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# 태그 모델
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# 포스트 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    thumb_image = models.ImageField(
        upload_to="blog/images/%Y/%m/%d/", blank=True, null=True
    )
    file_upload = models.FileField(
        upload_to="blog/files/%Y/%m/%d/", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(
        "Tag", related_name="posts", blank=True
    )  # Tag 모델을 문자열로 참조
    likes = models.PositiveIntegerField(default=0)  # 여기서 수정되었습니다
    dislikes = models.PositiveIntegerField(default=0)  # 여기서 수정되었습니다

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"


# 댓글 모델
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True
    )

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
