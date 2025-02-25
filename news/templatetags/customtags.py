import os, random

from django.contrib.admin import register
from django import template

from ..models import Favorite, Like


register = template.Library()


@register.filter(name='has_liked')
def has_liked(article, ip_address):
    return Like.objects.filter(article=article, ip_address=ip_address).exists()


@register.filter(name='has_favorited')
def has_favorited(article, ip_address):
    return Favorite.objects.filter(article=article, ip_address=ip_address).exists()


@register.filter(name='random_color')
def random_color(tag):
    # Генерируем уникальный цвет для каждого тега на основе его ID
    random.seed(tag.id)
    return f'#{random.randint(0, 0xFFFFFF):06x}'


@register.filter
def basename(value):
    return os.path.basename(value)


@register.filter
def add(value, arg):
    return int(value) + int(arg)


@register.filter(name='can_edit')
def can_edit(article, user):
    """
    Возвращает True, если пользователь может редактировать (или удалять) статью.
    Условие:
      - пользователь аутентифицирован, и
      - либо он является суперпользователем,
      - либо состоит в группе "Moderator",
      - либо является автором статьи.
    """
    if not user.is_authenticated:
        return False
    if user.is_superuser or user.groups.filter(name="Moderator").exists():
        return True
    return article.author == user


@register.simple_tag
def paginate_pages(page_obj, adjacent_pages=2):
    """
    Формирует список страниц для вывода в пагинаторе по следующей логике:
      - Всегда показываем первые 3 страницы (если они существуют)
      - Показываем страницы: (текущая страница - adjacent_pages) ... (текущая страница + adjacent_pages)
      - Всегда показываем последние 3 страницы (если они существуют)
    Между непоследовательными номерами вставляем многоточие ("...").
    """
    current = page_obj.number
    last = page_obj.paginator.num_pages
    pages = set()

    # Первые 3 страницы
    for i in range(1, min(4, last + 1)):
        pages.add(i)

    # Страницы вокруг текущей
    for i in range(max(current - adjacent_pages, 1), min(current + adjacent_pages, last) + 1):
        pages.add(i)

    # Последние 3 страницы
    for i in range(max(last - 2, 1), last + 1):
        pages.add(i)

    pages = sorted(pages)

    # Вставляем многоточия там, где разрыв между соседними номерами больше 1
    result = []
    prev = None
    for p in pages:
        if prev and p - prev > 1:
            result.append("...")
        result.append(p)
        prev = p

    return result