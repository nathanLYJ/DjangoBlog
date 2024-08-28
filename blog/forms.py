from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from .models import Post, Comment, Tag, Category, UserProfile


class ProfanityFilterMixin:
    PROFANITY_WORDS = [
        # 한국어 비속어
        "씨발",
        "개새끼",
        "병신",
        "지랄",
        "좆",
        "닥쳐",
        "미친",
        "시발",
        "새끼",
        "멍청이",
        "바보",
        # 영어 비속어
        "fuck",
        "shit",
        "asshole",
        "bitch",
        "damn",
        "crap",
        "piss",
        "dick",
        "bastard",
        "slut",
        # 변형된 형태
        "ㅅㅂ",
        "ㅄ",
        "ㅂㅅ",
        "ㅆㅂ",
        "tl qkf",
        "Tlqkf",
        "sibal",
        "ssibal",
        "tlqkf",
        "qq",
        "qq",
    ]

    def clean_text_content(self, field_name):
        content = self.cleaned_data.get(field_name)
        if content:
            for word in self.PROFANITY_WORDS:
                if word in content.lower():
                    raise ValidationError(
                        f"부적절한 표현이 포함되어 있습니다. 다시 확인해 주세요."
                    )
        return content


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                }
            )


class PostForm(BaseForm, ProfanityFilterMixin):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="카테고리를 선택하세요"
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple
    )
    file_upload = forms.FileField(
        required=False,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "doc", "docx", "jpg", "png", "mp4", "webm"]
            )
        ],
        help_text="허용된 파일 형식: pdf, doc, docx, jpg, png, mp4, webm",
    )

    class Meta:
        model = Post
        fields = ["title", "content", "thumb_image", "category", "tags", "file_upload"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["tags"].initial = self.instance.tags.all()

    def clean_file_upload(self):
        file = self.cleaned_data.get("file_upload")
        if file:
            if file.size > 10 * 1024 * 1024:  # 10MB 제한
                raise ValidationError("파일 크기는 10MB를 초과할 수 없습니다.")
        return file

    def clean_content(self):
        return self.clean_text_content("content")

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title and content:
            if len(title) < 5:
                self.add_error("title", "제목은 5글자 이상이어야 합니다.")
            if len(content) < 10:
                self.add_error("content", "내용은 10글자 이상이어야 합니다.")

        return cleaned_data


class CommentForm(BaseForm, ProfanityFilterMixin):
    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = self.clean_text_content("content")
        if len(content) < 2:
            raise ValidationError("댓글은 최소 2글자 이상이어야 합니다.")
        return content


# 나머지 폼 클래스들은 그대로 유지...


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
        name = name.lower()
        if Tag.objects.filter(name=name).exists():
            raise ValidationError("이미 존재하는 태그입니다.")
        return name


class CategoryForm(BaseForm):
    class Meta:
        model = Category
        fields = ["name", "slug"]

    def clean_slug(self):
        slug = self.cleaned_data.get("slug")
        if Category.objects.filter(slug=slug).exists():
            raise ValidationError("이미 사용 중인 슬러그입니다.")
        return slug


class UserProfileForm(BaseForm):
    class Meta:
        model = UserProfile
        fields = ["nickname", "introduction", "image", "address", "birth_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["birth_date"].widget = forms.DateInput(attrs={"type": "date"})

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        if (
            UserProfile.objects.filter(nickname=nickname)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise ValidationError("이미 사용 중인 닉네임입니다.")
        return nickname
