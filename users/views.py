# users/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from news.models import Article


class ProfileInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_tab'] = 'info'
        return context


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