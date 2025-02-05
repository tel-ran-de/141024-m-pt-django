from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('catalog/', views.GetAllNewsView.as_view(), name='catalog'),
    path('catalog/<int:pk>/', views.ArticleDetailView.as_view(), name='detail_article_by_id'),
    path('catalog/<slug:slug>/', views.ArticleDetailView.as_view(), name='detail_article_by_slag'),
    path('tag/<int:tag_id>/', views.GetNewsByTagView.as_view(), name='get_news_by_tag'),
    path('category/<int:category_id>/', views.GetNewsByCategoryView.as_view(), name='get_news_by_category'),
    path('search/', views.SearchNewsView.as_view(), name='search_news'),
    path('like/<int:article_id>/', views.ToggleLikeView.as_view(), name='toggle_like'),
    path('favorite/<int:article_id>/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
    path('favorites/', views.FavoritesView.as_view(), name='favorites'),
    path('add/', views.AddArticleView.as_view(), name='add_article'),
    path('edit/<int:article_id>/', views.article_update, name='article_update'),
    path('delete/<int:article_id>/', views.article_delete, name='article_delete'),
    path('upload_json/', views.UploadJsonView.as_view(), name='upload_json'),
    path('edit_article_from_json/<int:index>/', views.EditArticleFromJsonView.as_view(), name='edit_article_from_json'),
]
