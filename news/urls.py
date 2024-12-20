from django.urls import path
from . import views


# будет иметь префикс в urlах /news/
urlpatterns = [
    path('', views.get_all_news),
    path('<int:news_id>/', views.get_news_by_id),
]
