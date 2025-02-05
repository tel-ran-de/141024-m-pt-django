import unidecode

from django.db import models
from django.db.models import Q
from django.utils.text import slugify


class ArticleQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def by_category(self, category_id):
        return self.active().filter(category_id=category_id)

    def by_tag(self, tag_id):
        return self.active().filter(tags__id=tag_id)

    def search(self, query):
        return self.active().filter(Q(title__icontains=query) | Q(content__icontains=query))

    def sorted(self, sort='publication_date', order='desc'):
        valid_sort_fields = {'publication_date', 'views'}
        if sort not in valid_sort_fields:
            sort = 'publication_date'
        order_by = f'-{sort}' if order == 'desc' else sort
        return self.active().order_by(order_by)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def by_category(self, category_id):
        return self.get_queryset().by_category(category_id)

    def by_tag(self, tag_id):
        return self.get_queryset().by_tag(tag_id)

    def search(self, query):
        return self.get_queryset().search(query)

    def sorted(self, sort='publication_date', order='desc'):
        return self.get_queryset().sorted(sort, order)


class AllArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Категория')

    class Meta:
        db_table = 'Categories'  # без указания этого параметра, таблица в БД будет называться вида 'news_categorys'
        verbose_name = 'Категория'  # единственное число для отображения в админке
        verbose_name_plural = 'Категории'  # множественное число для отображения в админке

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True,  verbose_name='Тег')

    class Meta:
        db_table = 'Tags'  # без указания этого параметра, таблица в БД будет называться вида 'news_tags'
        verbose_name = 'Тег'  # единственное число для отображения в админке
        verbose_name_plural = 'Теги'  # множественное число для отображения в админке

    def __str__(self):
        return self.name


class Article(models.Model):
    class Status(models.IntegerChoices):
        UNCHECKED = 0, 'не проверено'
        CHECKED = 1, 'проверено'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1, verbose_name='Категория')
    tags = models.ManyToManyField('Tag', related_name='article', verbose_name='Теги')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Слаг')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    status = models.BooleanField(default=0,
                                 choices=(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                 verbose_name='Проверено')
    image = models.ImageField(
        upload_to='articles/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )

    class Meta:
        db_table = 'Articles'  # без указания этого параметра, таблица в БД будет называться вида 'news_articles'
        verbose_name = 'Статья'  # единственное число для отображения в админке
        verbose_name_plural = 'Статьи'  # множественное число для отображения в админке

    objects = ArticleManager()
    all_objects = AllArticleManager()

    def save(self, *args, **kwargs):
        # Сохраняем статью, чтобы получить id
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(unidecode.unidecode(self.title))
            unique_slug = base_slug
            num = 1
            while Article.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug

        # Сохраняем статью снова, чтобы обновить слаг
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f'Like by {self.ip_address} on {self.article}'


class Favorite(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='favorites')
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f'Favorite by {self.ip_address} on {self.article}'
