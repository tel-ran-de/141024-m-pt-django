from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView

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


def sign_up(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse('users:register_done'))
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


class RegisterDoneView(LoginRequiredMixin, BaseMixin, TemplateView):
    template_name = 'users/register_done.html'
    extra_context = {'title': 'Регистрация завершена'}
