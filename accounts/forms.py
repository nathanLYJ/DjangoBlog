from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


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
    full_name = forms.CharField(
        max_length=100, required=True, help_text="이름을 입력해주세요.", label="닉네임"
    )
    birth_date = forms.DateField(
        required=False, help_text="생년월일을 입력하세요 (선택 사항).", label="생년월일"
    )
    gender = forms.ChoiceField(
        choices=[("M", "남성"), ("F", "여성")],
        required=False,
        help_text="성별을 선택하세요.",
        label="성별",
    )
    profile_picture = forms.ImageField(
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
            "full_name",
            "email",
            "phone_number",
            "password1",
            "password2",
            "terms_agreement",
        )

        labels = {
            "username": "ID",
            "full_name": "닉네임",
            "password1": "비밀번호",
            "password2": "비밀번호 확인",
            "email": "이메일",
            "phone_number": "전화번호",
            "terms_agreement": "이용약관 동의",
        }
