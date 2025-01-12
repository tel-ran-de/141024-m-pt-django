from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article


"""
Информация в шаблоны будет браться из базы данных
Но пока, мы сделаем переменные, куда будем записывать информацию, которая пойдет в 
контекст шаблона
"""
# Пример данных для новостей
news_dataset = [
    {
        "title": "Коты захватили правительство!",
        "content": "Вчера ночью коты совершили государственный переворот и захватили все ключевые посты в правительстве. Президент кот Мурзик обещает бесплатный вискас для всех граждан.",
        "category": "Общество",
        "tags": ["коты", "переворот", "вискас"],
        "id_author": 1,
        "id_article": 1,
        "upload_date": "2023-01-15",
        "views_count": 1000,
        "favorites_count": 500
    },
    {
        "title": "Найден новый вид единорогов!",
        "content": "Ученые обнаружили новый вид единорогов в лесах Амазонии. Эти единороги могут летать и излучают радужный свет.",
        "category": "Наука",
        "tags": ["единороги", "ученые", "наука", "открытие"],
        "id_author": 2,
        "id_article": 2,
        "upload_date": "2023-01-20",
        "views_count": 1500,
        "favorites_count": 700
    },
    {
        "title": "Земля стала квадратной!",
        "content": "Сегодня утром жители Земли проснулись и обнаружили, что наша планета стала квадратной. Ученые в шоке, но обещают разобраться в причинах.",
        "category": "Наука",
        "tags": ["земля", "квадрат", "ученые", "наука", "открытие"],
        "id_author": 1,
        "id_article": 3,
        "upload_date": "2023-02-05",
        "views_count": 2000,
        "favorites_count": 1000
    },
    {
        "title": "Собаки научились говорить!",
        "content": "Вчера собаки по всему миру начали говорить на человеческом языке. Первые слова были: 'Где моя косточка?'",
        "category": "Общество",
        "tags": ["собаки", "язык", "косточка"],
        "id_author": 2,
        "id_article": 4,
        "upload_date": "2023-02-10",
        "views_count": 1800,
        "favorites_count": 900
    },
    {
        "title": "Луна исчезла на час!",
        "content": "Вчера вечером Луна исчезла с неба на целый час. Астрономы в панике, но обещают найти объяснение.",
        "category": "Наука",
        "tags": ["луна", "исчезновение", "ученые", "наука", "открытие"],
        "id_author": 3,
        "id_article": 5,
        "upload_date": "2023-03-01",
        "views_count": 2200,
        "favorites_count": 1100
    },
    {
        "title": "Роботы захватили кухни ресторанов!",
        "content": "Роботы-повара захватили кухни всех ресторанов мира. Теперь все блюда готовятся с идеальной точностью и вкусом.",
        "category": "Технологии",
        "tags": ["роботы", "кухня", "рестораны", "переворот"],
        "id_author": 1,
        "id_article": 6,
        "upload_date": "2023-03-15",
        "views_count": 2500,
        "favorites_count": 1200
    },
    {
        "title": "Деревья начали ходить!",
        "content": "Сегодня утром деревья в парках начали ходить. Ученые предполагают, что это связано с глобальным потеплением.",
        "category": "Природа",
        "tags": ["парки", "глобальное потепление", "ученые", "наука"],
        "id_author": 2,
        "id_article": 7,
        "upload_date": "2023-04-01",
        "views_count": 2800,
        "favorites_count": 1400
    },
    {
        "title": "Вода стала розовой!",
        "content": "Вчера вода во всех реках и озерах стала розовой. Ученые обещают найти причину этого явления.",
        "category": "Природа",
        "tags": ["вода", "ученые", "наука"],
        "id_author": 3,
        "id_article": 8,
        "upload_date": "2023-04-15",
        "views_count": 3000,
        "favorites_count": 1500
    },
    {
        "title": "Люди начали летать!",
        "content": "Сегодня утром люди по всему миру начали летать. Ученые в шоке, но обещают найти объяснение этому феномену.",
        "category": "Наука",
        "tags": ["ученые", "наука", "открытие"],
        "id_author": 1,
        "id_article": 9,
        "upload_date": "2023-05-01",
        "views_count": 3200,
        "favorites_count": 1600
    },
    {
        "title": "Зомби атакуют супермаркеты!",
        "content": "Вчера ночью зомби атаковали все супермаркеты мира. Они искали свежие мозги и консервы.",
        "category": "Общество",
        "tags": ["зомби", "супермаркеты", "атака", "переворот"],
        "id_author": 2,
        "id_article": 10,
        "upload_date": "2023-05-15",
        "views_count": 3500,
        "favorites_count": 1700
    }
]
info = {
    "users_count": 5,
    "news_count": 10,
    # "menu": ['Главная', 'О проекте', 'Каталог']
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
    ],
    "news": news_dataset  # Добавим в контекст шаблона информацию о новостях, чтобы все было в одном месте
}


def main(request):
    """
    Представление рендерит шаблон mian.html
    """
    return render(request, 'main.html', context=info)


def about(request):
    """Представление рендерит шаблон about.html"""
    return render(request, 'about.html', context=info)


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

    articles = Article.objects.select_related('category').prefetch_related('tags')

    context = {
        'news': articles,
        'news_count': len(articles),
        'menu': [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "catalog"},
        ],
    }

    return render(request, 'news/catalog.html', context=context)


def get_detail_article_by_id(request, article_id):
    """
    Возвращает детальную информацию по новости для представления
    """
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
        'menu': [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "catalog"},
        ],
    }
    return render(request, 'news/article_detail.html', context=context)


def get_detail_article_by_title(request, title):

    article = get_object_or_404(Article, slug=title)
    context = {
        'article': article,
        'menu': [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "catalog"},
        ],
    }
    return render(request, 'news/article_detail.html', context=context)
