from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)  # 사용자가 입력한 URL (YouTube 등)
    text_input = models.TextField(blank=True, null=True)  # 사용자가 입력한 텍스트
    file_name = models.CharField(
        max_length=100, blank=True, null=True
    )  # 업로드한 파일명
    summary_result = models.TextField(blank=True, null=True)  # 영어 요약 결과
    translation_result = models.TextField(blank=True, null=True)  # 한글 번역 결과
    created_at = models.DateTimeField(auto_now_add=True)  # 레코드 생성 시간

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
