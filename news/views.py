from django.http import HttpResponse
from django.shortcuts import render


info = {
    "users_count": 100600,
    "news_count": 100600,
    "menu": [
        {"title": "Главная",
         "url": "/",
         "url_name": "index"},
        {"title": "О проекте",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог",
         "url": "/news/catalog/",
         "url_name": "catalog"},
    ]
}


def main(request):
    """
    Представление рендерит шаблон base.html
    """
    return render(request, 'base.html')


def about(request):
    return HttpResponse('info')


def catalog(request):
    return HttpResponse('Каталог новостей')


def get_categories(request):
    """
    Возвращает все категории для представления в каталоге
    """
    return HttpResponse('All categories')


def get_news_by_category(request, slug):
    """
    Возвращает новости по категории для представления в каталоге
    """
    return HttpResponse(f'News by category {slug}')


def get_news_by_tag(request, slug):
    """
    Возвращает новости по тегу для представления в каталоге
    """
    return HttpResponse(f'News by tag {slug}')


def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")


def get_all_news(request):
    """
    Принимает информацию о проекте (словарь info)
    """
    return render(request, 'news/catalog.html', context=info)


def get_detail_news_by_id(request, news_id):
    """
    Возвращает детальную информацию по новости для представления
    """
    return HttpResponse(f'Detail news by id {news_id}')
