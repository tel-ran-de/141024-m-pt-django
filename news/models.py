import unidecode

from django.db import models
from django.utils.text import slugify


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def sorted_by_title(self):
        return self.get_queryset().all().order_by('-title')


class AllArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField('Tag', related_name='article')
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = ArticleManager()
    all_objects = AllArticleManager()

    def save(self, *args, **kwargs):
        # Сохраняем статью, чтобы получить id
        super().save(*args, **kwargs)

        if not self.slug:
            print(f"Title before slugify: {self.title}")  # Отладочное сообщение
            base_slug = slugify(unidecode.unidecode(self.title))
            self.slug = f"{base_slug}-{self.id}"
            print(f"Generated slug: {self.slug}")  # Отладочное сообщение

        # Сохраняем статью снова, чтобы обновить слаг
        super().save(*args, **kwargs)
        print(f"Saved article with slug: {self.slug}")  # Отладочное сообщение

    def __str__(self):
        return self.title
