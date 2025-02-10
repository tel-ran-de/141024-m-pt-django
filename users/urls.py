from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register_done/', views.RegisterDoneView.as_view(), name='register_done')
]
