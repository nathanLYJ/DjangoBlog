from django.contrib import admin
from .models import UserProfile, Category, Tag, Post, Comment

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
