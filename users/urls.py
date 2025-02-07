from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('register_done/', views.RegisterDoneView.as_view(), name='register_done')
]
