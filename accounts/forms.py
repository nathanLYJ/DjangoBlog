from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="유효한 이메일 주소를 입력해주세요.",
        label="이메일 주소",
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text="전화번호를 입력하세요 (선택 사항).",
        label="전화번호",
    )
    nickname = forms.CharField(
        max_length=50, required=True, help_text="닉네임을 입력해주세요.", label="닉네임"
    )
    birth_date = forms.DateField(
        required=False, help_text="생년월일을 입력하세요 (선택 사항).", label="생년월일"
    )
    address = forms.CharField(
        max_length=255,
        required=False,
        help_text="주소를 입력하세요 (선택 사항).",
        label="주소",
    )
    introduction = forms.CharField(
        widget=forms.Textarea,
        required=False,
        help_text="자기소개를 입력하세요 (선택 사항).",
        label="자기소개",
    )
    image = forms.ImageField(
        required=False,
        help_text="프로필 사진을 업로드하세요 (선택 사항).",
        label="프로필 사진",
    )
    terms_agreement = forms.BooleanField(
        required=True,
        help_text="서비스 이용약관에 동의해주세요.",
        label="이용약관 동의",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "nickname",
            "phone_number",
            "birth_date",
            "address",
            "introduction",
            "image",
            "terms_agreement",
        )

        labels = {
            "username": "ID",
            "email": "이메일",
            "password1": "비밀번호",
            "password2": "비밀번호 확인",
            "nickname": "닉네임",
            "phone_number": "전화번호",
            "birth_date": "생년월일",
            "address": "주소",
            "introduction": "자기소개",
            "image": "프로필 사진",
            "terms_agreement": "이용약관 동의",
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                nickname=self.cleaned_data["nickname"],
                birth_date=self.cleaned_data["birth_date"],
                address=self.cleaned_data["address"],
                introduction=self.cleaned_data["introduction"],
                image=self.cleaned_data["image"],
            )
        return user
