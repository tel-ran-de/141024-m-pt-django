from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('catalog/', views.GetAllNewsView.as_view(), name='catalog'),
    path('catalog/<int:pk>/', views.ArticleDetailView.as_view(), name='detail_article_by_id'),
    path('catalog/<slug:title>/', views.get_detail_article_by_title, name='detail_article_by_title'),
    path('tag/<int:tag_id>/', views.get_news_by_tag, name='get_news_by_tag'),
    path('category/<int:category_id>/', views.get_news_by_category, name='get_news_by_category'),
    path('search/', views.search_news, name='search_news'),
    path('like/<int:article_id>/', views.toggle_like, name='toggle_like'),
    path('favorite/<int:article_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorites, name='favorites'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:article_id>/', views.article_update, name='article_update'),
    path('delete/<int:article_id>/', views.article_delete, name='article_delete'),
    path('upload_json/', views.upload_json_view, name='upload_json'),
    path('edit_article_from_json/<int:index>/', views.EditArticleFromJsonView.as_view(), name='edit_article_from_json'),
]
