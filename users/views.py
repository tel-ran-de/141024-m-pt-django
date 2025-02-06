from django.http import HttpResponse


def login_user(request):
    return HttpResponse('Вы вошли в систему!')


def logout_user(request):
    return HttpResponse('Вы вышли из системы!')
