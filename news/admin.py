from django.contrib import admin

from .models import Article, Category, Tag


admin.site.site_header = "Info to Go Admin Portal"
admin.site.site_title = "Info to Go Admin Portal"
admin.site.index_title = "Welcome to ITG Admin Portal"


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
