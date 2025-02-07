from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import CustomAuthenticationForm, RegisterUserForm
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


class RegisterUser(BaseMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:register_done')

    def form_valid(self, form):
        # Сохраняем пользователя, но не коммитим в базу данных
        user = form.save(commit=False)
        # Хешируем пароль
        user.set_password(form.cleaned_data['password'])
        # Сохраняем пользователя в базе данных
        user.save()
        return super().form_valid(form)


class RegisterDoneView(LoginRequiredMixin, BaseMixin, TemplateView):
    template_name = 'users/register_done.html'
    extra_context = {'title': 'Регистрация завершена'}
