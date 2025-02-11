from django.contrib.auth import get_user_model
from django.core.cache import cache
from news.models import Article, Category


def global_context(request):
    return {
        "users_count": get_user_model().objects.count(),
        "news_count": Article.objects.count(),
        "categories": cache.get_or_set("categories", list(Category.objects.all()), 60 * 15),
        "menu": [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "news:catalog"},
            {"title": "Добавить статью", "url": "/news/add/", "url_name": "news:add_article"},
            {"title": "Избранное", "url": "/news/favorites/", "url_name": "news:favorites"},
        ],
    }
