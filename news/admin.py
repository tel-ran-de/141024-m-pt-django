from django.contrib import admin
from django.utils.html import format_html

from .models import Article, Category, Tag


admin.site.site_header = "Info to Go Admin Portal"
admin.site.site_title = "Info to Go Admin Portal"
admin.site.index_title = "Welcome to ITG Admin Portal"


def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


make_inactive.short_description = 'Сделать неактивными выбранные статьи'
make_active.short_description = 'Сделать активными выбранные статьи'


class TagInline(admin.TabularInline):
    model = Article.tags.through
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    # list_display отображает поля в таблице
    list_display = ('title', 'category', 'publication_date', 'views', 'colored_status')
    # list_filter позволяет фильтровать по полям
    list_filter = ('category', 'is_active')
    # search_fields позволяет искать по полям
    search_fields = ('title', 'content')
    # actions позволяет выполнять действия над выбранными записями
    actions = [make_inactive, make_active]

    # # fields позволяет выбирать поля для редактирования (не работает с fieldsets)
    # fields = ('title', 'category', 'content', 'tags', 'is_active')

    # fieldsets позволяет выбирать группы полей (не работает с fields)
    fieldsets = (
        ('Главная информация', {'fields': ('title', 'content')}),
        ('Дополнительные параметры', {'fields': ('category', 'tags', 'is_active')}),
    )
    # inlines позволяет добавлять дополнительные поля
    inlines = [TagInline]


    def get_queryset(self, request):
        return Article.all_objects.get_queryset()

    def colored_status(self, obj):
        return format_html('<span style="color: {};">{}</span>', 'green' if obj.is_active else 'red', obj.is_active)

    colored_status.short_description = 'Статус'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
