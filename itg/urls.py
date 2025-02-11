from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from itg import settings
from news import views
from users.views import CustomConfirmEmailView, CustomPasswordResetDoneView, CustomPasswordResetFromKeyView, CustomPasswordResetFromKeyDoneView, CustomPasswordResetView, CustomLoginView, CustomSignupView


# Подключаем файл urls.py из приложения news через include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('news/', include('news.urls', namespace='news')),

    # Переопределенные URL allauth
    path('accounts/confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('accounts/password/reset/key/<uidb36>/<str:key>/', CustomPasswordResetView.as_view(), name='account_reset_password_from_key'),
    path('accounts/password/reset/key/done/', CustomPasswordResetFromKeyDoneView.as_view(), name='account_reset_password_from_key_done'),
    path('accounts/password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/password/reset/done/', CustomPasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),

    # Общие URL allauth
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path(
        'accounts/password/reset/key/q-set-password/',
        CustomPasswordResetFromKeyView.as_view(),
        kwargs={'uidb36': 'q', 'key': 'set-password'},
        name='special_password_reset'
    ),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
