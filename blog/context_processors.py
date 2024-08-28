from django.core.cache import cache
from .models import Category


def categories(request):
    categories = cache.get("all_categories")
    if not categories:
        categories = list(Category.objects.all())
        cache.set("all_categories", categories, 3600)  # 1시간 동안 캐시
    return {"categories": categories}
