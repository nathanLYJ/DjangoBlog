from django.core.cache import cache
from .models import Category, Post


def categories(request):
    categories = cache.get("all_categories")
    if not categories:
        categories = list(Category.objects.all())
        cache.set("all_categories", categories, 3600) 
    return {"categories": categories}


def get_post_file(post_id):
    cache_key = f"post_{post_id}_file_upload"
    file_info = cache.get(cache_key)
    
    if not file_info:
        try:
            post = Post.objects.get(pk=post_id)
            file_info = post.file_upload  
        except Post.DoesNotExist:
            file_info = None    
        cache.set(cache_key, file_info, 3600)  
    
    return file_info
