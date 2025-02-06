from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy

from .forms import LoginUserPassword


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    redirect_field_name = 'next'

    def get_success_url(self):
        if self.request.GET.get('next', '').strip():
            return self.request.POST.get('next')
        return reverse_lazy('news:catalog')


def logout_user(request):
    logout(request)
    # перенаправляем пользователя на главную страницу, используя reverse для получения URL-адреса
    return redirect(reverse('users:login'))


def sign_up(request):
    return HttpResponse('Регистрация')
