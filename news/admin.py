from django.contrib import admin

from .models import Article, Category, Tag


admin.site.site_header = "Info to Go Admin Portal"
admin.site.site_title = "Info to Go Admin Portal"
admin.site.index_title = "Welcome to ITG Admin Portal"


class ArticleAdmin(admin.ModelAdmin):
    # list_display отображает поля в таблице
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active')
    # list_filter позволяет фильтровать по полям
    list_filter = ('category', 'is_active')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
