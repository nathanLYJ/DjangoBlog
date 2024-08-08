from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Categories'

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	modified_date = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, related_name='posts')

	class Meta:
		ordering = ['-created_date']

	def __str__(self):
		return self.title