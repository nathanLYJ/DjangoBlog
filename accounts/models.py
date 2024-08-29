from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    introduction = models.TextField(blank=True)
    image = models.ImageField(upload_to="profile_images", blank=True)
    nickname = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)  # 이 필드를 추가

    def __str__(self):
        return self.nickname or self.user.username
