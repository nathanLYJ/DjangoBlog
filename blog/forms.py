from django import forms
from .models import Post, Comment, Tag, Category, UserProfile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            "title",
            "content",
            "thumb_image",
            "file_upload",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "name",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "nickname",
            "introduction",
            "image",
        ]
