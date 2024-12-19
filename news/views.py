from django.http import HttpResponse


def main(request):
    return HttpResponse('Hello, world!')  # Вернёт страницу с надписью "Hello world!"


def info(request):
    return HttpResponse('info')
