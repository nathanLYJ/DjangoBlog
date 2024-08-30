from django import forms


class ChatForm(forms.Form):
    text_input = forms.CharField(
        label="글 내용에 대해서 요약",
        max_length=100,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "요약할 글 내용을 입력하세요",
                "rows": 4,  # 입력창의 높이를 조절
            }
        ),
        required=False,
    )
    file_input = forms.FileField(
        label="PDF 파일 업로드",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
        required=False,
    )
    youtube_url = forms.URLField(
        label="Youtube URL 요약",
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
                "placeholder": "요약할 Youtube URL을 입력하세요",
            }
        ),
        required=False,
    )
