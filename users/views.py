from allauth.account.views import ConfirmEmailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import CustomAuthenticationForm
from news.views import BaseMixin


class LogoutUser(BaseMixin, LogoutView):
    next_page = reverse_lazy('account_login')


class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        response = super().get(*args, **kwargs)
        if self.object.emailaddress_set.filter(verified=True).exists():
            return redirect('account_login')
        return response
