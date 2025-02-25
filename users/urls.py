# users/urls.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('profile/articles/', views.ProfileArticlesView.as_view(), name='profile_articles'),
    path('profile/activity/', views.ProfileActivityView.as_view(), name='profile_activity'),
]