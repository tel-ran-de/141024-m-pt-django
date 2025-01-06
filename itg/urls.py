from django.contrib import admin
from django.urls import path, include

from news import views


# Подключаем файл urls.py из приложения news через include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='index'),
    path('about/', views.about, name='about'),
    path('news/', include('news.urls')),
]
