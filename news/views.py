from django.http import HttpResponse
from django.shortcuts import render


info = {
    "users_count": 100600,
    "news_count": 1000,
    "menu": ["Главная", "О проекте", "Каталог"],
}


def main(request):
    return HttpResponse('Hello, world!')  # Вернёт страницу с надписью "Hello world!"


def about(request):
    return HttpResponse('info')


def get_all_news(request):
    """
    Принимает информацию о проекте (словарь info)
    """
    return render(request, 'news/catalog.html', context=info)


def get_news_by_id(request, news_id):
    if news_id > 10:
        return HttpResponse('Такой новости нет', status=404)
    return HttpResponse(f'Вы открыли новость {news_id}')  # Вернёт страницу с надписью "Вы открыли новость {news_id}"
