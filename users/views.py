from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from .forms import LoginUserPassword


def login_user(request):
    if request.method == 'POST':
        form = LoginUserPassword(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news:catalog')
    else:
        form = LoginUserPassword()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    # перенаправляем пользователя на главную страницу, используя reverse для получения URL-адреса
    return redirect(reverse('users:login'))
