import random

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
