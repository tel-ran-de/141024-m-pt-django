from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import CustomAuthenticationForm
from news.views import BaseMixin


class LoginUser(BaseMixin, LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    redirect_field_name = 'next'

    def get_success_url(self):
        if self.request.GET.get('next', '').strip():
            return self.request.POST.get('next')
        return reverse_lazy('news:catalog')


class LogoutUser(BaseMixin, LogoutView):
    next_page = reverse_lazy('users:login')


def sign_up(request):
    return HttpResponse('Регистрация')
