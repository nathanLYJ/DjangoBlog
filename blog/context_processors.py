from django.core.cache import cache
from .models import Category


def categories(request):
    categories = cache.get("all_categories")
    if not categories:
        categories = list(Category.objects.all())
        cache.set("all_categories", categories, 3600)  # 1시간 동안 캐시
    return {"categories": categories}

from .models import Post

def get_post_file(post_id):
    # 캐시에서 파일 정보 가져오기
    cache_key = f"post_{post_id}_file_upload"
    file_info = cache.get(cache_key)
    
    if not file_info:
        # 캐시에 파일 정보가 없으면 데이터베이스에서 쿼리
        try:
            post = Post.objects.get(pk=post_id)
            file_info = post.file_upload  # 파일 정보 가져오기
        except Post.DoesNotExist:
            file_info = None
        
        # 캐시에 파일 정보 저장 (1시간 동안 캐시)
        cache.set(cache_key, file_info, 3600)  # 1시간 동안 캐시
    
    return file_info
