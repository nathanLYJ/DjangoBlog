from django import forms
from .models import Post, Comment, Tag, Category, UserProfile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "thumb_image",
            "category",
            "tags",
            "file_upload",
        ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["tags"].widget = forms.CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()


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

    def clean_name(self):
        name = self.cleaned_data["name"]
        return name.lower()  # 태그 이름을 소문자로 저장


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "description",  # description 필드 추가
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "nickname",
            "introduction",
            "image",
            "address",  # address 필드 추가
            "birth_date",  # birth_date 필드 추가
        ]
