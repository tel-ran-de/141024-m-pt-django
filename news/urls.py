from django.urls import path
from . import views


# будет иметь префикс в urlах /news/
urlpatterns = [
    path('', views.get_all_news),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:news_id>/', views.get_detail_news_by_id),
    path('catalog/<slug:slug>/', views.get_category_by_name),
]
