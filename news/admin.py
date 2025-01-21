from django.contrib import admin
from django.utils.html import format_html

from .models import Article, Category, Tag


admin.site.site_header = "Info to Go Admin Portal"
admin.site.site_title = "Info to Go Admin Portal"
admin.site.index_title = "Welcome to ITG Admin Portal"


class TagInline(admin.TabularInline):
    model = Article.tags.through
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    # list_display отображает поля в таблице
    list_display = ('id', 'title', 'category', 'views', 'is_active', 'status', 'has_spiders')
    # list_display_links позволяет указать в качестве ссылок другие поля
    list_display_links = ('id', 'title')
    # list_filter позволяет фильтровать по полям
    list_filter = ('category', 'is_active')
    # сортировка, возможна по нескольким полям
    ordering = ('-views', 'title')
    # search_fields позволяет искать по полям
    search_fields = ('title', 'content')
    # actions позволяет выполнять действия над выбранными записями
    actions = ['make_inactive', 'make_active', 'set_checked', 'set_unchecked']
    # количество статей на страницу (пагинация)
    list_per_page = 10

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

    @admin.display(description='Пауки внутри')
    def has_spiders(self, article):
        return 'Да' if 'пауки' in article.content else 'Нет'

    @admin.action(description='Сделать неактивными выбранные статьи')
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description='Сделать активными выбранные статьи')
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Отметить статьи как проверенные')
    def set_checked(self, request, queryset):
        updated = queryset.update(status=Article.Status.CHECKED)
        self.message_user(request, f'{updated} статей было отмечено как проверенные')

    @admin.action(description='Отметить статьи как не проверенные')
    def set_unchecked(self, request, queryset):
        updated = queryset.update(status=Article.Status.UNCHECKED)
        self.message_user(request, f'{updated} статей было отмечено как не проверенные', 'warning')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
