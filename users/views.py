# users/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from news.models import Article

from .forms import UserUpdateForm, ProfileUpdateForm


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаём формы в контекст
        context['user_form'] = kwargs.get('user_form', UserUpdateForm(instance=self.request.user))
        context['profile_form'] = kwargs.get('profile_form', ProfileUpdateForm(instance=self.request.user.profile))
        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:profile')  # Укажите нужное имя URL для профиля
        # Если формы не валидны, передаём их обратно в контекст
        return self.render_to_response(self.get_context_data(user_form=user_form, profile_form=profile_form))


class ProfileArticlesView(LoginRequiredMixin, ListView):
    template_name = 'users/profile_articles.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_tab'] = 'articles'
        return context


class ProfileActivityView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_activity.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь вы можете получить историю действий пользователя, например,
        # из логов или специальной модели истории
        context['active_tab'] = 'activity'
        return context