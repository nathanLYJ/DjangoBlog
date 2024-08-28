from django.contrib import admin
from .models import UserProfile, Category, Tag, Post, Comment


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "nickname", "introduction")
    search_fields = ("user__username", "nickname")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "updated_at", "category")
    list_filter = ("category", "tags")
    search_fields = ("title", "content")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
