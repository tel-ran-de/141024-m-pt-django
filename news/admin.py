from django.contrib import admin
from django.utils.html import format_html

from .models import Article, Category, Tag


admin.site.site_header = "Info to Go Admin Portal"
admin.site.site_title = "Info to Go Admin Portal"
admin.site.index_title = "Welcome to ITG Admin Portal"


class ArticleAdmin(admin.ModelAdmin):
    # list_display отображает поля в таблице
    list_display = ('title', 'category', 'publication_date', 'views', 'colored_status')
    # list_filter позволяет фильтровать по полям
    list_filter = ('category', 'is_active')
    # search_fields позволяет искать по полям
    search_fields = ('title', 'content')

    def get_queryset(self, request):
        return Article.all_objects.get_queryset()

    def colored_status(self, obj):
        return format_html('<span style="color: {};">{}</span>', 'green' if obj.is_active else 'red', obj.is_active)

    colored_status.short_description = 'Статус'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
