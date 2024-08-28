from django import forms
from .models import Post, Comment, Tag, Category, UserProfile


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                }
            )


class PostForm(BaseForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="카테고리를 선택하세요"
    )
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "thumb_image",
            "category",
            "tags",
            "file_upload",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tags"].widget = forms.CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()


class CommentForm(BaseForm):
    class Meta:
        model = Comment
        fields = ["content"]


class TagForm(BaseForm):
    class Meta:
        model = Tag
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"placeholder": "태그 이름 (예: 파이썬)"}
        )

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name.startswith("#"):
            name = name[1:]
        return name.lower()


class CategoryForm(BaseForm):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class UserProfileForm(BaseForm):
    class Meta:
        model = UserProfile
        fields = ["nickname", "introduction", "image", "address", "birth_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["birth_date"].widget = forms.DateInput(attrs={"type": "date"})
