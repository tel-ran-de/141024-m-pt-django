import json

from django.core.paginator import Paginator
from django.db import models
from django.db.models import F, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify
from django.views import View
import unidecode

from .forms import ArticleForm, ArticleUploadForm
from .models import Article, Favorite, Category, Like, Tag


info = {
    "users_count": 5,
    "news_count": 10,
    "categories": Category.objects.all(),
    "menu": [
        {"title": "Главная",
         "url": "/",
         "url_name": "index"},
        {"title": "О проекте",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог",
         "url": "/news/catalog/",
         "url_name": "news:catalog"},
        {"title": "Добавить статью",
         "url": "/news/add/",
         "url_name": "news:add_article"},
        {"title": "Избранное",
         "url": "/news/favorites/",
         "url_name": "news:favorites"},
    ],
}


def upload_json_view(request):
    if request.method == 'POST':
        form = ArticleUploadForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = form.cleaned_data['json_file']
            try:
                data = json.load(json_file)
                errors = form.validate_json_data(data)
                if errors:
                    return render(request, 'news/upload_json.html', {'form': form, 'errors': errors})

                # Сохраняем данные в сессию для последовательного просмотра
                request.session['articles_data'] = data
                request.session['current_index'] = 0
                return redirect('news:edit_article_from_json', index=0)
            except json.JSONDecodeError:
                return render(request, 'news/upload_json.html', {'form': form, 'error': 'Неверный формат JSON-файла'})
    else:
        form = ArticleUploadForm()
    return render(request, 'news/upload_json.html', {'form': form})


def edit_article_from_json(request, index):
    articles_data = request.session.get('articles_data', [])
    if index >= len(articles_data):
        return redirect('news:catalog')
    article_data = articles_data[index]
    form = ArticleForm(initial={
        'title': article_data['fields']['title'],
        'content': article_data['fields']['content'],
        'category': Category.objects.get(name=article_data['fields']['category']),
        'tags': [Tag.objects.get(name=tag) for tag in article_data['fields']['tags']]
    })
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            if 'next' in request.POST:
                # Сохраняем текущую статью
                save_article(article_data, form)
                # Переходим к следующей статье
                request.session['current_index'] = index + 1
                return redirect('news:edit_article_from_json', index=index + 1)
            elif 'save_all' in request.POST:
                # Сохраняем текущую статью
                save_article(article_data, form)
                # Сохраняем все оставшиеся статьи
                for i in range(index + 1, len(articles_data)):
                    save_article(articles_data[i])
                del request.session['articles_data']
                del request.session['current_index']
                return redirect('news:catalog')
    context = {'form': form, 'index': index, 'total': len(articles_data), 'is_last': index == len(articles_data) - 1}
    return render(request, 'news/edit_article_from_json.html', context)


def save_article(article_data, form=None):
    fields = article_data['fields']
    title = fields['title']
    content = fields['content']
    category_name = fields['category']
    tags_names = fields['tags']
    category = Category.objects.get(name=category_name)
    # Генерируем slug до создания статьи
    base_slug = slugify(unidecode.unidecode(title))
    unique_slug = base_slug
    num = 1
    while Article.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{base_slug}-{num}"
        num += 1
    if form:
        article = form.save(commit=False)
        article.slug = unique_slug
        article.save()
        # Обновляем теги
        article.tags.set(form.cleaned_data['tags'])
    else:
        article = Article(
            title=title,
            content=content,
            category=category,
            slug=unique_slug
        )
        article.save()
        # Добавляем теги к статье
        for tag_name in tags_names:
            tag = Tag.objects.get(name=tag_name)
            article.tags.add(tag)
    return article


def favorites(request):
    ip_address = request.META.get('REMOTE_ADDR')
    favorite_articles = Article.objects.filter(favorites__ip_address=ip_address)
    context = {**info, 'news': favorite_articles, 'news_count': len(favorite_articles), 'page_obj': favorite_articles, 'user_ip': request.META.get('REMOTE_ADDR'), }
    return render(request, 'news/catalog.html', context=context)


def toggle_favorite(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    ip_address = request.META.get('REMOTE_ADDR')
    favorite, created = Favorite.objects.get_or_create(article=article, ip_address=ip_address)
    if not created:
        favorite.delete()
    return redirect('news:detail_article_by_id', article_id=article_id)


def toggle_like(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    ip_address = request.META.get('REMOTE_ADDR')
    like, created = Like.objects.get_or_create(article=article, ip_address=ip_address)
    if not created:
        like.delete()
    return redirect('news:detail_article_by_id', article_id=article_id)


def search_news(request):
    query = request.GET.get('q')
    categories = Category.objects.all()
    if query:
        articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        articles = Article.objects.all()

    paginator = Paginator(articles, 10)  # Показывать 10 новостей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {**info, 'news': articles, 'news_count': len(articles), 'page_obj': page_obj, 'user_ip': request.META.get('REMOTE_ADDR'),}

    return render(request, 'news/catalog.html', context=context)


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


def get_news_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles = Article.objects.filter(category=category)

    paginator = Paginator(articles, 10)  # Показывать 10 новостей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {**info, 'news': articles, 'news_count': len(articles), 'page_obj': page_obj, 'user_ip': request.META.get('REMOTE_ADDR'),}

    return render(request, 'news/catalog.html', context=context)


def get_news_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    articles = Article.objects.filter(tags=tag)

    paginator = Paginator(articles, 10)  # Показывать 10 новостей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {**info, 'news': articles, 'news_count': len(articles), 'page_obj': page_obj,}

    return render(request, 'news/catalog.html', context=context)


def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")


class GetAllNewsView(View):
    def get(self, request, *args, **kwargs):
        sort = request.GET.get('sort', 'publication_date')  # по умолчанию сортируем по дате загрузки
        order = request.GET.get('order', 'desc')  # по умолчанию сортируем по убыванию
        valid_sort_fields = {'publication_date', 'views'}

        if sort not in valid_sort_fields:
            sort = 'publication_date'
        order_by = f'-{sort}' if order == 'desc' else sort

        articles = Article.objects.select_related('category').prefetch_related('tags').order_by(order_by)

        paginator = Paginator(articles, 10)  # Показывать 10 новостей на странице
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {**info, 'news': articles, 'news_count': len(articles), 'page_obj': page_obj, 'user_ip': request.META.get('REMOTE_ADDR'),}

        return render(request, 'news/catalog.html', context=context)


def get_detail_article_by_id(request, article_id):
    """
    Возвращает детальную информацию по новости для представления
    """
    article = get_object_or_404(Article, pk=article_id)

    # Увеличиваем счетчик просмотров только один раз за сессию для каждой новости
    viewed_articles = request.session.get('viewed_articles', [])
    if article_id not in viewed_articles:
        article.views += 1
        article.save()
        viewed_articles.append(article_id)
        request.session['viewed_articles'] = viewed_articles

    context = {**info, 'article': article}

    return render(request, 'news/article_detail.html', context=context)


def get_detail_article_by_title(request, title):

    article = get_object_or_404(Article, slug=title)

    context = {**info, 'article': article, 'user_ip': request.META.get('REMOTE_ADDR'),}

    return render(request, 'news/article_detail.html', context=context)


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article_data = {
                'fields': {
                    'title': form.cleaned_data['title'],
                    'content': form.cleaned_data['content'],
                    'category': form.cleaned_data['category'].name,
                    'tags': [tag.name for tag in form.cleaned_data['tags']]
                }
            }
            article = save_article(article_data, form)
            return redirect('news:detail_article_by_id', article_id=article.id)
    else:
        form = ArticleForm()
    context = {'form': form, 'menu': info['menu']}
    return render(request, 'news/add_article.html', context=context)


def article_update(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('news:detail_article_by_id', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'menu': info['menu'], 'article': article}
    return render(request, 'news/edit_article.html', context=context)


def article_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == "POST":
        article.delete()
        return redirect('news:catalog')

    context = {'menu': info['menu'], 'article': article}
    return render(request, 'news/delete_article.html', context=context)
