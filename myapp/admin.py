from django.contrib import admin
from .models import Category, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_date', 'modified_date', 'category']
	list_filter = ['created_date', 'category']
	search_fields = ['title', 'content']
	date_hierarchy = 'created_date'
	ordering = ['-created_date']

admin.site.register(Category)
admin.site.register(Post)
