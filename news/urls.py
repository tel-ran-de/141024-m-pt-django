from django.urls import path
from . import views


# будет иметь префикс в urlах /news/
urlpatterns = [
    path('catalog/', views.get_all_news, name='catalog'),
    path('catalog/<int:article_id>/', views.get_detail_article_by_id, name='detail_article_by_id'),
    path('catalog/<slug:title>/', views.get_detail_article_by_title, name='detail_article_by_title'),
]
