from django.contrib import admin
from accounts.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "nickname", "introduction")
    search_fields = ("user__username", "nickname")
