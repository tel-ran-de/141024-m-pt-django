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
