# Учебный проект "Новости Info to Go"


## Урок 1

### Создали проект `itg`
1. Создали репозиторий
2. Создали проект `itg`
3. Установили зависимости `pip install django`
4. Сохранили зависимости в файл `requirements.txt` командой `pip freeze > requirements.txt`

Развернуть проект на локальной машине через командную строку:
 - Склонировать репозиторий
 - Перейти в папку проекта
 - Создать виртуальное окружение `python -m venv venv`
 - Активировать виртуальное окружение `source venv/bin/activate` на Linux/MacOS или `.\venv\Scripts\activate.bat` на Windows
 - Установить зависимости `pip install -r requirements.txt`

Либо через PyCharm:
 - Склонировать репозиторий через File -> Project from Version Control 
 - Установить зависимости через File -> Settings -> Project Interpreter или через `pip install -r requirements.txt` 

### Создание Django project
Создать проект `django-admin startproject itg .`
Этой командой мы создадим проект с именем `itg` в текущей директории.
Точка в конце команды означает, что проект будет создан в текущей директории, 
без создания дополнительной директории с именем проекта.

**commit: `Урок 1: создаём django проект`**

Запуск проекта `python manage.py runserver`
Для запуска проекта, вам нужно использовать терминал, и находясь в директории проекта, на одном уровне с файлом `manage.py`, выполнить команду `python manage.py runserver`
Для остановки сервера используйте комбинацию клавиш `Ctrl+C`

**Команды терминала:**
- `python manage.py runserver` - запуск сервера
- `cd` - смена директории
- `cd..` - переход на уровень выше
- `ls` - просмотр содержимого директории
- `pwd` - показать текущую директорию

**commit: `Урок 1: запускаем django сервер`**

Создание приложения `python manage.py startapp news`
После создания приложения, вам нужно зарегистрировать его в файле `settings.py` в разделе `INSTALLED_APPS`

**commit: `Урок 1: cоздаём django_app news`**

### Создали первое представление
```python
from django.http import HttpResponse

def main(request):
    return HttpResponse("Hello, world!")  # вернет страничку с надписью "Hello, world!"
```
Чтобы представление заработало, его нужно зарегистрировать в файле `urls.py` конфигурации проекта.

### Создали первый URL
```python
from news import views

path('', views.main),
```

Теперь, если вы перейдете на главную страницу сайта, то увидите надпись "Hello, world!"

**commit: `Урок 1: создаём первый маршрут и первое представление`**


## Урок 2

### Создаем детальное представление новости по ее ID

Для этого нам нужно создать новый маршрут, с конвертом int, который будет принимать ID новости.
```python
path('news/<int:news_id>/', views.news_detail),
```

А так же функцию, которая будет обрабатывать запрос и возвращать страницу с детальной информацией о новости.
```python
def news_by_id(request, news_id):
    return HttpResponse(f"Новость с ID {news_id}")
```

### `include` и собственный файл `urls.py` для приложения `news`
1. Создали еще одно представление `get_all_news` в файле `views.py`
2. Создали файл `urls.py` в директории приложения `news`
3. Зарегистрировали новый файл `urls.py` в файле `urls.py` конфигурации проекта с помощью функции `include`
4. Зарегистрировали маршруты без префикса `news/` в файле `urls.py` приложения `news`

**commit: `Урок 2: собственный urls.py в cards и функция include`**

### Знакомство с Django Templates (Шаблоны)

1. Создали папку `templates` в директории приложения `news`
2. Создали файл `catalog.html` в директории `templates/news`
3. Переписали функцию `get_all_news` в файле `views.py` так, чтобы она возвращала страницу `catalog.html`
используя функцию `render` из модуля `django.shortcuts`

**commit: `Урок 2: рендер первого шаблона`**

### Работа с шаблоном 

1. Создали словарь с данными в `views.py` и передали его в шаблон
```python
info = {
    "users_count": 100600,
    "news_count": 1000,
}
```
2. Вставили данные в шаблон `catalog.html` с помощью шаблонного языка `Django` (`DTL`)
3. Подключили `BS5` по `CDN` и стилизовали страницу

**commit: `Урок 2: передаём первые данные в шаблон и подключил BS5`*

### Смотрим типы данных внутри шаблона

- Проверили, что можно передать только словарь
- Передали список и вывели его в шаблоне
- Передали список меню и познакомились с конструкцией `{% for item in menu %}`
- Познакомились с конструкцией `{% comment %} {% endcomment %}` для комментирования участков шаблона

**commit: `Урок 2: первый цикл в шаблоне`**

### Посмотрели на тег шаблона `if`
- Сделали `<hr>` после каждого элемента списка, кроме последнего с помощью специальной переменной `forloop.last`

**commit: `Урок 2: первый тег if в шаблоне`**

### Сделали ссылки в меню кликабельными
- Передали в шаблон список словарей, где каждый словарь содержит `url` и `title`
- Переделали маршрут `info` в `about`

**commit: `Урок 2: сделали ссылки в меню кликабельными`**

- Описали маршруты 
  `/catalog`,
  `/catalog/<int:news_id/>`,
  `/catalog/<slug:slug>`
  и создали соответствующие представления в файле `views.py`
- `catalog` возвращает `HttpResponse("Каталог новостей")`
- `get_news_by_id` возвращает `HttpResponse(f"Новость {news_id}")`
- `get_category_by_name` возвращает `HttpResponse(f"Карточка {slug}")`

**commit: `Урок 2: добавили новые маршруты`**

### Изменение структуры news/url.py` и `news/views.py`
Изменил пути и функции для дальнейшего развития проекта.
Дописали `include` в `urls.py` приложения `itg`

**commit: `Урок 2: изменение структуры путей`**


## Урок 3

### Создание базового шаблона `base.html` в корне проекта в папке `templates`

- Создали базовый шаблон `base.html` в папке `templates`
- Указали кастомный, нестандартный путь для Django в файле `settings.py` в разделе `TEMPLATES` 
- Прописали там `BASE_DIR / 'templates',`
- Подключили базовый шаблон для теста функции `main` в файле `views.py`

**commit: `Урок 3: создали базовый шаблон base.html`**

### Синтаксис блоков в шаблонах. `{% block %}` и `{% extends %}`

- Описали блок `content` в базовом шаблоне `base.html`
- Описали блок `footer` в базовом шаблоне `base.html`
- Создали шаблон `main.html` в папке `templates`, который расширяет базовый шаблон `base.html` через `{% extends %}`
- Переопределили блок `content` в шаблоне `main.html` через `{% block %}`
- Переопределили блок `footer` в шаблоне `main.html` через `{% block %}`
- Подключили шаблон `main.html` в функции `main` в файле `views.py`

**commit: `Урок 3: создали шаблон main.html и расширили базовый шаблон base.html`**

### Создание шаблона `nav_menu.html` и подключение его в базовом шаблоне через `{% include %}`

- Создали каталог `include` в папке `templates` в корне проекта
- Создали шаблон `nav_menu.html` в папке `include`
- Написали навигационное меню в шаблоне `nav_menu.html`
- Использовали шаблонный тег `{% url %}` который позволяет создавать ссылки на страницы по их именам в файле `urls.py`
- Подключили шаблон `nav_menu.html` в базовом шаблоне `base.html` через `{% include %}`
- Добавили датасет с новостями и меню, чтобы в будущем проверить работу шаблона

**commit: `Урок 3: создали шаблон nav_menu.html и подключили его в базовом шаблоне`**

### Начали работу над каталогом новостей (динамическая вставка данных в шаблон, цикл + `include`)

- Создали `include` в папке `templates` в приложении `news`
- Внутри создали шаблон `article_preview.html`
- Шаблон `article_preview.html` пока что только выводит сообщение `hello`
- Подключили шаблон `article_preview.html` в шаблоне `catalog.html` через `{% include %}`

**commit: `Урок 3: начали работу над каталогом новостей и динамической вставкой данных в шаблон`**

### Продолжили работу над каталогом статей (динамическая вставка данных в шаблон, цикл + `include`)

- Добавили шаблон `article_detail.html` в папке `templates/news` 
- Доделали `article_preview.html` в папке `templates/news`, распарсив в нём поля `title`, `category`, `tags`, `id_author`, `id_article`, `upload_date`, `views_count`, `favorites_count`
- Те же поля + `content` распарсили в `article_detail.html`
- Обновили функцию `get_detail_article_by_id` - сделали поиск статьи по `id_article` в словаре и возврат шаблона `article_detail.html` ИЛИ `404`

**commit: `Урок 3: доделали каталог новостей и детальное отображение статьи по id_article`**

### Создали папку `static` в приложении `news` и подключили статику в шаблоне `base.html`

- Создали папку `static` в приложении `news`
- Создали папку `news` в папке `static`
- В ней создали папку `css` и файл `main.css`, а так же папку `js` и файл `main.js`
- Создали тестовые стили и скрипт
- Подключили статику в шаблоне `base.html` через тег `{% load static %}` и тег `{% static %}`
- Подключили стили и скрипт в шаблоне `base.html`
- Проверили работу статики на всех страницах
- После создания и подключения статики нужно перезапустить сервер

**commit: `Урок 3: подключили статику в шаблоне base.html`**

### Собственные шаблонные теги через `simple_tag`

- Создали тег шаблона `upper_words` через `simple_tag` в файле `news/templatetags/upper_words.py`
- Протестировали его в представлении `article_detail` в шаблоне `article_detail.html`
- После создания тега и регистрации с помощью `template.Library()` нужно перезапустить сервер

**commit: `Урок 3: создал собственный тег шаблона upper_words через simple_tag`**

### Работа с фильтрами в шаблонах
Посмотрели на работу следующих фильтров в шаблоне `article_preview.html`:
- `length`
- `truncatechars`
- `join`
Так же, в шаблон был добавлен цикл для вывода тегов новости.

**commit: `Урок 3: работа с фильтрами в шаблонах`**


## Урок 4

### Инициализирующие миграции
Применили 18 стартовых миграций для создания структуры БД и настройки
`python manage.py migrate`
Инициализирующая миграция — это первая миграция, которая создается при инициализации нового приложения в Django.
Она содержит начальную структуру базы данных, основанную на моделях, определенных в вашем приложении.
Инициализирующая миграция важна для установления базовой схемы базы данных, с которой будет работать ваше приложение.
`auth`: Миграции для приложения аутентификации, которое включает модели пользователей, групп и разрешений.
`contenttypes`: Миграции для приложения, которое отслеживает типы контента в базе данных.
`sessions`: Миграции для приложения, которое управляет сессиями пользователей.
`admin`: Миграции для административного интерфейса `Django`.

**commit: `Урок 4: применение инициализирующих миграций`**

### Создаём первую модель данных
1. Описание модели
```python
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
```
2. Создание миграции
`python manage.py makemigrations`
3. Применение миграции
`python manage.py migrate`

**commit: `Урок 4: создание модели данных статьи и применение миграции`**

### Знакомство с `Shell Plus` и работа с моделью `Article` в интерактивной оболочке `Django`
- Установили `Shell Plus` командой `pip install django-extensions`
- Добавили `django_extensions` в `INSTALLED_APPS` в файле `settings.py` (перед нашим приложением `news`) 
- Запустили `Shell Plus` командой `python manage.py shell_plus`
(для отображения `SQL` запросов в консоли - `python manage.py shell_plus --print-sql`)
(для выхода из консоли `Shell Plus` - `exit()`)

**commit: `Урок 4: установка Shell Plus и подготовка ORM`**

### Загрузка данных в базу данных из JSON файла
`python manage.py loaddata articles.json`

**commit: `Урок 4: Наполнили базу данных тестовыми данными`**

### Операции CRUD в базе данных
```python
# Откройте Django Shell Plus
python manage.py shell_plus

# Импортируйте модель Article
from news.models import Article

# Создание новой статьи
new_article = Article(
    title="Вода стала розовой!",
    content="Вчера вода во всех реках и озерах стала розовой. Ученые обещают найти причину этого явления.",
    publication_date="2023-10-31T12:00:00Z",
    views=0
)
new_article.save()

# Чтение всех статей
all_articles = Article.objects.all()
for article in all_articles:
    print(article.title, article.content, article.publication_date, article.views)
    
# Чтение одной статьи по её ID
article = Article.objects.get(pk=1)
print(article.title, article.content, article.publication_date, article.views)

# Обновление статьи
article.title = "Обновленная абсурдная новость"
article.content = "Обновленное содержание абсурдной новости"
article.save()

# Удаление статьи
article.delete()
```
**commit: `Урок 4: Посмотрели операции CRUD через командную строку`**


## Урок 5

### Расширили модель данных тегами и категориями через связи `ForeignKey` и `ManyToManyField`
```python
class Article(models.Model):
    ...
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField('Tag', related_name='article')
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
```
### Создали миграции с помощью команды `python manage.py makemigrations`
### Применили миграции с помощью команды `python manage.py migrate`

**commit: `Урок 5: Добавили модели данных Category и Tag`**

Загрузили новые данные соответствующие новым моделям с помощью команды `python manage.py loaddata articles_2.json`

**commit: `Урок 5: Загрузка новых данных`**

### Рассмотрели примеры в `Django ORM`
```python
# Откройте Django Shell
# python manage.py  shell_plus

# Создайте новый тег
new_tag = Tag(name="Новый тег")
new_tag.save()

# Создайте новую категорию
new_category = Category(name="Новая категория")
new_category.save()

# Создайте новую статью с этим тегом и категорией
new_article = Article(
    title="Новая абсурдная новость",
    content="Содержание новой абсурдной новости",
    category=new_category
)
new_article.save()
new_article.tags.add(new_tag)

# Чтение всех категорий
all_categories = Category.objects.all()
for category in all_categories:
    print(category.name)
    
# Чтение всех тегов
all_tags = Tag.objects.all()
for tag in all_tags:
    print(tag.name)
    
# Чтение всех статей
all_articles = Article.objects.all()
for article in all_articles:
    print(article.title, article.content, article.category.name, [tag.name for tag in article.tags.all()])

# Чтение одной категории по её ID
category = Category.objects.get(pk=1)
print(category.name)

# Чтение одного тега по его ID
tag = Tag.objects.get(pk=1)
print(tag.name)

# Чтение одной статьи по её ID
article = Article.objects.get(pk=1)
print(article.title, article.content, article.category.name, [tag.name for tag in article.tags.all()])

# Обновите тег
tag = Tag.objects.get(name="Новый тег")
tag.name = "Обновленный тег"
tag.save()

# Обновите категорию
category = Category.objects.get(name="Новая категория")
category.name = "Обновленная категория"
category.save()

# Обновите статью
article = Article.objects.get(title="Новая абсурдная новость")
article.title = "Обновленная абсурдная новость"
article.content = "Обновленное содержание абсурдной новости"
article.save()

# Обновите теги статьи
new_tag = Tag.objects.get(name="Обновленный тег")
article.tags.add(new_tag)

# Удаление категории
category = Category.objects.get(name="Обновленная категория")
category.delete()

# Удаление тега
tag = Tag.objects.get(name="Обновленный тег")
tag.delete()

# Удаление статьи
article = Article.objects.get(title="Обновленная абсурдная новость")
article.delete()
```
**commit: `Урок 5: Посмотрели операции CRUD через командную строку`**

#### Импортировали модели в `news/views.py`
```python
from .models import Article
```

#### Переписали представления для показа каталога новостей и подробного показа новости
```python
def get_all_news(request):
    articles = Article.objects.all()
    context = {
        'news': articles,
        'menu': [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "catalog"},
        ],
    }
    return render(request, 'news/catalog.html', context=context)

def get_detail_article_by_id(request, article_id):
    """
    Возвращает детальную информацию по новости для представления
    """
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
        'menu': [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "catalog"},
        ],
    }
    return render(request, 'news/article_detail.html', context=context)
```

**commit: `Урок 5: Подключили модели данных к представлениям`**

### Сделали ORM запросы на выборку по тегам и категориям

#### Выборка статей по категории
```python
# Пример: Получение всех статей в категории "Технологии"
category_name = "Технологии"
category = Category.objects.get(name=category_name)
articles_in_category = Article.objects.filter(category=category)
for article in articles_in_category:
    print(article.title)
```

#### Выборка статей по тегу
```python
# Пример: Получение всех статей с тегом "Инновации"
tag_name = "Инновации"
tag = Tag.objects.get(name=tag_name)
articles_with_tag = Article.objects.filter(tags=tag)
for article in articles_with_tag:
    print(article.title)
```

#### Выборка статей по категории и тегу
```python
# Пример: Получение всех статей в категории "Наука" и с тегом "Исследования"
category_name = "Наука"
tag_name = "Исследования"
category = Category.objects.get(name=category_name)
tag = Tag.objects.get(name=tag_name)
articles_in_category_and_tag = Article.objects.filter(category=category, tags=tag)
for article in articles_in_category_and_tag:
    print(article.title)
```
**commit: `Урок 5: Посмотрели операции на выборку новостей по тегу и/или категории`**


## Урок 6

### Задача: Получить все статьи, которые принадлежат категории "Технологии".

```python
# Получаем объект категории "Технологии"
technology_category = Category.objects.get(name="Технологии")
# Фильтруем статьи по этой категории
articles_in_technology = Article.objects.filter(category=technology_category)
# Выводим результат
for article in articles_in_technology:
    print(article.title)
```

### Задача: Получить все статьи, которые имеют тег "Инновации".
```python
# Получаем объект тега "Инновации"
innovation_tag = Tag.objects.get(name="Инновации")
# Фильтруем статьи по этому тегу
articles_with_innovation_tag = Article.objects.filter(tags=innovation_tag)
# Выводим результат
for article in articles_with_innovation_tag:
    print(article.title)
```

### Задача: Получить все статьи, отсортированные по заголовку в порядке убывания
```python
# Сортируем статьи по заголовку в порядке убывания
articles_sorted_by_title = Article.objects.all().order_by('-title')
# Выводим результат
for article in articles_sorted_by_title:
    print(article.title, article.id)
```

### Задача: Получить все статьи, у которых количество просмотров больше 10, отсортированные по количеству просмотров в порядке возрастания.
Для начала можно изменить у некоторых статей количество просмотров, чтобы выборка имела смысл
```python
# Фильтруем статьи, у которых id больше 30, и обновляем их количество просмотров
Article.objects.filter(id__gt=30).update(views=20)
```
```python
# Фильтруем статьи по количеству просмотров и сортируем их
articles_filtered_and_sorted = Article.objects.filter(views__gt=10).order_by('views')
# Выводим результат
for article in articles_filtered_and_sorted:
    print(article.title, article.views)
```

**commit: `Урок 6: Рассмотрели операции на фильтрацию и сортировку данных, а так же лукапы`**

### Решение первой практики

### Задание 1: Фильтрация статей по категории
**Задача:** Получить все статьи, которые принадлежат категории "Технологии".
**Решение:**
```python
# Получаем объект категории "Технологии"
technology_category = Category.objects.get(name="Технологии")
# Фильтруем статьи по этой категории
articles_in_technology = Article.objects.filter(category=technology_category)
# Выводим результат
for article in articles_in_technology:
    print(article.title)
```
**Пояснение:**
1. Получаем объект категории "Технологии".
2. Фильтруем статьи, которые принадлежат этой категории.
3. Выводим заголовки всех статей, которые соответствуют этой категории.

### Задание 2: Фильтрация статей по тегу
**Задача:** Получить все статьи, которые имеют тег "Инновации".
**Решение:**
```python
# Получаем объект тега "Инновации"
innovation_tag = Tag.objects.get(name="Инновации")
# Фильтруем статьи по этому тегу
articles_with_innovation_tag = Article.objects.filter(tags=innovation_tag)
# Выводим результат
for article in articles_with_innovation_tag:
    print(article.title)
```
**Пояснение:**
1. Получаем объект тега "Инновации".
2. Фильтруем статьи, которые имеют этот тег.
3. Выводим заголовки всех статей, которые соответствуют этому тегу.

### Задание 3: Сортировка статей по дате публикации
**Задача:** Получить все статьи, отсортированные по дате публикации в порядке убывания.
**Решение:**
```python
# Сортируем статьи по дате публикации в порядке убывания
articles_sorted_by_date = Article.objects.all().order_by('-publication_date')
# Выводим результат
for article in articles_sorted_by_date:
    print(article.title, article.publication_date)
```
**Пояснение:**
1. Сортируем статьи по дате публикации в порядке убывания.
2. Выводим заголовки и даты публикации всех статей.

### Задание 4: Фильтрация и сортировка статей по количеству просмотров
**Задача:** Получить все статьи, у которых количество просмотров больше 10, отсортированные по количеству просмотров в порядке возрастания.
**Решение:**
```python
# Фильтруем статьи по количеству просмотров и сортируем их
articles_filtered_and_sorted = Article.objects.filter(views__gt=10).order_by('views')
# Выводим результат
for article in articles_filtered_and_sorted:
    print(article.title, article.views)
```
**Пояснение:**
1. Фильтруем статьи, у которых количество просмотров больше 10.
2. Сортируем эти статьи по количеству просмотров в порядке возрастания.
3. Выводим заголовки и количество просмотров всех статей, которые соответствуют условию.

### Задание 5: Фильтрация статей по содержанию
**Задача:** Получить все статьи, у которых содержание содержит слово "кошки".
**Решение:**
```python
# Фильтруем статьи по содержанию
articles_with_cats_in_content = Article.objects.filter(content__icontains="кошки")
# Выводим результат
for article in articles_with_cats_in_content:
    print(article.title)
```
**Пояснение:**
1. Фильтруем статьи, у которых заголовок содержит слово "кошки" без учета регистра.
2. Выводим заголовки всех статей, которые соответствуют этому условию.

### Задание 6: Фильтрация статей по диапазону дат
**Задача:** Получить все статьи, опубликованные в октябре 2023 года.
**Решение:**
```python
# Фильтруем статьи по диапазону дат
articles_in_october_2023 = Article.objects.filter(publication_date__range=(datetime(2023, 10, 1), datetime(2023, 10, 31)))
# Выводим результат
for article in articles_in_october_2023:
    print(article.title, article.publication_date)
```
**Пояснение:**
1. Фильтруем статьи, опубликованные в октябре 2023 года.
2. Выводим заголовки и даты публикации всех статей, которые соответствуют этому условию.

### Задание 7: Фильтрация статей по году публикации
**Задача:** Получить все статьи, опубликованные в 2023 году.
**Решение:**
```python
# Фильтруем статьи по году публикации
articles_in_2023 = Article.objects.filter(publication_date__year=2023)
# Выводим результат
for article in articles_in_2023:
    print(article.title, article.publication_date)
```
**Пояснение:**
1. Фильтруем статьи, опубликованные в 2023 году.
2. Выводим заголовки и даты публикации всех статей, которые соответствуют этому условию.

### Задание 8: Фильтрация статей по наличию тегов
**Задача:** Получить все статьи, у которых есть хотя бы один тег.
**Решение:**
```python
# Фильтруем статьи, у которых есть хотя бы один тег
articles_with_tags = Article.objects.filter(tags__isnull=False)
# Выводим результат
for article in articles_with_tags:
    print(article.title)
```
**Пояснение:**
1. Фильтруем статьи, у которых есть хотя бы один тег.
2. Выводим заголовки всех статей, которые соответствуют этому условию.

### Задание 9: Фильтрация статей по количеству тегов
**Задача:** Получить все статьи, у которых количество тегов больше 3.
**Решение:**
```python
# Фильтруем статьи по количеству тегов
articles_with_more_than_three_tags = Article.objects.annotate(num_tags=Count('tags')).filter(num_tags__gt=3)
# Выводим результат
for article in articles_with_more_than_three_tags:
    print(article.title, article.num_tags)
```
**Пояснение:**
1. Аннотируем статьи, подсчитывая количество тегов для каждой статьи.
В `Django ORM` метод `annotate` используется для добавления дополнительных полей
к каждому объекту в `QuerySet` на основе агрегатных функций,
таких как `Count`, `Sum`, `Avg`, `Max`, `Min` и другие.
Эти дополнительные поля могут быть использованы для фильтрации,
сортировки или просто для получения дополнительной информации о каждом объекте.
2. Фильтруем статьи, у которых количество тегов больше 3.
3. Выводим заголовки и количество тегов всех статей, которые соответствуют этому условию.

### Задание 10: Фильтрация статей по наличию определенного слова в контенте
**Задача:** Получить все статьи, у которых контент содержит слово "открыли".
**Решение:**
```python
# Фильтруем статьи по наличию слова "открыли" в заголовке
articles_with_open_in_title = Article.objects.filter(title__icontains="открыли")
# Выводим результат
for article in articles_with_open_in_title:
    print(article.title)
```
**Пояснение:**
1. Фильтруем статьи, у которых заголовок содержит слово "открыли" без учета регистра.
2. Выводим заголовки всех статей, которые соответствуют этому условию.

**commit: `Урок 6: Разобрали первое практическое задание`**

### Новое поле `slug` в модели данных `Article`

#### Сначала нужно очистить БД
`python manage.py flush`

#### Добавляем `slug` и переопределяем метод сохранения
```python
from django.utils.text import slugify
class Article(models.Model):
    ...
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
```

#### Создаём миграцию
`python manage.py makemigrations`

#### Применяем миграцию
`python manage.py migrate`

#### Загружаем новый дамп данных
`python manage.py loaddata articles_3.json`

**commit: `Урок 6: Добавили slug в Article`**

### Добавление слага в маршруты и представления
```python
# news/urls.py
urlpatterns = [
    ...
    path('catalog/<slug:slug>/', views.get_detail_article_by_slag, name='detail_article_by_slag'),
]
```
```python
# news/views.py
def get_detail_article_by_slag(request, slug):
    article = get_object_or_404(Article, slug=slug)
    ...
    return render(request, 'news/article_detail.html', context=context)
```

**commit: `Урок 6: Добавление slug в маршруты и представления`**

### Добавление пользовательского менеджера модели

#### Создание пользовательского менеджера

```python
class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    def sorted_by_title(self):
        return self.get_queryset().all().order_by('-title')
```

#### Добавление пользовательского менеджера в модель
```python
class Article(models.Model):
    ...
    is_active = models.BooleanField(default=True)
    objects = ArticleManager()
```

#### Создание миграции
`python manage.py makemigrations`

#### Применение миграции
`python manage.py migrate`

#### Проверка пользовательского менеджера модели в shell_plus
```python
published_articles = Article.objects.sorted_by_title()
for i in published_articles:
    print(i.title)
```

**commit: `Урок 6: Добавление пользовательского менеджера модели Article`**

### Исправление `slug` в модели данных `Article`
`unidecode` — это библиотека `Python`, которая преобразует `Unicode`-строки в ближайшие эквиваленты `ASCII`.
Это полезно, когда вам нужно удалить или заменить не-`ASCII` символы в строке,
чтобы сделать её более совместимой с системами, которые не поддерживают `Unicode`.

#### Установка `unidecode`
`pip install unidecode`

#### Применение `unidecode` к `slug` в модели данных `Article`
```python
from django.utils.text import slugify
from unidecode import unidecode


class Article(models.Model):
    ...
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Сохраняем статью, чтобы получить id
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(unidecode.unidecode(self.title))
            self.slug = f"{base_slug}-{self.id}"

        # Сохраняем статью снова, чтобы обновить слаг
        super().save(*args, **kwargs)
```

#### Проверка работы slugify и unidecode
```python
# Создаем категорию, если она еще не существует
category, created = Category.objects.get_or_create(name="Технологии")

# Создаем теги, если они еще не существуют
tag1, created = Tag.objects.get_or_create(name="Технологии")
tag2, created = Tag.objects.get_or_create(name="Инновации")

# Создаем статью
article = Article(
    title="Новая статья о технологиях",
    content="Это тестовая статья для проверки работы поля slug.",
    category=category,
)

# Сохраняем статью, чтобы убедиться, что slug был сгенерирован
article.save()

# Добавляем теги к статье
article.tags.add(tag1, tag2)

# Выводим информацию о статье, чтобы убедиться, что slug был сгенерирован
print(f"Title: {article.title}")
print(f"Slug: {article.slug}")
print(f"Content: {article.content}")
print(f"Category: {article.category.name}")
print(f"Tags: {', '.join([tag.name for tag in article.tags.all()])}")
```

**commit: `Урок 6: Исправили `slug`**


## Урок 7

### Очистка базы данных
`python manage.py flush`

### Загрузка новых данных
`python manage.py loaddata articles_4.json`

**commit: `Урок 7: Подготовка данных`**

### Класс Q
```python
# Пример 1: Простое использование Q
# Создаем объекты Q для условий
category_q = Q(category__name='Технологии')
tag_q = Q(tags__name='Инновации')
# Комбинируем условия с помощью логического оператора OR
articles = Article.objects.filter(category_q | tag_q)

# Пример 2: Комбинирование условий с AND и OR
# Создаем объекты Q для условий
category_q = Q(category__name='Наука')
tag_q1 = Q(tags__name='Исследования')
tag_q2 = Q(tags__name='Инновации')
# Комбинируем условия с помощью логических операторов
articles = Article.objects.filter(category_q & (tag_q1 | tag_q2))

# Пример 3: Использование NOT
# Создаем объект Q для условия
category_q = Q(category__name='Спорт')
# Используем логический оператор NOT
articles = Article.objects.filter(~category_q)

# Пример 4: Комбинирование нескольких условий
# Создаем объекты Q для условий
category_q1 = Q(category__name='Технологии')
category_q2 = Q(category__name='Наука')
tag_q1 = Q(tags__name='Инновации')
tag_q2 = Q(tags__name='Исследования')
# Комбинируем условия с помощью логических операторов
articles = Article.objects.filter((category_q1 | category_q2) & (tag_q1 | tag_q2))
```

**commit: `Урок 7: Класс Q`**

### Методы exists() и count(): Проверка наличия данных и подсчёт записей
```python
# Пример 1: Проверка наличия статей в категории "Технологии"
# Проверяем наличие статей в категории "Технологии"
exists = Article.objects.filter(category__name='Технологии').exists()
print(exists)  # Выведет True или False

# Пример 2: Подсчет количества статей в категории "Наука"
# Подсчитываем количество статей в категории "Наука"
count = Article.objects.filter(category__name='Наука').count()
print(count)  # Выведет количество статей

# Пример 3: Проверка наличия статей с тегом "Инновации" или "Исследования"
# Создаем объекты Q для условий
tag_q1 = Q(tags__name='Инновации')
tag_q2 = Q(tags__name='Исследования')
# Проверяем наличие статей с тегами "Инновации" или "Исследования"
exists = Article.objects.filter(tag_q1 | tag_q2).exists()
print(exists)  # Выведет True или False

# Пример 4: Подсчет количества статей в категории "Технологии" или "Наука"
# Создаем объекты Q для условий
category_q1 = Q(category__name='Технологии')
category_q2 = Q(category__name='Наука')
# Подсчитываем количество статей в категории "Технологии" или "Наука"
count = Article.objects.filter(category_q1 | category_q2).count()
print(count)  # Выведет количество статей
```

**commit: `Урок 7: Методы exists() и count()`**

### Класс F, Value и метод annotate(): Выполнение операций с полями внутри запросов
```python
# Пример 1: Увеличение количества просмотров статьи
# Найдем статью по slug и увеличим количество просмотров на 1
Article.objects.filter(slug='17-kroty-otkryli-restoran').update(views=F('views') + 1)

# Пример 2: Аннотация статей с константным значением
# Аннотируем все статьи с константным значением is_featured
articles = Article.objects.annotate(is_featured=Value(True))
for article in articles:
    print(article.is_featured)  # Выведет True для всех статей
    
# Пример 3: Аннотация статей с количеством просмотров, увеличенным на 10
# Аннотируем все статьи с количеством просмотров, увеличенным на 10
articles = Article.objects.annotate(increased_views=F('views') + 10)
for article in articles:
    print(article.increased_views)  # Выведет количество просмотров, увеличенное на 10
```
**commit: `Урок 7: Класс F, Value и метод annotate()`**

### Агрегация данных: Использование Count, Sum, Avg, Max, Min и метода values()
```python
# Пример 1: Подсчет количества статей в каждой категории
# Подсчитываем количество статей в каждой категории
category_counts = Article.objects.values('category__name').annotate(count=Count('id'))
for category in category_counts:
    print(f"Category: {category.name}, Count: {category.count}")

# Пример 2: Суммирование количества просмотров всех статей
# Подсчитываем суммарное количество просмотров всех статей
total_views = Article.objects.aggregate(total_views=Sum('views'))
print(f"Total Views: {total_views['total_views']}")

# Пример 3: Вычисление среднего количества просмотров статей
# Вычисляем среднее количество просмотров статей
average_views = Article.objects.aggregate(average_views=Avg('views'))
print(f"Average Views: {average_views['average_views']}")

# Пример 4: Нахождение максимального и минимального количества просмотров статей
# Находим максимальное и минимальное количество просмотров статей
max_views = Article.objects.aggregate(max_views=Max('views'))
min_views = Article.objects.aggregate(min_views=Min('views'))
print(f"Max Views: {max_views['max_views']}")
print(f"Min Views: {min_views['min_views']}")

# Пример 5: Подсчет количества статей в каждой категории с использованием values() и annotate()
# Подсчитываем количество статей в каждой категории
category_counts = Article.objects.values('category__name').annotate(count=Count('id'))
for category in category_counts:
    print(f"Category: {category['category__name']}, Count: {category['count']}")
```

**commit: `Урок 7: Агрегация данных`**

### Практика

```python
from django.utils import timezone
# Задача 1: Найти все статьи, которые были опубликованы после 31 октября 2023 года.
# Фильтрация статей по дате публикации, которая больше 31 октября 2023 года.
articles = Article.objects.filter(publication_date__gt=timezone.datetime(2023, 10, 31))
print(articles)

# Задача 2: Найти все статьи, которые принадлежат категории "Образование" и имеют тег "Инновации".
# Создание объектов Q для условий фильтрации для категории "Образование" и тега "Инновации".
category_q = Q(category__name='Образование')
tag_q = Q(tags__name='Инновации')
# Комбинирование условий с использованием логического оператора AND.
articles = Article.objects.filter(category_q & tag_q)
print(articles)

# Задача 3: Найти все статьи, которые не принадлежат категории "Культура".
# Создание объекта Q для условия фильтрации для категории "Культура".
category_q = Q(category__name='Культура')
# Использование логического оператора NOT для инвертирования условия.
articles = Article.objects.filter(~category_q)
print(articles)

# Задача 4: Найти все статьи, которые принадлежат категории "Здоровье" или "Образование" и имеют тег "Исследования".
# Создание объектов Q для условий фильтрации для категорий "Здоровье" и "Образование" и тега "Исследования".
category_q1 = Q(category__name='Здоровье')
category_q2 = Q(category__name='Образование')
tag_q = Q(tags__name='Исследования')
# Комбинирование условий с использованием логических операторов OR и AND.
articles = Article.objects.filter((category_q1 | category_q2) & tag_q)
print(articles)

# Задача 5: Увеличить количество просмотров всех статей на 5.
# Использование класса F для создания выражения, которое ссылается на поле views.
# Обновление всех записей в таблице Article, увеличивая количество просмотров на 5.
Article.objects.update(views=F('views') + 5)

# Задача 6: Аннотировать все статьи с константным значением `is_featured` равным `False`.
# Использование метода annotate() для добавления нового поля is_featured со значением False ко всем статьям.
articles = Article.objects.annotate(is_featured=Value(False))
for article in articles:
    print(article.is_featured)  # Выведет False для всех статей
    
# Задача 7: Найти все статьи, которые были опубликованы в 2023 году.
# Фильтрация статей по году публикации, который равен 2023.
articles = Article.objects.filter(publication_date__year=2023)
print(articles)

# Задача 8: Найти все статьи, которые принадлежат категории "Технологии" и имеют тег "Инновации".
# Создание объектов Q для условий фильтрации для категории "Технологии" и тега "Инновации".
category_q = Q(category__name='Технологии')
tag_q = Q(tags__name='Инновации')
# Комбинирование условий с использованием логического оператора AND.
articles = Article.objects.filter(category_q & tag_q)
print(articles)

# Задача 9: Подсчитать количество статей в каждой категории.
# Использование метода values() для выбора поля category__name, по которому будем группировать данные.
# Использование метода annotate() для добавления нового поля count, которое представляет собой количество статей в каждой категории.
category_counts = Article.objects.values('category__name').annotate(count=Count('id'))
for category in category_counts:
    print(f"Category: {category['category__name']}, Count: {category['count']}")

# Задача 10: Подсчитать суммарное количество просмотров всех статей.
# Использование метода aggregate() для выполнения агрегатной операции суммирования над полем views.
total_views = Article.objects.aggregate(total_views=Sum('views'))
print(f"Total Views: {total_views['total_views']}")

# Задача 11: Найти статьи, у которых количество просмотров больше 150.
# Фильтрация статей по количеству просмотров, которое больше 150.
articles = Article.objects.filter(views__gt=150)
print(articles)

# Задача 12: Найти статьи, у которых количество просмотров меньше или равно 200.
# Фильтрация статей по количеству просмотров, которое меньше или равно 200.
articles = Article.objects.filter(views__lte=200)
print(articles)
```

**commit: `Урок 7: Практика`**

- установили отладочную панель `Django` (`pip install django-debug-toolbar`) и настроили её
- убедились в том, что наше приложение генерирует слишком много запросов

**commit: `Урок 7: Установили отладочную панель Django`**

#### включили жадную загрузку и снизили количество запросов до 4
```python
articles = Article.objects.select_related('category').prefetch_related('tags')
```

### `prefetch_related` и `select_related`
`prefetch_related` и `select_related` — это методы оптимизации запросов в `Django ORM`,
которые используются для уменьшения количества запросов к базе данных и повышения производительности при работе с моделями,
связанными через внешние ключи или отношения "многие ко многим".

#### `select_related`
`select_related` используется для выполнения запросов к моделям, связанных через внешние ключи (`ForeignKey`).
Это позволяет получить все необходимые данные за один запрос,
вместо того чтобы выполнять отдельные запросы для каждого связанного объекта.

#### `prefetch_related`
`prefetch_related` используется для выполнения отдельных запросов для получения связанных объектов,
но делает это более эффективно, чем выполнение отдельных запросов для каждого связанного объекта.
Это особенно полезно для отношений "многие ко многим" (`ManyToManyField`) и обратных отношений (`reverse ForeignKey`).

#### Основные различия
1. **Тип отношений**:
   - `select_related` работает с однозначными отношениями (`ForeignKey` и `OneToOneField`).
   - `prefetch_related` работает с отношениями "многие ко многим" (`ManyToManyField`) и обратными отношениями (`reverse ForeignKey`).
2. **Механизм работы**:
   - `select_related` использует `SQL`-объединения (`JOIN`), что может быть более эффективно для небольших наборов данных.
   - `prefetch_related` выполняет отдельные запросы для получения связанных объектов, что может быть более эффективно для больших наборов данных или сложных отношений.
3. **Производительность**:
   - `select_related` может быть быстрее для небольших наборов данных, так как выполняет меньше запросов.
   - `prefetch_related` может быть более эффективен для больших наборов данных, так как выполняет отдельные запросы для связанных объектов, что может уменьшить нагрузку на базу данных.

### Ленивая загрузка (`Lazy Loading`) и Жадная загрузка (`Eager Loading`)
В `Django ORM` ленивая загрузка (`lazy loading`) и жадная загрузка (`eager loading`) — это два подхода к загрузке связанных данных, которые могут существенно повлиять на производительность вашего приложения. Выбор между ними зависит от конкретных требований и сценариев использования.

#### Ленивая загрузка (`Lazy Loading`)
Ленивая загрузка — это подход, при котором связанные данные загружаются только тогда, когда они действительно нужны.
Это поведение по умолчанию в `Django ORM`.
**Преимущества:**
- **Экономия ресурсов:** Данные загружаются только при необходимости, что может снизить нагрузку на базу данных и уменьшить использование памяти.
- **Простота:** Не требует дополнительных настроек или оптимизаций.
**Недостатки:**
- **N+1 проблема:** Может привести к большому количеству запросов к базе данных, если связанные данные загружаются в цикле.
**Пример:**
```python
articles = Article.objects.all()
for article in articles:
    print(article.title)  # Каждый раз выполняется отдельный запрос для получения статьи
```

#### Жадная загрузка (`Eager Loading`)
Жадная загрузка — это подход, при котором связанные данные загружаются заранее, в один или несколько запросов.
В `Django` это достигается с помощью методов `select_related` и `prefetch_related`.
**Преимущества:**
- **Снижение количества запросов:** Уменьшает количество запросов к базе данных, что может значительно повысить производительность.
- **Оптимизация:** Позволяет более эффективно использовать ресурсы базы данных и памяти.
**Недостатки:**
- **Избыточность:** Может загружать данные, которые в итоге не понадобятся, что может привести к избыточному использованию памяти.
- **Сложность:** Требует дополнительных настроек и оптимизаций.
**Пример с `select_related` и `prefetch_related`:**
```python
articles = Article.objects.select_related('category').prefetch_related('tags')
for article in articles:
    print(article.title)  # Все книги загружены заранее, один запрос к базе данных для category и несколько для tags
```

#### Когда использовать ленивую загрузку
- **Простые запросы:** Когда вы знаете, что связанные данные будут загружаться редко или только для небольшого числа объектов.
- **Малые наборы данных:** Когда работаете с небольшими наборами данных, где дополнительные запросы не будут существенно влиять на производительность.
- **Прототипирование:** На этапе разработки и тестирования, когда производительность не является критичной.

#### Когда использовать жадную загрузку
- **Сложные запросы:** Когда вы знаете, что будете часто обращаться к связанным данным, особенно в циклах.
- **Большие наборы данных:** Когда работаете с большими наборами данных, где множество отдельных запросов могут существенно замедлить выполнение.
- **Производительность:** В производственных системах, где производительность критична и необходимо минимизировать количество запросов к базе данных.

Выбор между ленивой и жадной загрузкой зависит от конкретных требований вашего приложения.
Ленивая загрузка проще в использовании и может быть достаточной для простых сценариев,
тогда как жадная загрузка требует дополнительных настроек,
но может значительно повысить производительность в сложных и ресурсоёмких запросах.

**commit: `Урок 7: включили жадную загрузку`**


## Урок 8

### Немного об SQL

`SQL` (`Structured Query Language`) — это стандартный язык для работы с реляционными базами данных. Он позволяет выполнять различные операции, такие как создание, изменение, удаление и извлечение данных.

#### Основные команды SQL:
- **SELECT**: Извлечение данных из базы данных.
- **INSERT**: Добавление новых данных в таблицу.
- **UPDATE**: Обновление существующих данных в таблице.
- **DELETE**: Удаление данных из таблицы.
- **CREATE**: Создание новых таблиц или баз данных.
- **ALTER**: Изменение структуры существующей таблицы.
- **DROP**: Удаление таблицы или базы данных.

#### Примеры использования:
- **SELECT**: `SELECT * FROM users;`
- **INSERT**: `INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');`
- **UPDATE**: `UPDATE users SET email = 'newemail@example.com' WHERE name = 'John Doe';`
- **DELETE**: `DELETE FROM users WHERE name = 'John Doe';`

`SQL` является мощным инструментом для управления данными и используется в различных системах управления базами данных (СУБД), таких как `PostgreSQL`, `MySQL`, `Oracle` и другие.

**commit: `Урок 8: немного об SQL`**

### Основные возможности pgAdmin: Управление базой данных и визуализация
pgAdmin — это мощный инструмент для управления базами данных `PostgreSQL`, который предоставляет широкий спектр возможностей для администрирования и визуализации данных.

#### Основные возможности:
- **Управление базой данных**: Создание, изменение и удаление баз данных, таблиц, индексов, представлений и других объектов.
- **Визуализация данных**: Графическое представление структуры базы данных, визуализация запросов и результатов выполнения.
- **Мониторинг и управление производительностью**: Мониторинг и управление производительностью базы данных.
- **Управление пользователями и ролями**: Настройка прав доступа и управление пользователями.

#### Примеры использования:
- **Создание таблицы**: Используйте графический интерфейс для создания новых таблиц.
- **Выполнение запросов**: Используйте вкладку "Query Tool" для выполнения SQL-запросов.
- **Визуализация данных**: Построение диаграмм и отчетов на основе данных.
`pgAdmin` позволяет эффективно управлять базами данных `PostgreSQL`, обеспечивая удобный и интуитивно понятный интерфейс для выполнения различных задач.

**commit: `Урок 8: основные возможности pgAdmin: Управление базой данных и визуализация`**

### Создание таблиц: Структура и параметры таблиц
Создание таблиц в `PostgreSQL` — это процесс определения структуры данных, которые будут храниться в базе данных. Вот пошаговое руководство по созданию таблиц:

#### Шаги создания таблицы:
1. **Откройте pgAdmin и подключитесь к серверу**.
2. **Выберите базу данных**.
3. **Создайте новую таблицу**:
   - Щелкните правой кнопкой мыши на базе данных и выберите "Create" -> "Table".
   - Введите имя таблицы и выберите схему (по умолчанию `public`).
4. **Определите столбцы**:
   - В разделе "Columns" добавьте столбцы, указав их имена, типы данных и ограничения (например, `NOT NULL`, `UNIQUE`).
5. **Сохраните таблицу**:
   - Нажмите "Save" для создания таблицы.
   - 
#### Параметры таблиц:
- **Типы данных**: Определяют, какие данные могут храниться в столбцах (например, `INTEGER`, `VARCHAR`, `DATE`).
- **Ограничения**: Ограничения, такие как `NOT NULL`, `UNIQUE`, `CHECK`, которые обеспечивают целостность данных.
- **Индексы**: Структуры, которые ускоряют поиск данных.
- **Внешние ключи**: Ссылки на первичные ключи в других таблицах, которые устанавливают связи между таблицами.

#### Пример создания таблицы:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

**commit: `Урок 8: cоздание таблиц: Структура и параметры таблиц`**

### Типы данных: Основные типы данных `PostgreSQL`
`PostgreSQL` поддерживает широкий спектр типов данных, которые могут быть использованы для хранения различных видов информации. Вот список основных типов данных и их применения:

#### Числовые типы:
- **INTEGER**: Целое число. Используется для хранения целых чисел, таких как идентификаторы, количества и т.д.
- **BIGINT**: Большое целое число. Используется для хранения очень больших целых чисел.
- **SMALLINT**: Малое целое число. Используется для хранения небольших целых чисел.
- **NUMERIC (или DECIMAL)**: Число с фиксированной точностью. Используется для хранения денежных сумм, процентов и других точных чисел.
- **REAL**: Число с плавающей точкой одинарной точности. Используется для хранения чисел с плавающей точкой, где точность не критична.
- **DOUBLE PRECISION**: Число с плавающей точкой двойной точности. Используется для хранения чисел с плавающей точкой, где требуется высокая точность.
- **SERIAL**: Автоинкрементное целое число. Используется для создания уникальных идентификаторов.

#### Строковые типы:
- **CHAR(n)**: Фиксированная длина строки. Используется для хранения строк фиксированной длины.
- **VARCHAR(n)**: Переменная длина строки. Используется для хранения строк переменной длины.
- **TEXT**: Строка переменной длины без ограничения. Используется для хранения больших объемов текста.

#### Дата и время:
- **DATE**: Дата. Используется для хранения дат без времени.
- **TIME**: Время. Используется для хранения времени без даты.
- **TIMESTAMP**: Дата и время. Используется для хранения даты и времени.
- **TIMESTAMPTZ**: Дата и время с часовым поясом. Используется для хранения даты и времени с учетом часового пояса.
- **INTERVAL**: Интервал времени. Используется для хранения промежутков времени.

#### Логические типы:
- **BOOLEAN**: Логическое значение. Используется для хранения значений `TRUE` или `FALSE`.

#### Двоичные типы:
- **BYTEA**: Двоичные данные. Используется для хранения двоичных данных, таких как изображения, файлы и т.д.

#### Специальные типы:
- **UUID**: Универсальный уникальный идентификатор. Используется для хранения уникальных идентификаторов.
- **JSON**: JSON данные. Используется для хранения данных в формате JSON.
- **JSONB**: Двоичный JSON. Используется для хранения данных в формате JSON с более эффективным хранением и поиском.
- **ARRAY**: Массив. Используется для хранения массивов данных.
- **ENUM**: Перечисление. Используется для хранения значений из заранее определенного набора.

**commit: `Урок 8: типы данных: Основные типы данных PostgreSQL`**

### Проектирование моделей баз данных: Оптимизация структуры базы данных для типичных задач
Проектирование базы данных — это процесс создания структуры базы данных, которая эффективно хранит, извлекает и управляет данными. Основные шаги проектирования базы данных включают:

#### Этапы проектирования базы данных:
1. **Сбор требований**: Определение, какие данные нужно хранить и как они будут использоваться.
2. **Концептуальное проектирование**: Создание ER-диаграмм (Entity-Relationship) для визуализации сущностей и их связей.
3. **Логическое проектирование**: Определение таблиц, столбцов, типов данных и ограничений.
4. **Физическое проектирование**: Оптимизация структуры базы данных для конкретной СУБД, включая индексы, партиционирование и т.д.
5. **Реализация**: Создание базы данных и таблиц в СУБД.

#### Нормальные формы:
Нормальные формы помогают организовать данные в базе данных таким образом, чтобы избежать избыточности и обеспечить целостность данных.
1. **Первая нормальная форма (1NF)**:
   - Каждая таблица должна иметь уникальный первичный ключ.
   - Каждый столбец должен содержать атомарные значения (не должно быть массивов или списков в одном столбце).
2. **Вторая нормальная форма (2NF)**:
   - Таблица должна быть в 1NF.
   - Все неключевые атрибуты должны полностью зависеть от первичного ключа.
3. **Третья нормальная форма (3NF)**:
   - Таблица должна быть в 2NF.
   - Все атрибуты должны зависеть только от первичного ключа (не должно быть транзитивных зависимостей).
  
#### Индексы:
Индексы — это специальные структуры данных, которые ускоряют поиск и сортировку данных в базе данных. Они работают аналогично указателю в книге, который позволяет быстро найти нужную страницу без необходимости просматривать всю книгу.
- **Аналогия**: Представьте себе библиотеку с тысячами книг. Без каталога (индекса) вам придется просматривать каждую книгу, чтобы найти нужную. Каталог (индекс) позволяет быстро найти нужную книгу по автору, названию или теме.
- **Для чего нужны**:
  - **Ускорение поиска**: Индексы значительно ускоряют выполнение запросов, особенно в больших таблицах.
  - **Оптимизация сортировки**: Индексы помогают быстро сортировать данные по определенным столбцам.
  - **Уникальность данных**: Индексы могут обеспечивать уникальность значений в столбцах, что помогает избежать дублирования данных.
 
#### Пример создания базы данных:
```sql
-- Создание таблицы Category
CREATE TABLE category (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор категории
    name VARCHAR(255) UNIQUE NOT NULL -- Уникальное имя категории
);
-- Создание таблицы Tag
CREATE TABLE tag (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор тега
    name VARCHAR(255) UNIQUE NOT NULL -- Уникальное имя тега
);
-- Создание таблицы Article
CREATE TABLE article (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор статьи
    title VARCHAR(255) NOT NULL, -- Заголовок статьи
    content TEXT NOT NULL, -- Содержание статьи
    publication_date TIMESTAMPTZ DEFAULT NOW(), -- Дата публикации статьи
    views INTEGER DEFAULT 0, -- Количество просмотров статьи
    category_id INTEGER NOT NULL DEFAULT 1, -- Идентификатор категории статьи
    slug VARCHAR(255) UNIQUE, -- Уникальный slug статьи
    is_active BOOLEAN DEFAULT TRUE, -- Статус активности статьи
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE -- Внешний ключ на таблицу Category
);
-- Создание таблицы для связи Article и Tag
CREATE TABLE article_tag (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор связи
    article_id INTEGER NOT NULL, -- Идентификатор статьи
    tag_id INTEGER NOT NULL, -- Идентификатор тега
    FOREIGN KEY (article_id) REFERENCES article(id) ON DELETE CASCADE, -- Внешний ключ на таблицу Article
    FOREIGN KEY (tag_id) REFERENCES tag(id) ON DELETE CASCADE -- Внешний ключ на таблицу Tag
);
-- Создание индексов для ускорения поиска
CREATE INDEX idx_article_title ON article (title); -- Индекс для поиска по заголовку статьи
CREATE INDEX idx_article_slug ON article (slug); -- Индекс для поиска по slug статьи
-- Создание триггера для автоматического заполнения slug
CREATE OR REPLACE FUNCTION update_slug() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.slug IS NULL THEN
        NEW.slug := slugify(NEW.title); -- Функция slugify должна быть определена заранее
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER trigger_update_slug
BEFORE INSERT OR UPDATE ON article
FOR EACH ROW
EXECUTE FUNCTION update_slug();
```

**commit: `Урок 8: проектирование моделей баз данных: Оптимизация структуры базы данных для типичных задач`**


## Урок 9

#### Установили IPython, чтобы прекратить страдания:
```shell
pip install ipython
```

**commit: `Урок 9: установка ipython`**

### Если у вас установлен `pgAdmin` и вы хотите перенести базу данных из `SQLite` в `PostgreSQL`, выполните следующие шаги:

#### Шаг 1: Установите необходимые библиотеки
1. **Установите библиотеку `psycopg2` для Django**:
   ```sh
   pip install psycopg2-binary
   ```

#### Шаг 2: Настройте `PostgreSQL` через `pgAdmin`
1. **Откройте `pgAdmin` и подключитесь к вашему серверу `PostgreSQL`**.
2. **Создайте новую базу данных**:
   - В `pgAdmin`, щелкните правой кнопкой мыши на "Databases" и выберите "Create" > "Database".
   - Введите имя базы данных (например, `itg`) и выберите владельца (например, `postgres`).
   - Нажмите "Save".
   - 
#### Шаг 3: Экспортируйте данные из `SQLite`
1. **Создайте дамп данных из `SQLite`**:
```sh
python manage.py dumpdata --format=json --indent=4 > db.json
```

#### Шаг 4: Настройте `Django` для использования `PostgreSQL`
1. **Обновите `settings.py`**:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'itg_141024',
           'USER': 'postgres',
           'PASSWORD': 'admin',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

#### Шаг 5: Примените миграции в `PostgreSQL`
1. **Создайте миграции (если их нет)**:
   ```sh
   python manage.py makemigrations
   ```
2. **Примените миграции**:
   ```sh
   python manage.py migrate
   ```

#### Шаг 6: Импортируйте данные в PostgreSQL
1. **Загрузите данные из JSON файла**:
```sh
python manage.py loaddata db.json
```
или из articles_4.json
```sh
python manage.py loaddata articles_4.json
```

#### Шаг 7: Проверьте данные
1. **Запустите сервер разработки и убедитесь, что все работает**:
```sh
python manage.py runserver
```

#### Шаг 8: Очистите старую базу данных SQLite (опционально)
1. **Удалите файл SQLite базы данных**:
```sh
del db.sqlite3
```

#### Примечания
- **Проверка данных**: Убедитесь, что все данные успешно перенесены и что приложение работает корректно с новой базой данных `PostgreSQL`.
- **Обработка ошибок**: Если возникнут ошибки при импорте данных, проверьте логи и исправьте проблемы в данных или в моделях `Django`.

**commit: `Урок 9: перенесли данные из SQLite в PostgreSQL`**

### Синтаксические конструкции для CRUD-запросов: Основы написания команд `INSERT`, `SELECT`, `UPDATE`, `DELETE`
`CRUD` (`Create`, `Read`, `Update`, `Delete`) — это основные операции, которые выполняются с базой данных.
В `SQL` эти операции соответствуют командам `INSERT`, `SELECT`, `UPDATE` и `DELETE`.
Рассмотрим синтаксис каждой из этих команд и приведем по два примера для каждой операции.

#### 1. Команда `INSERT`
Команда `INSERT` используется для добавления новых записей в таблицу.
**Синтаксис:**
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```
**Примеры:**
1. Добавление новой категории:
   ```sql
   INSERT INTO news_category (name)
   VALUES ('Новая категория');
   ```
2. Добавление трех новых статей:
   ```sql
   INSERT INTO news_article (title, content, publication_date, views, category_id, slug, is_active)
   VALUES
   ('Новая статья 1', 'Содержание новой статьи 1', '2023-10-01T12:00:00Z', 0, 1, 'novaya-statya-1', TRUE),
   ('Новая статья 2', 'Содержание новой статьи 2', '2023-10-02T12:00:00Z', 0, 2, 'novaya-statya-2', TRUE),
   ('Новая статья 3', 'Содержание новой статьи 3', '2023-10-03T12:00:00Z', 0, 3, 'novaya-statya-3', TRUE);
   ```
   
#### 2. Команда `SELECT`
Команда `SELECT` используется для выборки данных из таблицы.
**Синтаксис:**
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```
**Примеры:**
1. Выборка всех статей из категории "Технологии":
   ```sql
   SELECT *
   FROM news_article
   WHERE category_id = (SELECT id FROM news_category WHERE name = 'Технологии');
   ```
2. Выборка всех активных статей:
   ```sql
   SELECT *
   FROM news_article
   WHERE is_active = TRUE;
   ```
   
#### 3. Команда UPDATE
Команда `UPDATE` используется для обновления существующих записей в таблице.
**Синтаксис:**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
**Примеры:**
1. Обновление заголовка статьи с `id` 2:
   ```sql
   UPDATE news_article
   SET title = 'Обновленный заголовок'
   WHERE id = 2;
   ```
2. Увеличение количества просмотров статьи с `id` 1 на 50:
   ```sql
   UPDATE news_article
   SET views = views + 50
   WHERE id = 1;
   ```
   
#### 4. Команда DELETE
Команда `DELETE` используется для удаления записей из таблицы.
**Синтаксис:**
```sql
DELETE FROM table_name
WHERE condition;
```

**Примеры:**
1. Удаление статьи с `id` 3:
   - Удаление связанных записей в таблице `news_article_tags`:
     ```sql
     DELETE FROM news_article_tags
     WHERE article_id = 3;
     ```
   - Удаление статьи из таблицы `news_article`:
     ```sql
     DELETE FROM news_article
     WHERE id = 3;
     ```
2. Удаление всех неактивных статей:
   - Удаление связанных записей в таблице `news_article_tags` для всех неактивных статей:
     ```sql
     DELETE FROM news_article_tags
     WHERE article_id IN (SELECT id FROM news_article WHERE is_active = FALSE);
     ```
   - Удаление всех неактивных статей из таблицы `news_article`:
     ```sql
     DELETE FROM news_article
     WHERE is_active = FALSE;
     ```

**commit: `Урок 9: посмотрели операции CRUD для SQL`**

### Синтаксические конструкции для CRUD-запросов: Основы написания команд INSERT, SELECT, UPDATE, DELETE с использованием Django ORM
`CRUD` (`Create`, `Read`, `Update`, `Delete`) — это основные операции, которые выполняются с базой данных. В `Django ORM` эти операции соответствуют методам `create()`, `filter()`, `update()` и `delete()`. Рассмотрим синтаксис каждого из этих методов и приведем по два примера для каждой операции.

#### 1. Метод `create()`
Метод `create()` используется для добавления новых записей в таблицу.
**Синтаксис:**
```python
Model.objects.create(field1=value1, field2=value2, ...)
```

**Примеры:**
1. Добавление новой категории:
   ```python
   from news.models import Category
   new_category = Category.objects.create(name='Новая категория')
   ```

2. Добавление трех новых статей:
   ```python
   from news.models import Article, Category
   category1 = Category.objects.get(name='Технологии')
   category2 = Category.objects.get(name='Наука')
   category3 = Category.objects.get(name='Спорт')
   Article.objects.create(
       title='Новая статья 1',
       content='Содержание новой статьи 1',
       publication_date='2023-10-01T12:00:00Z',
       views=0,
       category=category1,
       slug='novaya-statya-1',
       is_active=True
   )
   Article.objects.create(
       title='Новая статья 2',
       content='Содержание новой статьи 2',
       publication_date='2023-10-02T12:00:00Z',
       views=0,
       category=category2,
       slug='novaya-statya-2',
       is_active=True
   )
   Article.objects.create(
       title='Новая статья 3',
       content='Содержание новой статьи 3',
       publication_date='2023-10-03T12:00:00Z',
       views=0,
       category=category3,
       slug='novaya-statya-3',
       is_active=True
   )
   ```
   
#### 2. Метод `filter()`
Метод `filter()` используется для выборки данных из таблицы.
**Синтаксис:**
```python
Model.objects.filter(field1=value1, field2=value2, ...)
```
**Примеры:**
1. Выборка всех статей из категории "Технологии":
   ```python
   from news.models import Article, Category
   category = Category.objects.get(name='Технологии')
   articles = Article.objects.filter(category=category)
   ```
2. Выборка всех активных статей:
   ```python
   from news.models import Article
   active_articles = Article.objects.filter(is_active=True)
   ```
   
#### 3. Метод `update()`
Метод `update()` используется для обновления существующих записей в таблице.
**Синтаксис:**
```python
Model.objects.filter(condition).update(field1=value1, field2=value2, ...)
```
**Примеры:**
1. Обновление заголовка статьи с `id` 4:
   ```python
   from news.models import Article
   Article.objects.filter(id=4).update(title='Обновленный заголовок')
   ```
2. Увеличение количества просмотров статьи с `id` 5 на 50:
   ```python
   from news.models import Article
   from django.db.models import F
   Article.objects.filter(id=5).update(views=F('views') + 50)
   ```
   
#### 4. Метод `delete()`
Метод `delete()` используется для удаления записей из таблицы.
**Синтаксис:**
```python
Model.objects.filter(condition).delete()
```
**Примеры:**
1. Удаление статьи с `id` 6:
   - Удаление связанных записей в таблице `news_article_tags`:
     ```python
     from news.models import Article, Tag
     article = Article.objects.get(id=6)
     article.tags.clear()  # Удаление всех связанных тегов
     article.delete()  # Удаление статьи
     ```
2. Удаление всех неактивных статей:
   - Удаление связанных записей в таблице `news_article_tags` для всех неактивных статей:
     ```python
     from news.models import Article
     inactive_articles = Article.objects.filter(is_active=False)
     for article in inactive_articles:
         article.tags.clear()  # Удаление всех связанных тегов
     inactive_articles.delete()  # Удаление всех неактивных статей
     ```
     
**commit: `Урок 9: те же запросы, но в Django ORM`**

### Запросы на языке SQL

#### 1. Создание новой категории
**Пример:**
Создайте новую категорию с именем "Путешествия".
```sql
INSERT INTO news_category (name) VALUES ('Путешествия');
```

#### 2. Создание новой статьи
**Пример:**
Создайте новую статью с заголовком "Путешествие в Исландию", содержанием "Исландия — удивительная страна с вулканами и гейзерами.", датой публикации "2023-10-15T12:00:00Z", количеством просмотров 100, категорией "Путешествия" и активным статусом.
```sql
INSERT INTO news_article (title, content, publication_date, views, category_id, slug, is_active)
VALUES (
    'Путешествие в Исландию',
    'Исландия — удивительная страна с вулканами и гейзерами.',
    '2023-10-15T12:00:00Z',
    100,
    (SELECT id FROM news_category WHERE name = 'Путешествия'),
    'puteshestvie-v-islandiyu',
    TRUE
);
```

#### 3. Выборка всех статей из категории "Технологии"
**Пример:**
Выберите все статьи из категории "Технологии".
```sql
SELECT * FROM news_article
WHERE category_id = (SELECT id FROM news_category WHERE name = 'Технологии');
```

#### 4. Выборка всех активных статей
```sql
SELECT * FROM news_article WHERE is_active = TRUE;
```

#### 5. Обновление заголовка статьи
**Пример:**
Обновите заголовок статьи с `id` 1 на "Новый заголовок".
```sql
UPDATE news_article SET title = 'Новый заголовок' WHERE id = 1;
```

#### 6. Увеличение количества просмотров статьи
**Пример:**
Увеличьте количество просмотров статьи с `id` 2 на 50.
```sql
UPDATE news_article SET views = views + 50 WHERE id = 2;
```

#### 7. Удаление статьи
**Пример:**
Удалите статью с `id` 73.
```sql
DELETE FROM news_article_tags WHERE article_id = 73;
DELETE FROM news_article WHERE id = 73;
```

#### 8. Создание нового тега
**Пример:**
Создайте новый тег с именем "Путешествия".
```sql
INSERT INTO news_tag (name) VALUES ('Путешествия');
```

#### 9. Добавление тега к статье
**Пример:**
Добавьте тег "Путешествия" к статье с `id` 21.
```sql
INSERT INTO news_article_tags (article_id, tag_id)
VALUES (21, (SELECT id FROM news_tag WHERE name = 'Путешествия'));
```

#### 10. Выборка всех статей с определенным тегом
**Пример:**
Выберите все статьи, которые имеют тег "Путешествия".
```sql
SELECT * FROM news_article
WHERE id IN (
    SELECT article_id FROM news_article_tags
    WHERE tag_id = (SELECT id FROM news_tag WHERE name = 'Путешествия')
);
```

#### 11. Удаление тега из статьи
**Пример:**
Удалите тег "Путешествия" из статьи с `id` 21.
```sql
DELETE FROM news_article_tags
WHERE article_id = 21 AND tag_id = (SELECT id FROM news_tag WHERE name = 'Путешествия');
```

### Запросы на языке Django ORM

#### 12. Создание новой категории
**Пример:**
Создайте новую категорию с именем "Путешествия".
```python
Category.objects.create(name='Путешествия')
```

#### 13. Создание новой статьи
**Пример:**
Создайте новую статью с заголовком "Путешествие в Исландию", содержанием "Исландия — удивительная страна с вулканами и гейзерами.", датой публикации "2023-10-15T12:00:00Z", количеством просмотров 100, категорией "Путешествия" и активным статусом.
```python
category = Category.objects.get(name='Путешествия')
Article.objects.create(
    title='Путешествие в Исландию',
    content='Исландия — удивительная страна с вулканами и гейзерами.',
    publication_date='2023-10-15T12:00:00Z',
    views=100,
    category=category,
    slug='puteshestvie-v-islandiyu',
    is_active=True
)
```

#### 14. Выборка всех статей из категории "Технологии"
**Пример:**
Выберите все статьи из категории "Технологии".
```python
category = Category.objects.get(name='Технологии')
articles = Article.objects.filter(category=category)
```

#### 15. Выборка всех активных статей
```python
active_articles = Article.objects.filter(is_active=True)
```

#### 16. Обновление заголовка статьи
**Пример:**
Обновите заголовок статьи с `id` 1 на "Новый заголовок".
```python
Article.objects.filter(id=1).update(title='Новый заголовок')
```

#### 17. Увеличение количества просмотров статьи
**Пример:**
Увеличьте количество просмотров статьи с `id` 2 на 50.
```python
Article.objects.filter(id=2).update(views=F('views') + 50)
```

#### 18. Удаление статьи
**Пример:**
Удалите статью с `id` 73.
```python
article = Article.objects.get(id=73)
article.tags.clear()  # Удаление всех связанных тегов
article.delete()  # Удаление статьи
```

#### 19. Создание нового тега
**Пример:**
Создайте новый тег с именем "Путешествия".

```python
Tag.objects.create(name='Путешествия')
```

#### 20. Добавление тега к статье
**Пример:**
Добавьте тег "Путешествия" к статье с `id` 21.
```python
article = Article.objects.get(id=21)
tag = Tag.objects.get(name='Путешествия')
article.tags.add(tag)
```

#### 21. Выборка всех статей с определенным тегом
**Пример:**
Выберите все статьи, которые имеют тег "Путешествия".
```python
tag = Tag.objects.get(name='Путешествия')
articles = Article.objects.filter(tags=tag)
```

#### 22. Удаление тега из статьи
**Пример:**
Удалите тег "Путешествия" из статьи с `id` 21.
```python
article = Article.objects.get(id=21)
tag = Tag.objects.get(name='Путешествия')
article.tags.remove(tag)
```

**commit: `Урок 9: решение практики`**


## Урок 10

### Возможности по фильтрации и сортировке
- **Понимание методов сортировки и фильтрации данных:**
  - **Фильтрация:** Выборка данных по определенным критериям. Например, выборка всех статей, опубликованных в определенной категории.
  - **Сортировка:** Упорядочивание данных по определенным критериям. Например, сортировка статей по количеству просмотров.
- **Примеры использования фильтрации и сортировки в реальных задачах:**
  - **Интернет-магазин:** Фильтрация товаров по категориям, ценам, брендам и т.д. Сортировка товаров по популярности, цене, рейтингу и т.д.
  - **Социальные сети:** Фильтрация постов по хештегам, пользователям, дате публикации. Сортировка постов по количеству лайков, комментариев, дате публикации и т.д.
  - **Аналитика:** Фильтрация данных по определенным критериям для создания отчетов. Сортировка данных для анализа трендов и выявления закономерностей.

### Синтаксические конструкции для фильтрации и сортировки
- **Команды WHERE (OR, AND, IN, NOT):**
  - **WHERE:** Основная команда для фильтрации данных.
  - **OR:** Оператор для объединения нескольких условий, где достаточно выполнения хотя бы одного из них.
  - **AND:** Оператор для объединения нескольких условий, где должны выполняться все условия одновременно.
  - **IN:** Оператор для проверки наличия значения в списке значений.
  - **NOT:** Оператор для инверсии условия.
- **ORDER BY:** Команда для сортировки данных по одному или нескольким столбцам.
- **WITH:** Команда для создания временных таблиц или представлений.
- **Условия и операторы сравнения:** Основные операторы сравнения (=, <>, <, >, <=, >=) и логические операторы (AND, OR, NOT).
- 
**commit: `Урок 10: синтаксические конструкции для фильтрации и сортировки`**

### Написание запросов для фильтрации и сортировки
- **Шаблон для SQL-запросов:**
  - **Шаблон для фильтрации:**
    ```sql
    SELECT column1, column2, ...
    FROM table_name
    WHERE condition;
    ```
  - **Шаблон для сортировки:**
    ```sql
    SELECT column1, column2, ...
    FROM table_name
    ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
    ```
  - **Шаблон для фильтрации и сортировки:**
    ```sql
    SELECT column1, column2, ...
    FROM table_name
    WHERE condition
    ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
    ```

- **Шаблон для Django ORM:**
  - **Шаблон для фильтрации:**
    ```python
    Model.objects.filter(condition)
    ```
  - **Шаблон для сортировки:**
    ```python
    Model.objects.order_by('field1', 'field2', ...)
    ```
  - **Шаблон для фильтрации и сортировки:**
    ```python
    Model.objects.filter(condition).order_by('field1', 'field2', ...)
    ```

**commit: `Урок 10: написание запросов для фильтрации и сортировки`**

### Решения задач на SQL

1. **Выбрать все статьи из категории "Технологии" и получить их заголовки и количество просмотров.**
   ```sql
   SELECT title, views FROM news_article WHERE category_id = 1;
   ```

2. **Выбрать все статьи, у которых количество просмотров больше 200, и получить их заголовки и даты публикации.**
   ```sql
   SELECT title, publication_date FROM news_article WHERE views > 200;
   ```

3. **Выбрать все статьи, у которых количество просмотров больше 100 и меньше 300, и получить их заголовки и количество просмотров.**
   ```sql
   SELECT title, views FROM news_article WHERE views > 100 AND views < 300;
   ```

4. **Выбрать все статьи, у которых количество просмотров больше 200, и получить их заголовки и названия категорий.**
   ```sql
   SELECT title, (SELECT name FROM news_category WHERE id = news_article.category_id) AS category_name
   FROM news_article
   WHERE views > 200;
   ```

5. **Выбрать все статьи из категории "Технологии" или "Наука" и получить их заголовки и названия категорий.**
   ```sql
   SELECT title, (SELECT name FROM news_category WHERE id = news_article.category_id) AS category_name
   FROM news_article
   WHERE category_id IN (1, 2);
   ```

6. **Выбрать все статьи, у которых количество просмотров больше 200, и отсортировать их по дате публикации в порядке убывания, получить их заголовки и даты публикации.**
   ```sql
   SELECT title, publication_date FROM news_article WHERE views > 200 ORDER BY publication_date DESC;
   ```

7. **Выбрать все статьи, у которых количество просмотров больше 200, и отсортировать их по количеству просмотров в порядке убывания, получить их заголовки и количество просмотров.**
   ```sql
   SELECT title, views FROM news_article WHERE views > 200 ORDER BY views DESC;
   ```

8. **Выбрать все статьи, у которых количество просмотров меньше 300, и отсортировать их по категории и дате публикации, получить их заголовки и даты публикации.**
   ```sql
   SELECT title, publication_date FROM news_article WHERE views < 300 ORDER BY category_id, publication_date;
   ```

9. **Выбрать все статьи, у которых количество просмотров больше или равно 200, и отсортировать их по категории в порядке возрастания и дате публикации в порядке убывания, получить их заголовки и даты публикации.**
   ```sql
   SELECT title, publication_date FROM news_article WHERE views >= 200 ORDER BY category_id ASC, publication_date DESC;
   ```

10. **Выбрать все статьи, у которых количество просмотров между 220 и 270, и отсортировать их по категории в порядке убывания и дате публикации в порядке возрастания, получить их заголовки и даты публикации.**
    ```sql
    SELECT title, publication_date FROM news_article WHERE views BETWEEN 220 AND 270 ORDER BY category_id DESC, publication_date ASC;
    ```

11. **Выбрать все статьи, у которых количество просмотров не больше 200, и отсортировать их по категории и количеству просмотров в порядке убывания, получить их заголовки и количество просмотров.**
    ```sql
    SELECT title, views FROM news_article WHERE views <= 200 ORDER BY category_id, views DESC;
    ```

12. **Выбрать все статьи, у которых количество просмотров больше 300 и меньше 200, и отсортировать их по категории в порядке возрастания и количеству просмотров в порядке убывания, получить их заголовки и количество просмотров.**
    ```sql
    SELECT title, views FROM news_article WHERE views > 300 AND views < 200 ORDER BY category_id ASC, views DESC;
    ```

### Решения задач на Django ORM

1. **Выбрать все статьи из категории "Технологии" и получить их заголовки и количество просмотров.**
   ```python
   articles = Article.objects.filter(category_id=1).values('title', 'views')
   ```

2. **Выбрать все статьи, у которых количество просмотров больше 200, и получить их заголовки и даты публикации.**
   ```python
   articles = Article.objects.filter(views__gt=200).values('title', 'publication_date')
   ```

3. **Выбрать все статьи, у которых количество просмотров больше 100 и меньше 300, и получить их заголовки и количество просмотров.**
   ```python
   articles = Article.objects.filter(views__gt=100, views__lt=300).values('title', 'views')
   ```

4. **Выбрать все статьи, у которых количество просмотров больше 200, и получить их заголовки и названия категорий.**
   ```python
   from django.db.models import OuterRef, Subquery
   articles = Article.objects.filter(views__gt=200).annotate(category_name=Subquery(Category.objects.filter(id=OuterRef('category_id')).values('name')[:1])).values('title', 'category_name')
   ```

5. **Выбрать все статьи из категории "Технологии" или "Наука" и получить их заголовки и названия категорий.**
   ```python
   from django.db.models import Q, OuterRef, Subquery
   articles = Article.objects.filter(Q(category_id=1) | Q(category_id=2)).annotate(category_name=Subquery(Category.objects.filter(id=OuterRef('category_id')).values('name')[:1])).values('title', 'category_name')
   ```

6. **Выбрать все статьи, у которых количество просмотров больше 200, и отсортировать их по дате публикации в порядке убывания, получить их заголовки и даты публикации.**
   ```python
   articles = Article.objects.filter(views__gt=200).order_by('-publication_date').values('title', 'publication_date')
   ```

7. **Выбрать все статьи, у которых количество просмотров больше 200, и отсортировать их по количеству просмотров в порядке убывания, получить их заголовки и количество просмотров.**
   ```python
   articles = Article.objects.filter(views__gt=200).order_by('-views').values('title', 'views')
   ```

8. **Выбрать все статьи, у которых количество просмотров меньше 300, и отсортировать их по категории и дате публикации, получить их заголовки и даты публикации.**
   ```python
   articles = Article.objects.filter(views__lt=300).order_by('category_id', 'publication_date').values('title', 'publication_date')
   ```

9. **Выбрать все статьи, у которых количество просмотров больше или равно 200, и отсортировать их по категории в порядке возрастания и дате публикации в порядке убывания, получить их заголовки и даты публикации.**
   ```python
   articles = Article.objects.filter(views__gte=200).order_by('category_id', '-publication_date').values('title', 'publication_date')
   ```

10. **Выбрать все статьи, у которых количество просмотров между 220 и 270, и отсортировать их по категории в порядке убывания и дате публикации в порядке возрастания, получить их заголовки и даты публикации.**
    ```python
    articles = Article.objects.filter(views__range=(220, 270)).order_by('-category_id', 'publication_date').values('title', 'publication_date')
    ```

11. **Выбрать все статьи, у которых количество просмотров не больше 200, и отсортировать их по категории и количеству просмотров в порядке убывания, получить их заголовки и количество просмотров.**
    ```python
    articles = Article.objects.filter(views__lte=200).order_by('category_id', '-views').values('title', 'views')
    ```

12. **Выбрать все статьи, у которых количество просмотров больше 300 и меньше 200, и отсортировать их по категории в порядке возрастания и количеству просмотров в порядке убывания, получить их заголовки и количество просмотров.**
    ```python
    articles = Article.objects.filter(views__gt=300, views__lt=200).order_by('category_id', '-views').values('title', 'views')
    ```

**commit: `Урок 10: решение практики`**


## Урок 11

### Небольшие правки в проект

Ошибка `ManyRelatedManager object is not iterable` возникает потому, что вы пытаетесь итерировать по `ManyRelatedManager` напрямую,
вместо того чтобы использовать метод `.all()` для получения всех связанных объектов.
Чтобы исправить эту ошибку, вам нужно использовать `article.tags.all()` для получения всех тегов, связанных с конкретной статьей.

**commit: `Урок 11: исправили шаблоны карточек для отображения тегов новостей`**

### Улучшение внешнего вида и пользовательского интерфейса приложения

1. **Обновление базового шаблона (base.html):**
   - **Изменения:**
     - Добавлены стили для фона и текста:
       ```html
       <style>
           body {
               background-color: #f8f9fa;
               color: #343a40;
           }
           .navbar {
               background-color: #343a40;
           }
           .navbar-nav .nav-link {
               color: #ffffff;
           }
           .navbar-nav .nav-link\:hover {
               color: #ffc107;
           }
           .card {
               margin-bottom: 20px;
           }
           .footer {
               background-color: #343a40;
               color: #ffffff;
               text-align: center;
               padding: 10px 0;
           }
       </style>
       ```
     - Обновлены структура и стили навигационного меню:
       ```html
       <nav class="navbar navbar-expand-lg navbar-dark">
           <div class="container-fluid">
               <a class="navbar-brand" href="#">Info to Go</a>
               <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                   <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarNav">
                   <ul class="navbar-nav ms-auto">
                       {% include "include/nav_menu.html" %}
                   </ul>
               </div>
           </div>
       </nav>
       ```
   - **Причина:**
     - Улучшение общего внешнего вида приложения и повышение удобства использования.

2. **Обновление шаблона about.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для центрирования текста и улучшения отступов:
       ```html
       <h1 class="text-center mb-4">О сайте</h1>
       <p class="text-center">Добро пожаловать на наш сайт!</p>
       <p class="text-center">На нашем сайте, новостей {{ news_count }}, пользователей {{ users_count }}.</p>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида страницы "О сайте".

3. **Обновление шаблона main.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для центрирования текста и улучшения отступов:
       ```html
       <h1 class="text-center mb-4">Главная страница</h1>
       <p class="text-center">Добро пожаловать на сайт!</p>
       <p class="text-center">На нашем сайте, новостей {{ news_count }}, пользователей {{ users_count }}.</p>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида главной страницы.

4. **Обновление шаблона catalog.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для центрирования текста и улучшения отступов:
       ```html
       <h1 class="text-center mb-4">Каталог новостей Info to Go</h1>
       <p class="text-center">Всего новостей: {{ news_count }}</p>
       <p class="text-center">Всего пользователей: {{ users_count }}</p>
       ```
     - Добавлены классы Bootstrap для создания сетки из двух колонок для карточек новостей:
       ```html
       <div class="row">
           {% for article in news %}
               <div class="col-md-6 mb-4">
                   {% include "include/article_preview.html" with article=article %}
               </div>
           {% endfor %}
       </div>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида страницы каталога новостей, а также улучшение отображения карточек новостей.

5. **Обновление шаблона article_detail.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для улучшения внешнего вида карточки новости:
       ```html
       <div class="card">
           <div class="card-body">
               <h5 class="card-title">{% upper_words article.title %}</h5>
               <p class="card-text">{{ article.content }}</p>
               <p class="card-text">{{ article.category }}</p>
               {% for tag in article.tags.all %}
                   <span class="badge bg-info">{{ tag }}</span>
               {% endfor %}
               <p class="card-text">{{ article.id_author }}</p>
               <p class="card-text">{{ article.id }}</p>
               <p class="card-text">{{ article.publication_date }}</p>
               <p class="card-text">{{ article.views }}</p>
               <p class="card-text">{{ article.favorites_count }}</p>
           </div>
       </div>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида страницы детального представления новости.

6. **Обновление шаблона article_preview.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для улучшения внешнего вида карточки новости:
       ```html
       <div class="card">
           <div class="card-body">
               <h5 class="card-title">{{ article.title }}</h5>
               <p class="card-text">{{ article.content|truncatechars:50 }}</p>
               <p class="card-text">{{ article.category }}</p>
               {% for tag in article.tags.all %}
                   <span class="badge bg-info">{{ tag }}</span>
               {% endfor %}
               <p class="card-text">{{ article.id_author }}</p>
               <p class="card-text">{{ article.id }}</p>
               <p class="card-text">{{ article.publication_date }}</p>
               <p class="card-text">{{ article.views }}</p>
               <p class="card-text">{{ article.favorites_count }}</p>
               <a href="{% url 'detail_article_by_id' article.id %}" class="btn btn-primary">Подробнее</a>
           </div>
       </div>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида краткого представления новости.

7. **Обновление шаблона nav_menu.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для улучшения внешнего вида навигационного меню:
       ```html
       <ul class="navbar-nav">
           {% for item in menu %}
               <li class="nav-item">
                   <a class="nav-link" href="{% url item.url_name %}">{{ item.title }}</a>
               </li>
               {% if not forloop.last %}
                   <li class="nav-item"><hr class="dropdown-divider"/></li>
               {% endif %}
           {% endfor %}
       </ul>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида навигационного меню.

**commit: `Урок 11: исправили вёрстку, добавили адаптивности, поправили отступы`**

исправление маршрута `catalog/` для получения каталога новостей

**commit: `Урок 11: исправили маршрут для получения каталога`**

### добавление сортировки на страницу каталога

```python
# Считаем параметры из GET-запроса
sort = request.GET.get('sort', 'publication_date')  # по умолчанию сортируем по дате загрузки
order = request.GET.get('order', 'desc')  # по умолчанию сортируем по убыванию
# Проверяем, дали ли мы разрешение на сортировку по этому полю
valid_sort_fields = {'publication_date', 'views'}
if sort not in valid_sort_fields:
    sort = 'publication_date'
# Обрабатываем направление сортировки
if order == 'asc':
    order_by = sort
else:
    order_by = f'-{sort}'
```

1. **Считывание параметров из GET-запроса:**
   ```python
   sort = request.GET.get('sort', 'publication_date')  # по умолчанию сортируем по дате загрузки
   order = request.GET.get('order', 'desc')  # по умолчанию сортируем по убыванию
   ```
   - **Описание:**
     - Мы используем метод `request.GET.get()` для получения параметров `sort` и `order` из GET-запроса.
     - Если параметр `sort` не указан, по умолчанию используется `'publication_date'`.
     - Если параметр `order` не указан, по умолчанию используется `'desc'` (по убыванию).

2. **Проверка разрешенных полей для сортировки:**
   ```python
   valid_sort_fields = {'publication_date', 'views'}
   if sort not in valid_sort_fields:
       sort = 'publication_date'
   ```
   - **Описание:**
     - Мы определяем множество `valid_sort_fields`, которое содержит разрешенные поля для сортировки: `'publication_date'` и `'views'`.
     - Если значение `sort` не входит в множество `valid_sort_fields`, мы устанавливаем `sort` в `'publication_date'` по умолчанию.

3. **Обработка направления сортировки:**
   ```python
   if order == 'asc':
       order_by = sort
   else:
       order_by = f'-{sort}'
   ```
   - **Описание:**
     - Мы проверяем значение параметра `order`.
     - Если `order` равен `'asc'` (по возрастанию), мы устанавливаем `order_by` в `sort`.
     - В противном случае (по убыванию), мы устанавливаем `order_by` в `f'-{sort}'`, добавляя символ `-` перед полем сортировки, чтобы указать порядок по убыванию.

### Причина изменений:
- **Улучшение гибкости сортировки:**
  - Пользователи могут указывать параметры сортировки через GET-запрос, что делает интерфейс более гибким и удобным.
- **Безопасность и валидация:**
  - Проверка разрешенных полей для сортировки предотвращает использование недопустимых полей, что повышает безопасность и надежность приложения.
- **Улучшение пользовательского опыта:**
  - По умолчанию сортировка выполняется по дате загрузки и по убыванию, что соответствует ожиданиям большинства пользователей.

### Пример использования:
- **URL-запрос:**
  - `/news/?sort=views&order=asc` будет сортировать новости по количеству просмотров по возрастанию.
  - `/news/?sort=publication_date&order=desc` будет сортировать новости по дате загрузки по убыванию.

**commit: `Урок 11: добавили сортировку по датам или по просмотрам`**

### Подготовка базы данных для экспериментов с джоинами
**Изменение поля `category_id` в таблице `news_article`. Теперь поле может быть пустым:**
```sql
ALTER TABLE news_article ALTER COLUMN category_id DROP NOT NULL;
```

**Добавление двух новых категорий:**
```sql
INSERT INTO news_category (name) VALUES ('Погода');
INSERT INTO news_category (name) VALUES ('СРОЧНО');
```

**Очистка категории у некоторых статей**
Этот запрос обновляет таблицу `news_article`, устанавливая значение `category_id` в `NULL` для всех статей,
содержание которых не содержит слов 'городе' и 'довольны'.
Оператор `NOT LIKE` используется для проверки, что строка не содержит указанного шаблона.
```sql
UPDATE news_article
SET category_id = NULL
WHERE content NOT LIKE '%городе%'
  AND content NOT LIKE '%довольны%';
```

**commit: `Урок 11: изменили записи в БД чтобы посмотреть на работу джоинов`**


## Урок 12

### HAVING в SQL
`HAVING` в SQL используется для фильтрации групп на основе условий, применяемых к агрегационным функциям. `HAVING` работает аналогично `WHERE`, но применяется к группам, а не к отдельным строкам. Это позволяет фильтровать результаты после группировки и агрегации.
### Примеры использования HAVING

#### PostgreSQL
1. **Подсчет количества статей в каждой категории, где количество статей больше 5:**
```sql
SELECT category_id, COUNT(*)
FROM news_article
GROUP BY category_id
HAVING COUNT(*) > 5;
```
2. **Сумма просмотров статей в каждой категории, где сумма просмотров больше 1000:**
```sql
SELECT category_id, SUM(views)
FROM news_article
GROUP BY category_id
HAVING SUM(views) > 1000;
```
3. **Среднее количество просмотров статей в каждой категории, где среднее количество просмотров больше 200:**
```sql
SELECT category_id, AVG(views)
FROM news_article
GROUP BY category_id
HAVING AVG(views) > 200;
```
4. **Максимальное количество просмотров статьи в каждой категории, где максимальное количество просмотров больше 300:**
```sql
SELECT category_id, MAX(views)
FROM news_article
GROUP BY category_id
HAVING MAX(views) > 300;
```
5. **Минимальное количество просмотров статьи в каждой категории, где минимальное количество просмотров больше 100:**
```sql
SELECT category_id, MIN(views)
FROM news_article
GROUP BY category_id
HAVING MIN(views) > 100;
```

#### Django ORM
В Django ORM нет прямого эквивалента `HAVING`, но можно использовать `annotate` и `filter` для достижения аналогичного результата.
1. **Подсчет количества статей в каждой категории, где количество статей больше 5:**
```python
from django.db.models import Count
results = Article.objects.values('category').annotate(count=Count('id')).filter(count__gt=5)
for result in results:
    print(f"Category: {result['category']}, Count: {result['count']}")
```
2. **Сумма просмотров статей в каждой категории, где сумма просмотров больше 1000:**
```python
from django.db.models import Sum
results = Article.objects.values('category').annotate(total_views=Sum('views')).filter(total_views__gt=1000)
for result in results:
    print(f"Category: {result['category']}, Total Views: {result['total_views']}")
```
3. **Среднее количество просмотров статей в каждой категории, где среднее количество просмотров больше 200:**
```python
from django.db.models import Avg
results = Article.objects.values('category').annotate(avg_views=Avg('views')).filter(avg_views__gt=200)
for result in results:
    print(f"Category: {result['category']}, Average Views: {result['avg_views']}")
```
4. **Максимальное количество просмотров статьи в каждой категории, где максимальное количество просмотров больше 300:**
```python
from django.db.models import Max
results = Article.objects.values('category').annotate(max_views=Max('views')).filter(max_views__gt=300)
for result in results:
    print(f"Category: {result['category']}, Max Views: {result['max_views']}")
```
5. **Минимальное количество просмотров статьи в каждой категории, где минимальное количество просмотров больше 100:**
```python
from django.db.models import Min
results = Article.objects.values('category').annotate(min_views=Min('views')).filter(min_views__gt=100)
for result in results:
    print(f"Category: {result['category']}, Min Views: {result['min_views']}")
```

**commit: `Урок 12: рассмотрели работу агрегационных функций в SQL и в Django ORM`**

### решение практики

#### Задача 1: Получите список всех статей и их категорий.

**PostgreSQL:**
```sql
SELECT a.id, a.title, a.content, a.views, a.published_date, c.name AS category_name
FROM articles a
LEFT JOIN categories c ON a.category_id = c.id;
```

**Django ORM:**
```python
articles = Article.objects.select_related('category').all()
for article in articles:
    print(article.title, article.category.name if article.category else 'No category')
```

#### Задача 2: Получите список всех статей и их тегов.

**PostgreSQL:**
```sql
SELECT a.id, a.title, a.content, a.views, a.published_date, t.name AS tag_name
FROM articles a
LEFT JOIN article_tags at ON a.id = at.article_id
LEFT JOIN tags t ON at.tag_id = t.id;
```

**Django ORM:**
```python
articles = Article.objects.prefetch_related('tags').all()
for article in articles:
    print(article.title, [tag.name for tag in article.tags.all()])
```

#### Задача 3: Получите список всех статей, которые не имеют категории.

**PostgreSQL:**
```sql
SELECT *
FROM articles
WHERE category_id IS NULL;
```

**Django ORM:**
```python
articles = Article.objects.filter(category__isnull=True)
for article in articles:
    print(article.title)
```

#### Задача 4: Получите список всех статей, которые не имеют тегов.

**PostgreSQL:**
```sql
SELECT a.*
FROM articles a
LEFT JOIN article_tags at ON a.id = at.article_id
WHERE at.article_id IS NULL;
```

**Django ORM:**
```python
articles = Article.objects.filter(tags__isnull=True)
for article in articles:
    print(article.title)
```

#### Задача 5: Получите список всех категорий и связанных с ними статей.

**PostgreSQL:**
```sql
SELECT c.id, c.name, a.id AS article_id, a.title
FROM categories c
LEFT JOIN articles a ON c.id = a.category_id;
```

**Django ORM:**
```python
categories = Category.objects.prefetch_related('article_set').all()
for category in categories:
    print(category.name, [article.title for article in category.article_set.all()])
```

#### Задача 6: Получите список всех тегов и связанных с ними статей.

**PostgreSQL:**
```sql
SELECT t.id, t.name, a.id AS article_id, a.title
FROM tags t
LEFT JOIN article_tags at ON t.id = at.tag_id
LEFT JOIN articles a ON at.article_id = a.id;
```

**Django ORM:**
```python
tags = Tag.objects.prefetch_related('article_set').all()
for tag in tags:
    print(tag.name, [article.title for article in tag.article_set.all()])
```

#### Задача 7: Получите список всех статей, которые содержат слово "пауки" в заголовке или содержании.

**PostgreSQL:**
```sql
SELECT *
FROM articles
WHERE title ILIKE '%пауки%' OR content ILIKE '%пауки%';
```

**Django ORM:**
```python
articles = Article.objects.filter(models.Q(title__icontains='пауки') | models.Q(content__icontains='пауки'))
for article in articles:
    print(article.title)
```

#### Задача 8*: Получите список всех статей с их тегами (теги для каждой строки нужно свернуть в одну ячейку), которые были опубликованы в 2023 году.

**PostgreSQL:**
```sql
SELECT a.id, a.title, a.content, a.views, a.published_date, STRING_AGG(t.name, ', ') AS tags
FROM articles a
LEFT JOIN article_tags at ON a.id = at.article_id
LEFT JOIN tags t ON at.tag_id = t.id
WHERE a.published_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY a.id;
```

**Django ORM:**
```python
from django.db.models import Prefetch

articles = Article.objects.filter(published_date__year=2023).prefetch_related(
    Prefetch('tags', queryset=Tag.objects.all(), to_attr='tag_list')
)
for article in articles:
    print(article.title, ', '.join([tag.name for tag in article.tag_list]))
```

#### Задача 9: Получите список всех статей, которые имеют более 120 просмотров и были опубликованы НЕ в 2023 году.

**PostgreSQL:**
```sql
SELECT *
FROM articles
WHERE views > 120 AND published_date NOT BETWEEN '2023-01-01' AND '2023-12-31';
```

**Django ORM:**
```python
articles = Article.objects.filter(views__gt=120).exclude(published_date__year=2023)
for article in articles:
    print(article.title)
```

#### Задача 10: Получите список всех статей, которые принадлежат к категории "Наука" или "Технологии".

**PostgreSQL:**
```sql
SELECT a.*
FROM articles a
JOIN categories c ON a.category_id = c.id
WHERE c.name IN ('Наука', 'Технологии');
```

**Django ORM:**
```python
articles = Article.objects.filter(category__name__in=['Наука', 'Технологии'])
for article in articles:
    print(article.title)
```

#### Задача 11: Получите список всех статей, которые имеют тег НЕ "Здоровье" и не "Ученые" и при этом имеют меньше 200 просмотров.

**PostgreSQL:**
```sql
SELECT a.*
FROM articles a
LEFT JOIN article_tags at ON a.id = at.article_id
LEFT JOIN tags t ON at.tag_id = t.id
WHERE t.name NOT IN ('Здоровье', 'Ученые') AND a.views < 200;
```

**Django ORM:**
```python
articles = Article.objects.exclude(tags__name__in=['Здоровье', 'Ученые']).filter(views__lt=200)
for article in articles:
    print(article.title)
```

#### Задача 12: Получите список всех статей, которые не имеют категории и не содержат слова "городе" и "довольны" в содержании.

**PostgreSQL:**
```sql
SELECT *
FROM articles
WHERE category_id IS NULL AND content NOT ILIKE '%городе%' AND content NOT ILIKE '%довольны%';
```

**Django ORM:**
```python
articles = Article.objects.filter(category__isnull=True).exclude(content__icontains='городе').exclude(content__icontains='довольны')
for article in articles:
    print(article.title)
```

#### Задача 13: Вывести все статьи, опубликованные в октябре 2023 года.

**PostgreSQL:**
```sql
SELECT *
FROM articles
WHERE published_date BETWEEN '2023-10-01' AND '2023-10-31';
```

**Django ORM:**
```python
articles = Article.objects.filter(published_date__year=2023, published_date__month=10)
for article in articles:
    print(article.title)
```

#### Задача 14: Найти категории, у которых среднее количество просмотров статей больше 200.

**PostgreSQL:**
```sql
SELECT c.id, c.name, AVG(a.views) AS average_views
FROM categories c
JOIN articles a ON c.id = a.category_id
GROUP BY c.id
HAVING AVG(a.views) > 200;
```

**Django ORM:**
```python
from django.db.models import Avg

categories = Category.objects.annotate(average_views=Avg('article__views')).filter(average_views__gt=200)
for category in categories:
    print(category.name, category.average_views)
```

#### Задача 15: Получить список всех категорий и количество статей в каждой категории.

**PostgreSQL:**
```sql
SELECT c.id, c.name, COUNT(a.id) AS article_count
FROM categories c
LEFT JOIN articles a ON c.id = a.category_id
GROUP BY c.id;
```

**Django ORM:**
```python
from django.db.models import Count

categories = Category.objects.annotate(article_count=Count('article'))
for category in categories:
    print(category.name, category.article_count)
```

#### Задача 16: Найти статьи, которые принадлежат категории "Технологии" или "Наука".

**PostgreSQL:**
```sql
SELECT a.*
FROM articles a
JOIN categories c ON a.category_id = c.id
WHERE c.name IN ('Технологии', 'Наука');
```

**Django ORM:**
```python
articles = Article.objects.filter(category__name__in=['Технологии', 'Наука'])
for article in articles:
    print(article.title)
```

#### Задача 17: Найти категории, у которых максимальное количество просмотров статьи больше 300.

**PostgreSQL:**
```sql
SELECT c.id, c.name, MAX(a.views) AS max_views
FROM categories c
JOIN articles a ON c.id = a.category_id
GROUP BY c.id
HAVING MAX(a.views) > 300;
```

**Django ORM:**
```python
from django.db.models import Max

categories = Category.objects.annotate(max_views=Max('article__views')).filter(max_views__gt=300)
for category in categories:
    print(category.name, category.max_views)
```

#### Задача 18: Получить список всех тегов и количество статей, связанных с каждым тегом.

**PostgreSQL:**
```sql
SELECT t.id, t.name, COUNT(a.id) AS article_count
FROM tags t
LEFT JOIN article_tags at ON t.id = at.tag_id
LEFT JOIN articles a ON at.article_id = a.id
GROUP BY t.id;
```

**Django ORM:**
```python
from django.db.models import Count

tags = Tag.objects.annotate(article_count=Count('article'))
for tag in tags:
    print(tag.name, tag.article_count)
```

#### Задача 19: Найти статьи, которые не принадлежат ни одной категории.

**PostgreSQL:**
```sql
SELECT *
FROM articles
WHERE category_id IS NULL;
```

**Django ORM:**
```python
articles = Article.objects.filter(category__isnull=True)
for article in articles:
    print(article.title)
```

#### Задача 20: Вывести статьи, у которых заголовок содержит слово "летающие".

**PostgreSQL:**
```sql
SELECT *
FROM articles
WHERE title ILIKE '%летающие%';
```

**Django ORM:**
```python
articles = Article.objects.filter(title__icontains='летающие')
for article in articles:
    print(article.title)
```

#### Задача 21: Получить список всех статей и их категорий, отсортированных по количеству просмотров в порядке убывания.

**PostgreSQL:**
```sql
SELECT a.id, a.title, a.content, a.views, a.published_date, c.name AS category_name
FROM articles a
LEFT JOIN categories c ON a.category_id = c.id
ORDER BY a.views DESC;
```

**Django ORM:**
```python
articles = Article.objects.select_related('category').order_by('-views')
for article in articles:
    print(article.title, article.category.name if article.category else 'No category')
```

#### Задача 22: Найти теги, у которых сумма просмотров статей больше 1000.

**PostgreSQL:**
```sql
SELECT t.id, t.name, SUM(a.views) AS total_views
FROM tags t
LEFT JOIN article_tags at ON t.id = at.tag_id
LEFT JOIN articles a ON at.article_id = a.id
GROUP BY t.id
HAVING SUM(a.views) > 1000;
```

**Django ORM:**
```python
from django.db.models import Sum

tags = Tag.objects.annotate(total_views=Sum('article__views')).filter(total_views__gt=1000)
for tag in tags:
    print(tag.name, tag.total_views)
```

#### Задача 23: Получить список всех статей и их тегов, отсортированных по дате публикации.

**PostgreSQL:**
```sql
SELECT a.id, a.title, a.content, a.views, a.published_date, STRING_AGG(t.name, ', ') AS tags
FROM articles a
LEFT JOIN article_tags at ON a.id = at.article_id
LEFT JOIN tags t ON at.tag_id = t.id
GROUP BY a.id
ORDER BY a.published_date;
```

**Django ORM:**
```python
from django.db.models import Prefetch

articles = Article.objects.prefetch_related(
    Prefetch('tags', queryset=Tag.objects.all(), to_attr='tag_list')
).order_by('published_date')
for article in articles:
    print(article.title, ', '.join([tag.name for tag in article.tag_list]))
```

#### Задача 24: Найти статьи, которые принадлежат категории "Спорт" и имеют тег "Футбол".

**PostgreSQL:**
```sql
SELECT a.*
FROM articles a
JOIN categories c ON a.category_id = c.id
JOIN article_tags at ON a.id = at.article_id
JOIN tags t ON at.tag_id = t.id
WHERE c.name = 'Спорт' AND t.name = 'Футбол';
```

**Django ORM:**
```python
articles = Article.objects.filter(category__name='Спорт', tags__name='Футбол')
for article in articles:
    print(article.title)
```

**commit: `Урок 12: решили финальную практику по SQL и Django ORM`**


## Урок 13

### Создание суперпользователя

- `python manage.py createsuperuser`
- ввести имя для администратора
- ввести email для администратора
- ввести пароль
- повторить пароль
- если пароль слишком короткий, слишком общий или похож на имя пользователя, то будет предложено ввести другой пароль или согласиться предупреждениями

**commit: `Урок 13: создали суперпользователя`**

### Регистрация моделей в админ-панели

#### models.py
```python
from .models import Article, Category, Tag
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
```

**commit: `Урок 13: зарегистрировали модели в админ-панели`**

### Изменение заголовка, подзаголовка и тд в админ-панели

#### models.py
```python
admin.site.site_header = "Info to Go Admin Portal"
admin.site.site_title = "Info to Go Admin Portal"
admin.site.index_title = "Welcome to ITG Admin Portal"
```

В `settings.py` можно изменить язык админ-панели в константе `LANGUAGE_CODE`

**commit: `Урок 13: изменили заголовки в административной панели`**

### Настройка полей в отображении статей в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active')
admin.site.register(Article, ArticleAdmin)
```

**commit: `Урок 13: настроили поля в отображении статей в админ-панели`**

### Добавление фильтров в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active')
    list_filter = ('category', 'is_active')
admin.site.register(Article, ArticleAdmin)
```

**commit: `Урок 13: добавили фильтры в админ-панель`**

### Добавление поиска в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'content')
admin.site.register(Article, ArticleAdmin)
```

**commit: `Урок 13: добавили поиск в админ-панель`**

### Добавление пользовательского поля в админ-панели

#### models.py
```python
from django.utils.html import format_html
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active', 'colored_status')
    def colored_status(self, obj):
        return format_html('<span style="color: {};">{}</span>', 'green' if obj.is_active else 'red', obj.is_active)
    colored_status.short_description = 'Статус'
admin.site.register(Article, ArticleAdmin)
```

#### Дополнение
В `models.py` добавили пользовательский менеджер модели `AllArticleManager` для того чтобы получать список статей вне зависимости от поля `is_active`.
```python
class AllArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
```

В `admin.py` добавили метод `get_queryset` в класс `ArticleAdmin` для того чтобы получать список статей вне зависимости от поля `is_active`.
```python
    def get_queryset(self, request):
        return Article.all_objects.get_queryset()
```

**commit: `Урок 13: добавили пользовательское поле в админ-панель`

### Добавление дополнительных действий в админ-панели (сделать неактивными выбранные статьи)

#### models.py
```python
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)
    
make_inactive.short_description = "Сделать неактивными выбранные статьи
    
class ArticleAdmin(admin.ModelAdmin):
    ...
    actions = [make_inactive]
    ...
```
**commit: `Урок 13: добавили дополнительные действия в админ-панель`

### Настройка отображения полей в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    fields = ('title', 'content', 'category', 'tags', 'is_active')
    ...
```

**commit: `Урок 13: настроили отображение полей в админ-панели`**

### Добавление группировки в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):   
    ...
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Дополнительные параметры', {
            'fields': ('category', 'tags', 'is_active')
        }),
    )
    ...
```
**commit: `Урок 13: добавили группировку в админ-панель`**

### Добавлние гибкого редактирования тегов в админ-панели

#### models.py
```python
class TagInline(admin.TabularInline):
    model = Tag.article.through
    extra = 1
class ArticleAdmin(admin.ModelAdmin):
    ...
    inlines = [TagInline]
    ...
```
**commit: `Урок 13: добавили гибкое редактирование тегов в админ-панели`**


## Урок 14

### Добавление пагинации в админ-панель

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    list_per_page = 10
    ...
```

**commit: `Урок 14: добавили пагинацию в админ-панель`**

### Добавление ссылок по другим полям в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    list_display_links = ('id',)  # запятая в конце нужна, чтобы указать, что это кортеж
    ...
```

**commit: `Урок 14: добавили ссылки по другим полям в админ-панель`**

### Добавление сортировок по полям

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    ordering = ('-views', 'title')
    ...
```

**commit: `Урок 14: добавили сортировки по полям в админ-панели`**

### Перевод админ-панели

#### models.py
```python
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    class Meta:
        db_table = 'Categories'  # без указания этого параметра, таблица в БД будет называться вида 'news_categorys'
        verbose_name = 'Категория'  # единственное число для отображения в админке
        verbose_name_plural = 'Категории'  # множественное число для отображения в админке
```

#### models.py
```python
class Article(models.Model):
    title = models.CharField(..., verbose_name='Заголовок')
    content = models.TextField(..., verbose_name='Содержание')
    publication_date = models.DateTimeField(...,  verbose_name='Дата публикации')
    views = models.IntegerField(...,  verbose_name='Просмотры')
    category = models.ForeignKey(...,  verbose_name='Категория')
    tags = models.ManyToManyField(...,  verbose_name='Теги')
    slug = models.SlugField(...,  verbose_name='Слаг')
    is_active = models.BooleanField(...,  verbose_name='Активна')
```

#### apps.py
```python
class NewsConfig(AppConfig):
    ...
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'
```

**commit: `Урок 14: перевели админ-панель`**

#### добавили поле `status` в модель `Article`

- тип `BooleanField` используется для хранения булевых значений (`True` или `False`).
- параметр `choices` используется для ограничения возможных значений поля и для удобного отображения этих значений в админке Django.
- В данном случае, `choices` задается с помощью `tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices))`.
- 
_нам нужно было ограничить значения поля `status` только двумя возможными состояниями: `True` (Проверено) и `False` (Не проверено).
Для этого используется `BooleanField`, который по своей сути ограничивает значения до двух возможных вариантов._

- `Status.choices` возвращает кортеж кортежей вида `((0, 'Не проверено'), (1, 'Проверено'))`.
- С помощью `map(lambda x: (bool(x[0]), x[1]), Status.choices)` эти значения преобразуются в булевы значения: `((False, 'Не проверено'), (True, 'Проверено'))`.
- Это позволяет использовать `BooleanField` с человеко-читаемыми именами для значений.
- 
**commit: `Урок 14: добавили поле status`**

- добавили в админ. панель поле указывающее на наличие слова "пауки" в содержании статьи
- добавили в админ. панель дополнительные действия: пометить статьи как проверенные и как не проверенные

**commit: `Урок 14: добавили в админ. панель поле наличие слова пауки в содержании и дополнительные действия`**

##### Класс `ArticleCodeFilter`
Наследуется от `SimpleListFilter`, который предоставляет базовую функциональность для создания простых фильтров в админке `Django`.

##### Атрибут `title`
Задает название фильтра, которое будет отображаться в админке. В данном случае, это 'Внутри пауки'.

##### Атрибут `parameter_name`
Задает имя параметра, которое будет использоваться в `URL` для фильтрации. В данном случае, это `has_spiders`.

##### Метод `lookups`
Возвращает кортеж кортежей, где каждый внутренний кортеж состоит из двух элементов: значения параметра и человеко-читаемого названия.
В данном случае, возвращаются два варианта: `('yes', 'Да')` и `('no', 'Нет')`.

##### Метод `queryset`
Принимает запрос `request` и исходный набор данных `queryset`.
В зависимости от значения параметра `has_spiders` (которое можно получить с помощью `self.value()`), фильтрует набор данных.
Если значение параметра `has_spiders` равно `yes`, фильтрует набор данных, чтобы включить только те статьи, в которых поле `content` содержит слово 'пауки'.
Если значение параметра `has_spiders` равно `no`, фильтрует набор данных, чтобы исключить статьи, в которых поле `content` содержит слово 'пауки'.

**commit: `Урок 14: добавили кастомный фильтр по наличию пауков в тексте статьи`**


## Урок 15

### другой способ регистрации модели в админ-панели 

#### models.py
```
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ...
```

**commit: `Урок 15: посмотрели другой способ регистрации модели`**

### Добавление вывода объектов по датам

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    date_hierarchy = 'publication_date'
```

**commit: `Урок 15: добавили иерархическое отображение по дате публикации`**

### Добавление неизменяемых полей

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    readonly_fields = ('publication_date', 'views')
```

**commit: `Урок 15: пометили часть полей как неизменяемые`**

### Добавление редактирования полей в общем списке объектов

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    list_editable = ('title', 'category')
```

**commit: `Урок 15: добавили возможность изменения заголовка из списка объектов`**

### Перенос кнопок сохранения в верхнюю часть формы редактирования

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    save_on_top = True
```

**commit: `Урок 15: перенесли кнопки сохранения в верхнюю часть формы`**

### Включение возможности сохранения объекта как нового

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    save_as = True
```

**commit: `Урок 15: включили возможность сохранения объекта как нового`**

### установка `django-jazzmin`

```shell
pip install django-jazzmin
```

### настройка `django-jazzmin`

#### settings.py
```python
INSTALLED_APPS = [
    'jazzmin',
    ...
]
```

**commit: `Урок 15: установили django-jazzmin`**

### настройка интерфейса `django-jazzmin`

#### settings.py
```python
JAZZMIN_SETTINGS = {
    "site_title": "My Blog Admin",  # Заголовок административной панели
    "site_header": "My Blog",  # Заголовок окна браузера
    "site_brand": "My Blog",  # Бренд сайта
    "welcome_sign": "Welcome to My Blog Admin",  # Приветственное сообщение
    "copyright": "My Blog Ltd",  # Информация о копирайте
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,  # Показать боковую панель
    "navigation_expanded": True,  # Развернуть навигацию
    "hide_apps": [],  # Скрыть приложения
    "hide_models": [],  # Скрыть модели
    "default_icon_parents": "fas fa-chevron-circle-right",  # Иконка для родительских элементов
    "default_icon_children": "fas fa-circle",  # Иконка для дочерних элементов
    "related_modal_active": False,  # Включить модальные окна для связанных объектов
    "custom_css": None,  # Пользовательский CSS
    "custom_js": None,  # Пользовательский JS
    "use_google_fonts_cdn": True,  # Использовать Google Fonts CDN
    "show_ui_builder": True,  # Показать конструктор интерфейса
}
```

**commit: `Урок 15: настроили интерфейс django-jazzmin`**


## Урок 16

1. **itg/urls.py**:
   - **Удаление комментария**: Удалена строка комментария "Подключаем файл urls.py из приложения news через include". Это было сделано для очистки кода и удаления ненужных комментариев, которые могут засорять файл.
   - **Добавление namespace**: В маршруте `path('news/', include('news.urls'))` добавлен параметр `namespace='news'`. Это сделано для того, чтобы все маршруты, определенные в `news/urls.py`, были доступны под пространством имен `news`. Это улучшает организацию маршрутов и предотвращает конфликты имен маршрутов между различными приложениями.

3. **news/templates/include/article_preview.html**:
   - **Изменение имени маршрута**: В строке `<a href="{% url 'detail_article_by_id' article.id %}" class="btn btn-primary">Подробнее</a>` изменено имя маршрута с `'detail_article_by_id'` на `'news:detail_article_by_id'`. Это изменение необходимо для соответствия новому пространству имен `news`, что обеспечивает корректное формирование URL-адресов в шаблонах.

4. **news/urls.py**:
   - **Добавление app_name**: Добавлена строка `app_name = 'news'` для определения пространства имен приложения. Это необходимо для того, чтобы все маршруты в `news/urls.py` были доступны под пространством имен `news`, что улучшает организацию маршрутов и предотвращает конфликты имен маршрутов между различными приложениями.

5. **news/views.py**:
   - **Изменение url_name**: В словаре `info`, а также в функциях `get_all_news`, `get_detail_article_by_id` и `get_detail_article_by_slag` изменено значение ключа `"url_name"` с `"catalog"` на `"news:catalog"`. Это изменение необходимо для соответствия новому пространству имен `news`, что обеспечивает корректное формирование URL-адресов и ссылок в представлениях.
   - **Оптимизация контекста**: В функциях `get_all_news`, `get_detail_article_by_id` и `get_detail_article_by_slag` оптимизирован контекст, передаваемый в шаблоны. Вместо явного указания всех элементов меню, используется распаковка словаря `info`, что делает код более компактным и удобным для поддержки.

**commit: `Урок 16: рефакторинг кода`**


## Урок 17

1. **news/templates/include/article_preview.html**:
   - **Изменение отображения тегов**: В строке, где отображаются теги статьи, изменен элемент `<span>` на `<a>` с гиперссылкой на маршрут `news:get_news_by_tag`. Это изменение сделано для того, чтобы пользователи могли кликать на теги и переходить к странице с новостями, отфильтрованными по этому тегу.
2. **news/templates/news/article_detail.html**:
   - **Изменение отображения тегов**: Аналогичное изменение, как и в `article_preview.html`, где элемент `<span>` заменен на `<a>` с гиперссылкой на маршрут `news:get_news_by_tag`. Это изменение сделано для улучшения навигации и удобства пользователей, позволяя им переходить к новостям по тегам.
3. **news/urls.py**:
   - **Добавление нового маршрута**: Добавлен новый маршрут `path('tag/<int:tag_id>/', views.get_news_by_tag, name='get_news_by_tag')` для обработки запросов по тегам. Это изменение сделано для поддержки новой функциональности фильтрации новостей по тегам.
4. **news/views.py**:
   - **Импорт модели Tag**: Добавлен импорт модели `Tag` для работы с тегами.
   - **Изменение функции get_news_by_tag**: Функция `get_news_by_tag` изменена для фильтрации новостей по тегу. Теперь она принимает `tag_id` вместо `slug`, находит тег по его идентификатору и фильтрует новости, содержащие этот тег. Контекст обновлен для передачи отфильтрованных новостей в шаблон. Это изменение сделано для реализации функциональности фильтрации новостей по тегам и улучшения пользовательского опыта.

**commit: `Урок 17: кликабельные теги на карточках новостей`**

1. **news/templates/include/article_preview.html**:
   - **Изменение отображения категории**: В строке, где отображается категория статьи, изменен элемент `<p>` на `<a>` с гиперссылкой на маршрут `news:get_news_by_category`. Это изменение сделано для того, чтобы пользователи могли кликать на категорию и переходить к странице с новостями, отфильтрованными по этой категории.
2. **news/templates/news/article_detail.html**:
   - **Изменение отображения категории**: Аналогичное изменение, как и в `article_preview.html`, где элемент `<p>` заменен на `<a>` с гиперссылкой на маршрут `news:get_news_by_category`. Это изменение сделано для улучшения навигации и удобства пользователей, позволяя им переходить к новостям по категориям.
3. **news/urls.py**:
   - **Добавление нового маршрута**: Добавлен новый маршрут `path('category/<int:category_id>/', views.get_news_by_category, name='get_news_by_category')` для обработки запросов по категориям. Это изменение сделано для поддержки новой функциональности фильтрации новостей по категориям.
4. **news/views.py**:
   - **Импорт модели Category**: Добавлен импорт модели `Category` для работы с категориями.
   - **Изменение функции get_news_by_category**: Функция `get_news_by_category` изменена для фильтрации новостей по категории. Теперь она принимает `category_id` вместо `slug`, находит категорию по её идентификатору и фильтрует новости, принадлежащие этой категории. Контекст обновлен для передачи отфильтрованных новостей в шаблон. Это изменение сделано для реализации функциональности фильтрации новостей по категориям и улучшения пользовательского опыта.

**commit: `Урок 17: кликабельные категории на карточках новостей`**

1. **news/views.py**:
   - **Добавление категорий в контекст**: В словаре `info` добавлено поле `"categories"`, которое содержит все категории, полученные с помощью `Category.objects.all()`. Это изменение сделано для того, чтобы категории были доступны в шаблонах и могли быть использованы для отображения рубрикатора.

2**templates/base.html**:
   - **Добавление рубрикатора**: В базовый шаблон добавлен блок для отображения рубрикатора. Этот блок отображается только для приложения `news` и содержит список категорий с гиперссылками на соответствующие страницы новостей по категориям. Каждая категория отображается с именем и количеством статей в этой категории.
   - **Структура страницы**: Добавлены элементы `<div>` для создания двухколоночной структуры страницы. Основное содержимое отображается в левой колонке, а рубрикатор — в правой колонке. Это изменение сделано для улучшения навигации и удобства пользователей, позволяя им легко находить новости по категориям.

**commit: `Урок 17: добавили рубрикатор`**


## Урок 18

1. **news/urls.py**:
   - **Добавление нового маршрута для поиска**: Добавлен новый маршрут `path('search/', views.search_news, name='search_news')` для обработки запросов поиска новостей. Это изменение сделано для поддержки новой функциональности поиска новостей по запросу пользователя.
2. **news/views.py**:
   - **Импорт модуля Q**: Добавлен импорт `from django.db.models import Q` для использования сложных запросов с логическими операторами.
   - **Добавление функции search_news**: Добавлена новая функция `search_news`, которая обрабатывает запросы поиска. Функция получает параметр запроса `q` из GET-запроса, фильтрует статьи по заголовку и содержимому, содержащим запрос, и передает отфильтрованные статьи в шаблон. Если запрос пустой, возвращаются все статьи. Это изменение сделано для реализации функциональности поиска новостей по запросу пользователя.
3. **templates/base.html**:
   - **Добавление формы поиска**: В базовый шаблон добавлена форма поиска, которая отправляет GET-запрос на маршрут `news:search_news`. Форма содержит поле ввода для запроса и кнопку отправки. Это изменение сделано для предоставления пользователям возможности искать новости по ключевым словам, улучшая навигацию и пользовательский опыт.

**commit: `Урок 18: добавили поиск по заголовку или содержимому новости`**

1. **news/templates/include/article_preview.html**:
   - **Изменение стиля ссылок на категории**: В строке, где отображается категория статьи, добавлены классы `text-decoration-none text-primary fw-bold` для улучшения стиля ссылок на категории. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Изменение отображения даты публикации**: В строке, где отображается дата публикации статьи, добавлен элемент `<small>` с классом `text-muted` и иконкой календаря `<i class="bi bi-calendar"></i>`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Изменение отображения количества просмотров**: В строке, где отображается количество просмотров статьи, добавлена иконка глаза `<i class="bi bi-eye-fill"></i>`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Изменение стиля кнопки "Подробнее"**: В строке, где отображается кнопка "Подробнее", изменен класс кнопки с `btn-primary` на `btn-outline-secondary`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
2. **news/templates/news/article_detail.html**:
   - **Изменение стиля ссылок на категории**: Аналогичное изменение, как и в `article_preview.html`, где добавлены классы `text-decoration-none text-primary fw-bold` для улучшения стиля ссылок на категории.
   - **Изменение отображения даты публикации**: Аналогичное изменение, как и в `article_preview.html`, где добавлен элемент `<small>` с классом `text-muted` и иконкой календаря `<i class="bi bi-calendar"></i>`.
   - **Изменение отображения количества просмотров**: Аналогичное изменение, как и в `article_preview.html`, где добавлена иконка глаза `<i class="bi bi-eye-fill"></i>`.
3. **news/views.py**:
   - **Импорт модуля F**: Добавлен импорт `from django.db.models import F` для использования выражений базы данных.
   - **Обновление количества просмотров**: В функции `get_detail_article_by_id` добавлено обновление количества просмотров статьи с использованием `F('views') + 1`. После обновления количества просмотров объект статьи обновляется из базы данных с помощью `article.refresh_from_db()`. Это изменение сделано для автоматического увеличения счетчика просмотров при каждом просмотре статьи.
4. **templates/base.html**:
   - **Добавление стилей для иконок**: Добавлена ссылка на стили иконок Bootstrap `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">`. Это изменение сделано для использования иконок Bootstrap в шаблонах.

**commit: `Урок 18: добавили увеличение просмотров по клику`**

1. **news/templates/include/paginator.html**:
   - **Создание шаблона пагинатора**: Создан новый шаблон для пагинатора, который включает навигационные элементы для перехода между страницами. Шаблон содержит ссылки на первую и последнюю страницы, а также на предыдущую и следующую страницы, если они существуют. Это изменение сделано для улучшения навигации по страницам с новостями, предоставляя пользователям удобный способ перехода между страницами.
2. **news/templates/news/catalog.html**:
   - **Интеграция пагинатора**: В шаблон каталога новостей добавлены включения шаблона пагинатора `include "include/paginator.html" with page=page_obj` до и после цикла отображения новостей. Это изменение сделано для интеграции пагинатора в каталог новостей, что позволяет пользователям легко переходить между страницами с новостями.
   - **Изменение цикла отображения новостей**: В цикле отображения новостей изменен источник данных с `news` на `page_obj`, чтобы отображать только новости текущей страницы. Это изменение сделано для корректного отображения новостей на текущей странице пагинатора.
3. **news/views.py**:
   - **Импорт модуля Paginator**: Добавлен импорт `from django.core.paginator import Paginator` для использования пагинации.
   - **Добавление пагинации**: В функции `get_all_news` добавлена логика пагинации. Создан объект `Paginator` для разбиения новостей на страницы по 20 новостей на страницу. Получен номер текущей страницы из GET-запроса и создан объект `page_obj` для текущей страницы. Это изменение сделано для реализации пагинации новостей, что позволяет пользователям просматривать новости постранично.
   - **Обновление контекста**: В контекст добавлен объект `page_obj` для передачи информации о текущей странице в шаблон. Это изменение сделано для передачи данных пагинатора в шаблон, что позволяет корректно отображать навигационные элементы пагинатора.

**commit: `Урок 18: добавили пагинацию`**


## Урок 19

1. **news/models.py**:
   - **Добавление модели Like**: Добавлена новая модель `Like`, которая отслеживает лайки на статьи. Модель содержит поля `article` (ссылка на статью) и `ip_address` (IP-адрес пользователя, поставившего лайк). Это изменение сделано для реализации функциональности лайков на статьи, что позволяет пользователям выражать свое мнение о статьях.
2. **news/templates/include/article_preview.html**:
   - **Загрузка пользовательских тегов**: Добавлена строка `{% load customtags %}` для загрузки пользовательских тегов шаблонов.
   - **Изменение отображения количества лайков**: В строке, где отображается количество лайков статьи, добавлена иконка сердца `<i class="bi bi-heart-fill"></i>` и изменено отображение количества лайков с `article.favorites_count` на `article.likes.count`. Это изменение сделано для улучшения визуального оформления и отображения количества лайков.
3. **news/templates/news/article_detail.html**:
   - **Изменение отображения количества лайков**: Аналогичное изменение, как и в `article_preview.html`, где добавлена иконка сердца `<i class="bi bi-heart-fill"></i>` и изменено отображение количества лайков с `article.favorites_count` на `article.likes.count`.
   - **Добавление формы для лайков**: Добавлена форма для отправки лайков на статью. Форма содержит кнопку, которая меняет текст в зависимости от того, поставил ли пользователь лайк на статью или нет. Это изменение сделано для реализации функциональности лайков на статьи, что позволяет пользователям выражать свое мнение о статьях.
4. **news/templatetags/customtags.py**:
   - **Импорт модели Like**: Добавлен импорт модели `Like` для использования в пользовательских тегах шаблонов.
   - **Добавление фильтра has_liked**: Добавлен новый фильтр `has_liked`, который проверяет, поставил ли пользователь лайк на статью. Это изменение сделано для использования в шаблонах для отображения состояния лайка.
5. **news/urls.py**:
   - **Добавление нового маршрута для лайков**: Добавлен новый маршрут `path('like/<int:article_id>/', views.toggle_like, name='toggle_like')` для обработки запросов на добавление или удаление лайков на статьи. Это изменение сделано для поддержки новой функциональности лайков.
6. **news/views.py**:
   - **Импорт функций redirect и get_object_or_404**: Добавлены импорты `redirect` и `get_object_or_404` для использования в представлениях.
   - **Добавление функции toggle_like**: Добавлена новая функция `toggle_like`, которая обрабатывает запросы на добавление или удаление лайков на статьи. Функция получает IP-адрес пользователя и статью, проверяет наличие лайка и создает или удаляет лайк в зависимости от состояния. После этого происходит перенаправление на страницу статьи. Это изменение сделано для реализации функциональности лайков на статьи.
   - **Обновление контекста**: В контекст добавлен параметр `user_ip`, который содержит IP-адрес пользователя. Это изменение сделано для передачи IP-адреса пользователя в шаблоны, что позволяет корректно отображать состояние лайка.

**commit: `Урок 19: добавили лайки`**

1. **news/models.py**:
   - **Добавление модели Favorite**: Добавлена новая модель `Favorite`, которая отслеживает избранные статьи пользователей. Модель содержит поля `article` (ссылка на статью) и `ip_address` (IP-адрес пользователя, добавившего статью в избранное). Это изменение сделано для реализации функциональности избранных статей, что позволяет пользователям сохранять статьи для последующего просмотра.
2. **news/templates/news/article_detail.html**:
   - **Загрузка пользовательских тегов**: Изменена строка `{% load upper_words %}` на `{% load customtags %}` для загрузки пользовательских тегов шаблонов.
   - **Изменение отображения заголовка статьи**: Удален фильтр `upper_words` для отображения заголовка статьи. Теперь заголовок отображается без изменения регистра.
   - **Добавление формы для избранных статей**: Добавлена форма для добавления или удаления статьи из избранного. Форма содержит кнопку, которая меняет текст в зависимости от того, добавлена ли статья в избранное или нет. Это изменение сделано для реализации функциональности избранных статей, что позволяет пользователям сохранять статьи для последующего просмотра.
3. **news/templatetags/customtags.py**:
   - **Импорт модели Favorite**: Добавлен импорт модели `Favorite` для использования в пользовательских тегах шаблонов.
   - **Добавление фильтра has_favorited**: Добавлен новый фильтр `has_favorited`, который проверяет, добавил ли пользователь статью в избранное. Это изменение сделано для использования в шаблонах для отображения состояния избранного.
4. **news/urls.py**:
   - **Добавление новых маршрутов для избранных статей**: Добавлены новые маршруты `path('favorite/<int:article_id>/', views.toggle_favorite, name='toggle_favorite')` и `path('favorites/', views.favorites, name='favorites')` для обработки запросов на добавление или удаление статей из избранного и отображения списка избранных статей. Это изменение сделано для поддержки новой функциональности избранных статей.
5. **news/views.py**:
   - **Импорт модели Favorite**: Добавлен импорт модели `Favorite` для использования в представлениях.
   - **Добавление функции favorites**: Добавлена новая функция `favorites`, которая отображает список избранных статей пользователя. Функция получает IP-адрес пользователя и фильтрует статьи, добавленные в избранное этим пользователем. Это изменение сделано для реализации функциональности отображения списка избранных статей.
   - **Добавление функции toggle_favorite**: Добавлена новая функция `toggle_favorite`, которая обрабатывает запросы на добавление или удаление статей из избранного. Функция получает IP-адрес пользователя и статью, проверяет наличие статьи в избранном и создает или удаляет запись в зависимости от состояния. После этого происходит перенаправление на страницу статьи. Это изменение сделано для реализации функциональности избранных статей.
   - **Обновление контекста**: В контекст добавлен параметр `user_ip`, который содержит IP-адрес пользователя. Это изменение сделано для передачи IP-адреса пользователя в шаблоны, что позволяет корректно отображать состояние избранного.

**commit: `Урок 19: добавили избранные`**


## Урок 20

1. **news/templates/include/article_preview.html**:
   - **Изменение отображения содержимого статьи**: В строке, где отображается содержимое статьи, изменен фильтр с `truncatechars:50` на `truncatewords:7`. Это изменение сделано для более читаемого отображения содержимого статьи, обрезая его до 7 слов.
   - **Изменение отображения тегов**: В строке, где отображаются теги статьи, изменены классы и стили. Добавлены стили для цвета тега с использованием фильтра `random_color` и иконка `<i class="bi bi-hash"></i>`. Текст тега теперь отображается в верхнем регистре. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Удаление отображения количества просмотров и лайков**: Удалены строки, отображающие количество просмотров и лайков статьи. Это изменение сделано для упрощения интерфейса и фокусировки на основной информации.
2. **news/templates/news/article_detail.html**:
   - **Изменение отображения тегов**: Аналогичное изменение, как и в `article_preview.html`, где добавлены стили для цвета тега с использованием фильтра `random_color` и иконка `<i class="bi bi-hash"></i>`. Текст тега теперь отображается в верхнем регистре.
   - **Изменение стиля кнопок лайков и избранного**: В строках, где отображаются кнопки для лайков и избранного, изменены классы кнопок с `btn-primary` на `btn-link p-0 text-black text-decoration-none`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Изменение отображения состояния лайков и избранного**: В строках, где отображается состояние лайков и избранного, изменены иконки и текст. Для лайков добавлены иконки `<i class="bi bi-balloon-heart-fill"></i>` и `<i class="bi bi-balloon-heart"></i>`, а для избранного — `<i class="bi bi-star-fill"></i>` и `<i class="bi bi-star"></i>`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
3. **news/templatetags/customtags.py**:
   - **Импорт модуля random**: Добавлен импорт модуля `random` для генерации случайных цветов.
   - **Добавление фильтра random_color**: Добавлен новый фильтр `random_color`, который генерирует уникальный цвет для каждого тега на основе его ID. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
4. **news/views.py**:
   - **Изменение логики увеличения счетчика просмотров**: В функции `get_detail_article_by_id` изменена логика увеличения счетчика просмотров статьи. Теперь счетчик просмотров увеличивается только один раз за сессию для каждой новости. Это изменение сделано для предотвращения многократного увеличения счетчика просмотров при обновлении страницы.

**commit: `Урок 20: улучшение интерфейса`**

1. **news/templates/include/paginator.html**:
   - **Изменение структуры пагинатора**: Изменен контейнер пагинатора с `<div class="pagination">` на `<nav aria-label="Page navigation">`. Это изменение сделано для улучшения семантики HTML и доступности.
   - **Изменение структуры ссылок**: Ссылки на первую, предыдущую, следующую и последнюю страницы обернуты в элементы `<li class="page-item">`, а сами ссылки обернуты в элементы `<a class="page-link">`. Это изменение сделано для улучшения стилизации и доступности пагинатора.
   - **Добавление атрибутов aria-label**: Добавлены атрибуты `aria-label` для ссылок на первую, предыдующую, следующую и последнюю страницы. Это изменение сделано для улучшения доступности пагинатора.
   - **Добавление иконок для навигации**: Добавлены иконки для навигации (`&laquo;`, `&lsaquo;`, `&rsaquo;`, `&raquo;`) с использованием элементов `<span aria-hidden="true">`. Это изменение сделано для улучшения визуального оформления пагинатора.
   - **Изменение отображения текущей страницы**: Удален элемент `<span class="current">` и заменен на цикл, который отображает все номера страниц. Текущая страница подсвечивается с помощью класса `active`. Это изменение сделано для улучшения навигации и визуального оформления пагинатора.

**commit: `Урок 20: улучшение пагинатора`**

1. **news/templates/include/article_preview.html**:
   - **Изменение структуры карточки**: Изменен контейнер карточки с `<div class="card">` на `<div class="card card-shadow">` для добавления эффекта тени. Это изменение сделано для улучшения визуального оформления карточки.
   - **Изменение отображения категории**: В строке, где отображается категория статьи, добавлен класс `category-link` для улучшения стилизации ссылки на категорию. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Изменение отображения тегов**: В строке, где отображаются теги статьи, добавлен стиль `color: {{ tag|random_color }}` для случайного цвета тега и иконка `<i class="bi bi-hash"></i>`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Изменение отображения даты публикации и количества просмотров**: В строке, где отображается дата публикации и количество просмотров статьи, добавлены иконки `<i class="bi bi-calendar"></i>` и `<i class="bi bi-eye-fill"></i>`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Добавление формы для лайков**: Добавлена форма для добавления или удаления лайков на статью. Форма содержит кнопку, которая меняет текст и иконку в зависимости от того, поставил ли пользователь лайк на статью или нет. Это изменение сделано для реализации функциональности лайков на статьи, что позволяет пользователям выражать свое мнение о статьях.
   - **Добавление формы для избранных статей**: Добавлена форма для добавления или удаления статьи из избранного. Форма содержит кнопку, которая меняет текст и иконку в зависимости от того, добавлена ли статья в избранное или нет. Это изменение сделано для реализации функциональности избранных статей, что позволяет пользователям сохранять статьи для последующего просмотра.
   - **Изменение стиля кнопки "Подробнее"**: В строке, где отображается кнопка "Подробнее", добавлен класс `mt-2` для добавления отступа сверху. Это изменение сделано для улучшения визуального оформления и удобства пользователей.

2. **news/templates/include/paginator.html**:
   - **Изменение структуры пагинатора**: Изменен контейнер пагинатора с `<div class="pagination">` на `<nav aria-label="Page navigation">`. Это изменение сделано для улучшения семантики HTML и доступности.
   - **Изменение структуры ссылок**: Ссылки на первую, предыдущую, следующую и последнюю страницы обернуты в элементы `<li class="page-item">`, а сами ссылки обернуты в элементы `<a class="page-link">`. Это изменение сделано для улучшения стилизации и доступности пагинатора.
   - **Добавление атрибутов aria-label**: Добавлены атрибуты `aria-label` для ссылок на первую, предыдущую, следующую и последнюю страницы. Это изменение сделано для улучшения доступности пагинатора.
   - **Добавление иконок для навигации**: Добавлены иконки для навигации (`&laquo;`, `&lsaquo;`, `&rsaquo;`, `&raquo;`) с использованием элементов `<span aria-hidden="true">`. Это изменение сделано для улучшения визуального оформления пагинатора.
   - **Изменение отображения текущей страницы**: Удален элемент `<span class="current">` и заменен на цикл, который отображает все номера страниц. Текущая страница подсвечивается с помощью класса `active`. Это изменение сделано для улучшения навигации и визуального оформления пагинатора.

3. **news/templates/include/rubricator.html**:
   - **Создание шаблона рубрикатора**: Создан новый шаблон для рубрикатора, который включает список категорий с гиперссылками на соответствующие страницы новостей по категориям. Каждая категория отображается с именем и количеством статей в этой категории. Это изменение сделано для улучшения навигации и удобства пользователей, позволяя им легко находить новости по категориям.

4. **news/templates/include/search_form.html**:
   - **Создание шаблона формы поиска**: Создан новый шаблон для формы поиска, который содержит поле ввода для запроса и кнопку отправки. Это изменение сделано для предоставления пользователям возможности искать новости по ключевым словам, улучшая навигацию и пользовательский опыт.

5. **news/templates/news/article_detail.html**:
   - **Изменение структуры карточки**: Изменен контейнер карточки с `<div class="card">` на `<div class="card card-shadow">` для добавления эффекта тени. Это изменение сделано для улучшения визуального оформления карточки.
   - **Изменение отображения категории**: В строке, где отображается категория статьи, добавлен класс `category-link` для улучшения стилизации ссылки на категорию. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Изменение отображения тегов**: В строке, где отображаются теги статьи, добавлен стиль `color: {{ tag|random_color }}` для случайного цвета тега и иконка `<i class="bi bi-hash"></i>`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Изменение отображения даты публикации и количества просмотров**: В строке, где отображается дата публикации и количество просмотров статьи, добавлены иконки `<i class="bi bi-calendar"></i>` и `<i class="bi bi-eye-fill"></i>`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Добавление формы для лайков**: Добавлена форма для добавления или удаления лайков на статью. Форма содержит кнопку, которая меняет текст и иконку в зависимости от того, поставил ли пользователь лайк на статью или нет. Это изменение сделано для реализации функциональности лайков на статьи, что позволяет пользователям выражать свое мнение о статьях.
   - **Добавление формы для избранных статей**: Добавлена форма для добавления или удаления статьи из избранного. Форма содержит кнопку, которая меняет текст и иконку в зависимости от того, добавлена ли статья в избранное или нет. Это изменение сделано для реализации функциональности избранных статей, что позволяет пользователям сохранять статьи для последующего просмотра.

6. **news/templates/news/catalog.html**:
   - **Изменение структуры страницы**: Удалены элементы `<p class="text-center">` для отображения общего количества новостей и пользователей. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Добавление формы поиска**: Добавлен включенный шаблон формы поиска `include "include/search_form.html"` для предоставления пользователям возможности искать новости по ключевым словам, улучшая навигацию и пользовательский опыт.

7. **templates/base.html**:
   - **Изменение стилей**: Изменены стили для различных элементов, таких как `body`, `navbar`, `card`, `btn-outline-secondary`, `btn-outline-success`, `text-primary`, `text-secondary`, `text-success`, `text-danger`, `text-warning`, `text-info`, `text-light`, `text-dark`, `bg-primary`, `bg-secondary`, `bg-success`, `bg-danger`, `bg-warning`, `bg-info`, `bg-light`, `bg-dark`, `navbar-brand`, `hover-effect`. Эти изменения сделаны для улучшения визуального оформления и удобства пользователей.
   - **Изменение структуры страницы**: Добавлены классы `main-content`, `rubricator` для улучшения структуры и стилизации страницы. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Удаление формы поиска**: Удалена форма поиска из шаблона `base.html` и заменена на включенный шаблон формы поиска `include "include/search_form.html"` в других шаблонах. Это изменение сделано для улучшения структуры и удобства пользователей.
   - **Удаление футера**: Удален элемент `<footer>` из шаблона `base.html`. Это изменение сделано для улучшения структуры и удобства пользователей.

8. **templates/main.html**:
   - **Удаление блока footer**: Удален блок `footer` из шаблона `main.html`. Это изменение сделано для улучшения структуры и удобства пользователей.

### Список используемых тегов и стилей с их описанием

1. **HTML теги**:
   - `<div>`: Контейнер для группировки элементов.
   - `<nav>`: Навигационный элемент для пагинатора.
   - `<ul>`: Неупорядоченный список для элементов пагинатора.
   - `<li>`: Элемент списка для элементов пагинатора.
   - `<a>`: Гиперссылка для навигации.
   - `<form>`: Форма для отправки данных.
   - `<input>`: Поле ввода для формы поиска.
   - `<button>`: Кнопка для отправки формы.
   - `<i>`: Иконка для визуального оформления.
   - `<small>`: Мелкий текст для отображения даты публикации.
   - `<span>`: Контейнер для группировки элементов без семантического значения.

2. **Bootstrap классы**:
   - `card`: Стиль для карточки.
   - `card-body`: Стиль для тела карточки.
   - `card-title`: Стиль для заголовка карточки.
   - `card-text`: Стиль для текста карточки.
   - `text-decoration-none`: Убирает подчеркивание текста.
   - `text-primary`: Цвет текста (синий).
   - `fw-bold`: Жирный шрифт.
   - `d-flex`: Флексбокс для горизонтального выравнивания.
   - `justify-content-between`: Распределение элементов по краям контейнера.
   - `align-items-center`: Выравнивание элементов по центру по вертикали.
   - `mt-2`: Отступ сверху.
   - `btn`: Стиль для кнопки.
   - `btn-link`: Стиль для кнопки-ссылки.
   - `btn-outline-secondary`: Стиль для кнопки с обводкой (серая).
   - `btn-outline-success`: Стиль для кнопки с обводкой (зеленая).
   - `pagination`: Стиль для пагинатора.
   - `page-item`: Стиль для элемента пагинатора.
   - `page-link`: Стиль для ссылки пагинатора.
   - `active`: Стиль для активного элемента пагинатора.
   - `list-group`: Стиль для списка групп.
   - `list-group-item`: Стиль для элемента списка групп.
   - `list-group-item-action`: Стиль для активного элемента списка групп.
   - `d-inline`: Встроенный элемент.
   - `bg-primary`: Фон элемента (синий).
   - `bg-info`: Фон элемента (голубой).
   - `rounded-pill`: Закругленные углы элемента.
   - `badge`: Стиль для бейджа.
   - `form-inline`: Встроенная форма.
   - `form-control`: Стиль для поля ввода.
   - `input-group`: Группа ввода.
   - `navbar`: Стиль для навигационной панели.
   - `navbar-nav`: Стиль для навигационного меню.
   - `nav-link`: Стиль для ссылки навигационного меню.
   - `hover-effect`: Эффект при наведении.

3. **CSS стили**:
   - `box-shadow`: Тень элемента.
   - `transition`: Плавный переход элемента.
   - `transform`: Трансформация элемента.
   - `position`: Позиционирование элемента.
   - `width`: Ширина элемента.
   - `top`: Отступ сверху.
   - `bottom`: Отступ снизу.
   - `left`: Отступ слева.
   - `background-color`: Цвет фона элемента.
   - `color`: Цвет текста элемента.
   - `border-color`: Цвет границы элемента.
   - `overflow-y`: Вертикальное переполнение элемента.
   - `z-index`: Индекс слоя элемента.
   - `margin-bottom`: Отступ снизу.
   - `padding-top`: Внутренний отступ сверху.
   - `margin-left`: Отступ слева.
   - `background`: Фон элемента.
   - `-webkit-background-clip`: Обрезка фона элемента.
   - `-webkit-text-fill-color`: Цвет заливки текста элемента.
   - `font-weight`: Толщина шрифта элемента.

**commit: `Урок 20: рефакторинг вёрстки`**


## Урок 21

### Формы в Django
- Создали форму не связанную с моделью. Форма для добавления карточек
- Создали представление, обрабатывающее метод `POST` и возвращающее форму
- Создали шаблон для формы
- Протестировали работу формы
- Проверили валидацию формы

1. **news/forms.py**:
   - **Создание формы ArticleForm**: Создан новый файл `forms.py` с определением формы `ArticleForm`. Форма содержит два поля: `title` (заголовок) и `content` (содержание). Поле `title` имеет максимальную длину 255 символов, а поле `content` использует виджет `Textarea` и имеет максимальную длину 5000 символов. Это изменение сделано для создания формы, которая позволяет пользователям добавлять новые статьи.
2. **news/templates/news/add_article.html**:
   - **Создание шаблона для добавления статьи**: Создан новый шаблон `add_article.html`, который расширяет базовый шаблон и содержит форму для добавления новой статьи. Форма отправляется методом POST и содержит кнопку отправки. Это изменение сделано для предоставления пользователям интерфейса для добавления новых статей.
3. **news/urls.py**:
   - **Добавление нового маршрута для добавления статьи**: Добавлен новый маршрут `path('add/', views.add_article, name='add_article')` для обработки запросов на добавление новой статьи. Это изменение сделано для поддержки новой функциональности добавления статей.
4. **news/views.py**:
   - **Импорт HttpResponseRedirect и ArticleForm**: Добавлены импорты `HttpResponseRedirect` и `ArticleForm` для использования в представлениях.
   - **Добавление функции add_article**: Добавлена новая функция `add_article`, которая обрабатывает запросы на добавление новой статьи. Функция проверяет метод запроса (POST или GET), создает экземпляр формы `ArticleForm`, проверяет валидность данных формы и перенаправляет пользователя на главную страницу при успешной отправке формы. Это изменение сделано для реализации функциональности добавления новых статей.

### Для чего нужны формы?
**Формы в Django**:
Формы в `Django` используются для обработки и валидации данных, введенных пользователями. Они позволяют разработчикам легко создавать `HTML`-формы, обрабатывать данные формы и выполнять валидацию. Формы могут быть использованы для различных целей, таких как создание, обновление и удаление данных в базе данных.
**Как работает этот код**:
1. **Определение формы (news/forms.py)**:
   - Форма `ArticleForm` определена с использованием класса `forms.Form`. Она содержит два поля: `title` и `content`. Поле `title` использует виджет `CharField` с максимальной длиной 255 символов, а поле `content` использует виджет `Textarea` с максимальной длиной 5000 символов.
2. **Шаблон для добавления статьи (news/templates/news/add_article.html)**:
   - Шаблон `add_article.html` расширяет базовый шаблон и содержит форму для добавления новой статьи. Форма отправляется методом POST и содержит кнопку отправки. Шаблон использует тег `{% csrf_token %}` для защиты от CSRF-атак.
3. **Маршрут для добавления статьи (news/urls.py)**:
   - Добавлен новый маршрут `path('add/', views.add_article, name='add_article')` для обработки запросов на добавление новой статьи. Маршрут связывает URL `/add/` с представлением `add_article`.
4. **Представление для добавления статьи (news/views.py)**:
   - Функция `add_article` обрабатывает запросы на добавление новой статьи. Она проверяет метод запроса (POST или GET). Если метод POST, создается экземпляр формы `ArticleForm` с данными из запроса, проверяется валидность данных формы и, при успешной валидации, пользователь перенаправляется на главную страницу. Если метод GET, создается пустой экземпляр формы `ArticleForm`. Контекст содержит форму и меню, и шаблон `add_article.html` рендерится с этим контекстом.

### Список используемых тегов, стилей, классов и функций с их описанием
1. **HTML теги**:
   - `<form>`: Форма для отправки данных.
   - `<input>`: Поле ввода для формы.
   - `<button>`: Кнопка для отправки формы.
   - `<h1>`: Заголовок первого уровня.
   - `{% csrf_token %}`: Тег для защиты от CSRF-атак.
   - `{% extends "base.html" %}`: Тег для расширения базового шаблона.
   - `{% block content %}`: Тег для определения блока контента.
   - `{% endblock %}`: Тег для завершения блока контента.
2. **Django теги**:
   - `{% csrf_token %}`: Тег для защиты от CSRF-атак.
   - `{{ form.as_p }}`: Тег для отображения формы в виде абзацев.
3. **Django классы**:
   - `forms.Form`: Класс для создания формы.
   - `forms.CharField`: Класс для создания текстового поля.
   - `forms.Textarea`: Класс для создания текстовой области.
   - `HttpResponseRedirect`: Класс для перенаправления HTTP-запросов.
   - `get_object_or_404`: Функция для получения объекта или возврата ошибки 404.
   - `redirect`: Функция для перенаправления.
   - `render`: Функция для рендеринга шаблона.

**commit: `Урок 21: базовая форма для добавления карточек`**

- Дополнили шаблон с построчным рендером полей ввода
- Добавили категорию как выпадающий список `form.ChoiceField`

1. **news/forms.py**:
   - **Импорт модели Category**: Добавлен импорт модели `Category` для использования в форме.
   - **Добавление поля category в ArticleForm**: В форму `ArticleForm` добавлено новое поле `category`, которое является выпадающим списком (`ModelChoiceField`). Поле использует все объекты модели `Category` в качестве вариантов выбора. Поле обязательно для заполнения и имеет метку `Категория` и пустое значение `Категория не выбрана`. Это изменение сделано для того, чтобы пользователи могли выбирать категорию для новой статьи при её добавлении.
2. **news/templates/news/add_article.html**:
   - **Изменение отображения формы**: В шаблоне `add_article.html` изменено отображение формы. Теперь каждое поле формы отображается отдельно с использованием цикла `{% for field in form %}`. Для каждого поля отображается метка (`label_tag`) и само поле (`field`). Если у поля есть ошибки, они отображаются в элементе `<div class="error">`. Это изменение сделано для улучшения отображения формы и удобства пользователей при заполнении формы.
   - **Изменение кнопки отправки**: Кнопка отправки формы изменена с `<button type="submit">Добавить</button>` на `<input type="submit" value="Отправить">`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.

### Список используемых тегов и стилей с их описанием
1. **HTML теги**:
   - `{% for field in form %}`: Тег для цикла по полям формы.
   - `{% if field.errors %}`: Тег для условия проверки наличия ошибок у поля.
2. **Django теги**:
   - `{{ form.as_p }}`: Тег для отображения формы в виде абзацев.
   - `{{ field.label_tag }}`: Тег для отображения метки поля.
   - `{{ field }}`: Тег для отображения самого поля.
   - `{{ field.errors }}`: Тег для отображения ошибок поля.

**commit: `Урок 21: дополнили шаблон с построчным рендером полей ввода`**

- Передали классы и атрибуты в форму через класс формы
- Добавили обработку формы и сохранение данных в представлении

1. **news/forms.py**:
   - **Изменение поля title**: В поле `title` формы `ArticleForm` добавлены атрибуты `max_length=100` и `widget=forms.TextInput(attrs={'class': 'form-control'})`. Это изменение сделано для ограничения длины заголовка до 100 символов и добавления стиля Bootstrap для текстового поля.
   - **Изменение поля content**: В поле `content` формы `ArticleForm` добавлены атрибуты `widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 40})`. Это изменение сделано для добавления стиля Bootstrap для текстовой области и установки размеров текстовой области.
   - **Изменение поля category**: В поле `category` формы `ArticleForm` добавлен атрибут `widget=forms.Select(attrs={'class': 'form-control'})`. Это изменение сделано для добавления стиля Bootstrap для выпадающего списка.
2. **news/templates/news/add_article.html**:
   - **Изменение заголовка**: Заголовок страницы изменен с "Добавить новость" на "Предложить новость". Это изменение сделано для улучшения пользовательского опыта.
   - **Добавление контейнера и строки**: Добавлены контейнер `<div class="container-fluid">` и строка `<div class="row">` для улучшения структуры страницы.
   - **Добавление колонки для формы**: Добавлена колонка `<div class="col-12 col-lg-6">` для формы редактирования. Это изменение сделано для улучшения структуры страницы и удобства пользователей.
   - **Изменение отображения полей формы**: В цикле `{% for field in form %}` изменено отображение полей формы. Теперь каждое поле отображается в элементе `<div class="mb-3">` с меткой и самим полем. Если у поля есть ошибки, они отображаются в элементе `<div class="alert alert-danger mt-1">`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Добавление кнопки отправки**: Кнопка отправки формы изменена на `<button type="submit" class="btn btn-dark">Отправить</button>`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Добавление колонки с подсказкой**: Добавлена колонка `<div class="col-12 col-lg-6">` с подсказкой по заполнению формы. Это изменение сделано для улучшения пользовательского опыта и предоставления пользователям инструкций по заполнению формы.
3. **news/views.py**:
   - **Изменение функции add_article**: В функции `add_article` добавлены строки для сохранения статьи в базе данных. Теперь при успешной валидации формы создается объект `Article` с данными из формы и сохраняется в базе данных. После сохранения статьи пользователь перенаправляется на страницу карточки новости. Это изменение сделано для реализации функциональности добавления новых статей и сохранения их в базе данных.

### Список используемых классов с их описанием
1. **Bootstrap классы**:
   - `form-control`: Стиль для текстового поля.
   - `form-label`: Стиль для метки поля.
   - `alert alert-danger`: Стиль для отображения ошибок.
   - `btn btn-dark`: Стиль для кнопки отправки формы.
   - `container-fluid`: Контейнер для жидкой верстки.
   - `row`: Строка для размещения колонок.
   - `col-12 col-lg-6`: Колонка для размещения элементов.
   - `mb-3`: Отступ снизу.
   - `mt-1`: Отступ сверху.
   
**commit: `Урок 21: сохранение данных из формы в базу данных`**


## Урок 22

1. **news/forms.py**:
   - **Импорт моделей Article и Tag**: Добавлены импорты моделей `Article` и `Tag` для использования в форме.
   - **Изменение класса ArticleForm**: Класс `ArticleForm` изменен с `forms.Form` на `forms.ModelForm`. Это изменение сделано для упрощения работы с моделью `Article` и автоматического создания полей формы на основе модели.
   - **Добавление поля tags**: Добавлено новое поле `tags`, которое является множественным выбором (`ModelMultipleChoiceField`) с использованием модели `Tag`. Поле использует виджет `CheckboxSelectMultiple` и не является обязательным для заполнения. Это изменение сделано для того, чтобы пользователи могли выбирать несколько тегов для новой статьи.
   - **Добавление класса Meta**: Добавлен внутренний класс `Meta` для определения модели и полей, которые будут использоваться в форме. В классе `Meta` определены поля `title`, `content`, `category` и `tags`, а также виджеты и метки для этих полей. Это изменение сделано для автоматического создания полей формы на основе модели и упрощения работы с формой.

### Объяснение как это работает
1. **Определение формы (news/forms.py)**:
   - Форма `ArticleForm` определена с использованием класса `forms.ModelForm`. Она содержит поля `title`, `content`, `category` и `tags`. Поле `title` использует виджет `CharField` с максимальной длиной 100 символов и стилем Bootstrap. Поле `content` использует виджет `Textarea` с максимальной длиной 5000 символов и стилем Bootstrap. Поле `category` использует виджет `ModelChoiceField` для выбора категории из модели `Category` и стилем Bootstrap. Поле `tags` использует виджет `ModelMultipleChoiceField` для множественного выбора тегов из модели `Tag`.
2. **Шаблон для добавления статьи (news/templates/news/add_article.html)**:
   - Шаблон `add_article.html` расширяет базовый шаблон и содержит форму для добавления новой статьи. Форма отправляется методом POST и содержит кнопку отправки. Шаблон использует тег `{% csrf_token %}` для защиты от CSRF-атак.
   - Каждое поле формы отображается отдельно с использованием цикла `{% for field in form %}`. Для каждого поля отображается метка (`label_tag`) и само поле (`field`). Если у поля есть ошибки, они отображаются в элементе `<div class="alert alert-danger mt-1">`.
   - Добавлена колонка с подсказкой по заполнению формы для улучшения пользовательского опыта.
3. **Маршрут для добавления статьи (news/urls.py)**:
   - Добавлен новый маршрут `path('add/', views.add_article, name='add_article')` для обработки запросов на добавление новой статьи. Маршрут связывает URL `/add/` с представлением `add_article`.
4. **Представление для добавления статьи (news/views.py)**:
   - Функция `add_article` обрабатывает запросы на добавление новой статьи. Она проверяет метод запроса (POST или GET). Если метод POST, создается экземпляр формы `ArticleForm` с данными из запроса, проверяется валидность данных формы и, при успешной валидации, создается объект `Article` с данными из формы и сохраняется в базе данных. После сохранения статьи пользователь перенаправляется на страницу карточки новости. Если метод GET, создается пустой экземпляр формы `ArticleForm`. Контекст содержит форму и меню, и шаблон `add_article.html` рендерится с этим контекстом.

**commit: `Урок 22: переделали форму на ModelForm`**

1. **news/models.py**:
   - **Добавление поля image**: В модель `Article` добавлено новое поле `image`, которое является полем для загрузки изображений (`ImageField`). Поле использует параметр `upload_to='articles/'` для указания директории загрузки, `blank=True` для разрешения пустых значений и `null=True` для разрешения значений NULL в базе данных. Поле имеет метку `Изображение`. Это изменение сделано для того, чтобы пользователи могли загружать изображения для статей.
2. **requirements.txt**:
   - **Добавление библиотеки Pillow**: В файл `requirements.txt` добавлена библиотека `Pillow==10.3.0`. Это изменение сделано для установки библиотеки Pillow, которая необходима для работы с изображениями в Django.

### Объяснение:
**Поле ImageField в Django**:
Поле `ImageField` в Django используется для загрузки и хранения изображений. Оно позволяет пользователям загружать изображения через формы и сохранять их в указанной директории на сервере. Поле `ImageField` требует установки библиотеки Pillow для работы с изображениями.

**Библиотека Pillow**:
Pillow — это библиотека Python для работы с изображениями. Она предоставляет мощные инструменты для открытия, манипуляции и сохранения многих различных форматов изображений. Pillow необходима для работы с полем `ImageField` в Django.

**Как работает этот код**:
1. **Определение модели Article (news/models.py)**:
   - В модели `Article` добавлено новое поле `image`, которое является полем для загрузки изображений (`ImageField`). Поле использует параметр `upload_to='articles/'` для указания директории загрузки, `blank=True` для разрешения пустых значений и `null=True` для разрешения значений NULL в базе данных. Поле имеет метку `Изображение`.
2. **Установка библиотеки Pillow (requirements.txt)**:
   - В файл `requirements.txt` добавлена библиотека `Pillow==10.3.0`. Это необходимо для установки библиотеки Pillow, которая требуется для работы с изображениями в Django.

### Список используемых тегов и стилей с их описанием
1. **Django поля**:
   - `ImageField`: Поле для загрузки и хранения изображений.
   - `upload_to`: Параметр для указания директории загрузки изображений.
   - `blank=True`: Параметр для разрешения пустых значений в поле.
   - `null=True`: Параметр для разрешения значений NULL в базе данных.
   - `verbose_name`: Параметр для указания метки поля.
2. **Библиотека Pillow**:
   - `Pillow`: Библиотека Python для работы с изображениями.

**commit: `Урок 22: добавили поле для хранения изображений в статьях`**

1. **news/views.py**:
   - **Изменение обработки формы в функции add_article**: В функции `add_article` изменена обработка формы при методе POST. Теперь форма создается с использованием `request.POST` и `request.FILES`, что позволяет обрабатывать загрузку файлов. Это изменение сделано для поддержки загрузки изображений при добавлении статьи.
   - **Изменение сохранения статьи**: Удалены строки, которые вручную создавали объект `Article` и сохраняли его в базе данных. Теперь используется метод `form.save()`, который автоматически создает и сохраняет объект `Article` на основе данных формы. Это изменение сделано для упрощения кода и автоматического сохранения статьи в базе данных.
   - **Изменение перенаправления**: Изменен способ перенаправления пользователя после успешного сохранения статьи. Теперь используется функция `redirect` с именем маршрута `news:detail_article_by_id` и параметром `article_id=article.id`. Это изменение сделано для улучшения читаемости кода и использования именованных маршрутов.
   - **Изменение контекста**: Удалены лишние фигурные скобки в контексте. Теперь контекст создается с использованием словаря, что упрощает код и делает его более читаемым.

**Как работает этот код**:
1. **Определение функции add_article (news/views.py)**:
   - Функция `add_article` обрабатывает запросы на добавление новой статьи. Она проверяет метод запроса (POST или GET). Если метод POST, создается экземпляр формы `ArticleForm` с данными из запроса (`request.POST` и `request.FILES`), проверяется валидность данных формы и, при успешной валидации, создается и сохраняется объект `Article` с данными из формы. После сохранения статьи пользователь перенаправляется на страницу карточки новости. Если метод GET, создается пустой экземпляр формы `ArticleForm`. Контекст содержит форму и меню, и шаблон `add_article.html` рендерится с этим контекстом.
2. **Обработка загрузки файлов**:
   - В функции `add_article` теперь используется `request.FILES` для обработки загрузки файлов. Это позволяет пользователям загружать изображения при добавлении статьи.
3. **Автоматическое сохранение статьи**:
   - Вместо ручного создания и сохранения объекта `Article`, теперь используется метод `form.save()`, который автоматически создает и сохраняет объект `Article` на основе данных формы. Это упрощает код и делает его более читаемым.
4. **Перенаправление пользователя**:
   - После успешного сохранения статьи пользователь перенаправляется на страницу карточки новости с использованием функции `redirect` и именованного маршрута `news:detail_article_by_id`. Это улучшает читаемость кода и использование именованных маршрутов.
5. **Создание контекста**:
   - Контекст создается с использованием словаря, что упрощает код и делает его более читаемым.

**commit: `Урок 22: обновили представление add_article`**

1. **news/templates/news/delete_article.html**:
   - **Создание шаблона для удаления статьи**: Создан новый шаблон `delete_article.html`, который расширяет базовый шаблон и содержит форму для удаления статьи. Форма отправляется методом POST и содержит кнопку для подтверждения удаления и кнопку для отмены. Это изменение сделано для предоставления пользователям интерфейса для удаления статей.
2. **news/templates/news/edit_article.html**:
   - **Создание шаблона для редактирования статьи**: Создан новый шаблон `edit_article.html`, который расширяет базовый шаблон и содержит форму для редактирования статьи. Форма отправляется методом POST и содержит кнопку для сохранения изменений и кнопку для отмены. Это изменение сделано для предоставления пользователям интерфейса для редактирования статей.
3. **news/urls.py**:
   - **Добавление новых маршрутов**: Добавлены новые маршруты `path('edit/<int:article_id>/', views.article_update, name='article_update')` и `path('delete/<int:article_id>/', views.article_delete, name='article_delete')` для обработки запросов на редактирование и удаление статей соответственно. Это изменение сделано для поддержки новой функциональности редактирования и удаления статей.
4. **news/views.py**:
   - **Добавление функции article_update**: Добавлена новая функция `article_update`, которая обрабатывает запросы на редактирование статьи. Функция проверяет метод запроса (POST или GET). Если метод POST, создается экземпляр формы `ArticleForm` с данными из запроса (`request.POST` и `request.FILES`) и экземпляром статьи, проверяется валидность данных формы и, при успешной валидации, сохраняется экземпляр статьи. После сохранения статьи пользователь перенаправляется на страницу карточки новости. Если метод GET, создается экземпляр формы `ArticleForm` с экземпляром статьи. Контекст содержит форму и статью, и шаблон `edit_article.html` рендерится с этим контекстом.
   - **Добавление функции article_delete**: Добавлена новая функция `article_delete`, которая обрабатывает запросы на удаление статьи. Функция проверяет метод запроса (POST или GET). Если метод POST, удаляется экземпляр статьи и пользователь перенаправляется на страницу каталога новостей. Если метод GET, рендерится шаблон `delete_article.html` с контекстом, содержащим статью.

**Как работает этот код**:
1. **Шаблон для удаления статьи (news/templates/news/delete_article.html)**:
   - Шаблон `delete_article.html` расширяет базовый шаблон и содержит форму для удаления статьи. Форма отправляется методом POST и содержит кнопку для подтверждения удаления и кнопку для отмены. Шаблон использует тег `{% csrf_token %}` для защиты от CSRF-атак.
2. **Шаблон для редактирования статьи (news/templates/news/edit_article.html)**:
   - Шаблон `edit_article.html` расширяет базовый шаблон и содержит форму для редактирования статьи. Форма отправляется методом POST и содержит кнопку для сохранения изменений и кнопку для отмены. Шаблон использует тег `{% csrf_token %}` для защиты от CSRF-атак.
3. **Маршруты для редактирования и удаления статьи (news/urls.py)**:
   - Добавлены новые маршруты `path('edit/<int:article_id>/', views.article_update, name='article_update')` и `path('delete/<int:article_id>/', views.article_delete, name='article_delete')` для обработки запросов на редактирование и удаление статей соответственно. Маршруты связывают URL `/edit/<int:article_id>/` и `/delete/<int:article_id>/` с представлениями `article_update` и `article_delete` соответственно.
4. **Представление для редактирования статьи (news/views.py)**:
   - Функция `article_update` обрабатывает запросы на редактирование статьи. Она проверяет метод запроса (POST или GET). Если метод POST, создается экземпляр формы `ArticleForm` с данными из запроса (`request.POST` и `request.FILES`) и экземпляром статьи, проверяется валидность данных формы и, при успешной валидации, сохраняется экземпляр статьи. После сохранения статьи пользователь перенаправляется на страницу карточки новости. Если метод GET, создается экземпляр формы `ArticleForm` с экземпляром статьи. Контекст содержит форму и статью, и шаблон `edit_article.html` рендерится с этим контекстом.
5. **Представление для удаления статьи (news/views.py)**:
   - Функция `article_delete` обрабатывает запросы на удаление статьи. Она проверяет метод запроса (POST или GET). Если метод POST, удаляется экземпляр статьи и пользователь перенаправляется на страницу каталога новостей. Если метод GET, рендерится шаблон `delete_article.html` с контекстом, содержащим статью.

### Список используемых тегов и стилей с их описанием
1. **HTML теги**:
   - `<form>`: Форма для отправки данных.
   - `<input>`: Поле ввода для формы.
   - `<button>`: Кнопка для отправки формы.
   - `<h1>`: Заголовок первого уровня.
   - `<div>`: Контейнер для группировки элементов.
   - `<a>`: Гиперссылка.
   - `{% csrf_token %}`: Тег для защиты от CSRF-атак.
   - `{% extends "base.html" %}`: Тег для расширения базового шаблона.
   - `{% block content %}`: Тег для определения блока контента.
   - `{% endblock %}`: Тег для завершения блока контента.
2. **Bootstrap классы**:
   - `btn btn-danger`: Стиль для кнопки удаления.
   - `btn btn-secondary`: Стиль для кнопки отмены.
   - `btn btn-primary`: Стиль для кнопки сохранения.
   - `mt-3`: Отступ сверху.

**commit: `Урок 22: добавили формы для редактирования и удаления статей`**

1. **news/templates/news/article_detail.html**:
   - **Добавление контейнера для кнопок редактирования и удаления**: Добавлен новый контейнер `<div class="mt-4 border-top pt-3">` для размещения кнопок редактирования и удаления статьи. Это изменение сделано для улучшения структуры страницы и удобства пользователей.
   - **Добавление кнопки редактирования**: Добавлена кнопка `<a href="{% url 'news:article_update' article.id %}" class="btn btn-warning">` для редактирования статьи. Кнопка содержит иконку `<i class="bi bi-pencil-square"></i>` и текст "Редактировать". Это изменение сделано для предоставления пользователям возможности редактировать статью.
   - **Добавление кнопки удаления**: Добавлена кнопка `<a href="{% url 'news:article_delete' article.id %}" class="btn btn-danger">` для удаления статьи. Кнопка содержит иконку `<i class="bi bi-trash"></i>` и текст "Удалить". Это изменение сделано для предоставления пользователям возможности удалять статью.

**Как работает этот код**:
1. **Шаблон для отображения статьи (news/templates/news/article_detail.html)**:
   - Шаблон `article_detail.html` расширяет базовый шаблон и содержит информацию о статье. В шаблоне добавлен новый контейнер `<div class="mt-4 border-top pt-3">` для размещения кнопок редактирования и удаления статьи.
   - Добавлена кнопка `<a href="{% url 'news:article_update' article.id %}" class="btn btn-warning">` для редактирования статьи. Кнопка содержит иконку `<i class="bi bi-pencil-square"></i>` и текст "Редактировать".
   - Добавлена кнопка `<a href="{% url 'news:article_delete' article.id %}" class="btn btn-danger">` для удаления статьи. Кнопка содержит иконку `<i class="bi bi-trash"></i>` и текст "Удалить".

### Список используемых тегов и стилей с их описанием
1. **HTML теги**:
   - `<div>`: Контейнер для группировки элементов.
   - `<a>`: Гиперссылка для навигации.
   - `<i>`: Иконка для визуального оформления.
   - `{% csrf_token %}`: Тег для защиты от CSRF-атак.
   - `{% extends "base.html" %}`: Тег для расширения базового шаблона.
   - `{% block content %}`: Тег для определения блока контента.
   - `{% endblock %}`: Тег для завершения блока контента.
   - `{% include "include/search_form.html" %}`: Тег для включения другого шаблона.

2. **Bootstrap классы**:
   - `mt-4`: Отступ сверху.
   - `border-top`: Граница сверху.
   - `pt-3`: Внутренний отступ сверху.
   - `btn btn-warning`: Стиль для кнопки редактирования.
   - `btn btn-danger`: Стиль для кнопки удаления.
   - `bi bi-pencil-square`: Иконка карандаша для редактирования.
   - `bi bi-trash`: Иконка корзины для удаления.

**commit: `Урок 22: добавили кнопки удаления и редактирования на странице статей`**

- Настроили пути для медиа-файлов
- Добавили обработку медиа в режиме разработки

**commit: `Урок 22: добавили папку /media/articles`**

1. **news/forms.py**:
   - **Добавление поля image в Meta**: В классе `Meta` формы `ArticleForm` добавлено поле `image` и виджет `ClearableFileInput` для загрузки изображений. Это изменение сделано для того, чтобы пользователи могли загружать изображения при добавлении статьи.
2. **news/models.py**:
   - **Изменение параметра upload_to поля image**: В поле `image` модели `Article` изменен параметр `upload_to` на `'articles/%Y/%m/%d/'`, чтобы изображения сохранялись в директории с подкаталогами по году, месяцу и дню. Это изменение сделано для улучшения организации загруженных изображений.
3. **news/templates/news/add_article.html**:
   - **Изменение структуры шаблона**: Удалены лишние контейнеры и добавлены новые элементы для улучшения структуры и визуального оформления шаблона.
   - **Добавление поля для загрузки изображения**: Добавлено поле для загрузки изображения с использованием виджета `ClearableFileInput`. Это изменение сделано для того, чтобы пользователи могли загружать изображения при добавлении статьи.
   - **Добавление кнопок "Опубликовать" и "Отмена"**: Добавлены кнопки "Опубликовать" и "Отмена" для улучшения пользовательского опыта.
4. **news/templates/news/article_detail.html**:
   - **Изменение структуры шаблона**: Удалены лишние контейнеры и добавлены новые элементы для улучшения структуры и визуального оформления шаблона.
   - **Добавление отображения изображения**: Добавлено отображение изображения статьи, если оно существует. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Добавление кнопок управления**: Добавлены кнопки для редактирования и удаления статьи для улучшения пользовательского опыта.
5. **news/templatetags/customtags.py**:
   - **Добавление фильтра basename**: Добавлен новый фильтр `basename`, который возвращает имя файла без пути. Это изменение сделано для улучшения отображения имен файлов в шаблонах.

### Как это работает:
1. **Определение формы (news/forms.py)**:
   - Форма `ArticleForm` определена с использованием класса `forms.ModelForm`. Она содержит поля `title`, `content`, `category`, `tags` и `image`. Поле `image` использует виджет `ClearableFileInput` для загрузки изображений. Это изменение сделано для того, чтобы пользователи могли загружать изображения при добавлении статьи.
2. **Определение модели (news/models.py)**:
   - В модели `Article` поле `image` использует параметр `upload_to='articles/%Y/%m/%d/'` для сохранения изображений в директории с подкаталогами по году, месяцу и дню. Это изменение сделано для улучшения организации загруженных изображений.
3. **Шаблон для добавления статьи (news/templates/news/add_article.html)**:
   - Шаблон `add_article.html` расширяет базовый шаблон и содержит форму для добавления новой статьи. Форма отправляется методом POST и содержит кнопки "Опубликовать" и "Отмена". Шаблон использует тег `{% csrf_token %}` для защиты от CSRF-атак.
   - Добавлено поле для загрузки изображения с использованием виджета `ClearableFileInput`. Это изменение сделано для того, чтобы пользователи могли загружать изображения при добавлении статьи.
4. **Шаблон для отображения статьи (news/templates/news/article_detail.html)**:
   - Шаблон `article_detail.html` расширяет базовый шаблон и содержит информацию о статье. В шаблоне добавлено отображение изображения статьи, если оно существует. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - Добавлены кнопки для редактирования и удаления статьи для улучшения пользовательского опыта.
5. **Фильтр basename (news/templatetags/customtags.py)**:
   - Добавлен новый фильтр `basename`, который возвращает имя файла без пути. Это изменение сделано для улучшения отображения имен файлов в шаблонах.

### Список используемых тегов и стилей с их описанием
1. **HTML теги**:
   - `<div>`: Контейнер для группировки элементов.
   - `<a>`: Гиперссылка для навигации.
   - `<i>`: Иконка для визуального оформления.
   - `<form>`: Форма для отправки данных.
   - `<input>`: Поле ввода для формы.
   - `<button>`: Кнопка для отправки формы.
   - `<h1>`: Заголовок первого уровня.
   - `<img>`: Изображение.
   - `<small>`: Мелкий текст для отображения дополнительной информации.
   - `{% csrf_token %}`: Тег для защиты от CSRF-атак.
   - `{% extends "base.html" %}`: Тег для расширения базового шаблона.
   - `{% block content %}`: Тег для определения блока контента.
   - `{% endblock %}`: Тег для завершения блока контента.
   - `{% include "include/search_form.html" %}`: Тег для включения другого шаблона.
   - `{% for field in form %}`: Тег для цикла по полям формы.
   - `{% endfor %}`: Тег для завершения цикла.
   - `{% if field.errors %}`: Тег для условия проверки наличия ошибок у поля.
   - `{% endif %}`: Тег для завершения условия.
2. **Bootstrap классы**:
   - `container`: Контейнер для центрирования содержимого.
   - `mt-4`: Отступ сверху.
   - `mb-4`: Отступ снизу.
   - `mb-5`: Отступ снизу.
   - `display-4`: Размер заголовка.
   - `text-muted`: Цвет текста (приглушенный).
   - `text-center`: Выравнивание текста по центру.
   - `img-fluid`: Отзывчивое изображение.
   - `rounded-3`: Закругленные углы.
   - `shadow`: Тень.
   - `loading="lazy"`: Ленивая загрузка изображения.
   - `btn btn-warning`: Стиль для кнопки редактирования.
   - `btn btn-danger`: Стиль для кнопки удаления.
   - `btn btn-primary`: Стиль для кнопки "Опубликовать".
   - `btn btn-secondary`: Стиль для кнопки "Отмена".
   - `btn btn-outline-primary`: Стиль для кнопки категории.
   - `btn btn-outline-secondary`: Стиль для кнопки тега.
   - `btn-sm`: Маленькая кнопка.
   - `d-flex`: Флексбокс для горизонтального выравнивания.
   - `flex-wrap`: Перенос элементов на новую строку.
   - `gap-2`: Отступ между элементами.
   - `form-group`: Группа полей формы.
   - `form-label`: Метка поля формы.
   - `form-control-file`: Стиль для поля загрузки файла.
   - `custom-file`: Стиль для пользовательского поля загрузки файла.
   - `custom-file-label`: Стиль для метки пользовательского поля загрузки файла.
   - `form-text`: Текст для описания поля формы.
   - `alert alert-danger`: Стиль для отображения ошибок.
   - `bi bi-pencil-square`: Иконка карандаша для редактирования.
   - `bi bi-trash`: Иконка корзины для удаления.
   - `bi bi-save`: Иконка сохранения.
   - `bi bi-x-circle`: Иконка отмены.
   - `bi bi-bookmark`: Иконка закладки.
   - `bi bi-tag`: Иконка тега.

**commit: `Урок 22: добавили возможность добавления картинки к новости`**


## Урок 23

1. **news/templates/news/add_article.html**:
   - **Добавление формы для загрузки JSON-файла**: Добавлена новая форма для загрузки JSON-файла. Форма отправляется методом POST и содержит поле для выбора файла и кнопку для загрузки. Это изменение сделано для предоставления пользователям возможности загружать статьи из JSON-файла.
2. **news/urls.py**:
   - **Добавление нового маршрута для загрузки JSON-файла**: Добавлен новый маршрут `path('upload_json/', views.upload_json, name='upload_json')` для обработки запросов на загрузку JSON-файла. Это изменение сделано для поддержки новой функциональности загрузки статей из JSON-файла.
3. **news/views.py**:
   - **Импорт модулей**: Добавлены импорты модулей `json`, `unidecode`, `models` и `slugify`. Эти модули необходимы для работы с JSON-файлами и генерации уникальных слагов.
   - **Добавление функции upload_json**: Добавлена новая функция `upload_json`, которая обрабатывает запросы на загрузку JSON-файла. Функция проверяет метод запроса (POST) и наличие файла в запросе. Если файл существует, он загружается и обрабатывается. Данные из файла загружаются и создаются новые статьи с уникальными слагами. Также добавляются теги к статьям. Если файл не является корректным JSON, возвращается ошибка. Это изменение сделано для реализации функциональности загрузки статей из JSON-файла.

### Объяснение, для чего нужны эти изменения и как работает этот код
**Загрузка JSON-файла**:
Загрузка JSON-файла позволяет пользователям легко добавлять несколько статей одновременно, используя данные в формате JSON. Это упрощает процесс добавления статей и позволяет быстро заполнить базу данных большим количеством статей.

**Как работает этот код**:
1. **Шаблон для добавления статьи (news/templates/news/add_article.html)**:
   - В шаблоне `add_article.html` добавлена новая форма для загрузки JSON-файла. Форма отправляется методом POST и содержит поле для выбора файла и кнопку для загрузки. Шаблон использует тег `{% csrf_token %}` для защиты от CSRF-атак.
2. **Маршрут для загрузки JSON-файла (news/urls.py)**:
   - Добавлен новый маршрут `path('upload_json/', views.upload_json, name='upload_json')` для обработки запросов на загрузку JSON-файла. Маршрут связывает URL `/upload_json/` с представлением `upload_json`.
3. **Представление для загрузки JSON-файла (news/views.py)**:
   - Функция `upload_json` обрабатывает запросы на загрузку JSON-файла. Она проверяет метод запроса (POST) и наличие файла в запросе. Если файл существует, он загружается и обрабатывается. Данные из файла загружаются и создаются новые статьи с уникальными слагами. Также добавляются теги к статьям. Если файл не является корректным JSON, возвращается ошибка.

**Почему сначала создаётся статья, а только потом добавляются теги**:
Сначала создаётся статья, чтобы получить её идентификатор и уникальный слаг. После этого теги добавляются к уже созданной статье. Это позволяет избежать проблем с целостностью данных и обеспечивает корректное связывание данных в базе данных.

**commit: `Урок 23: добавили возможность добавления нескольких статей из json-файла`**

### Обзор изменений
1. **Создание формы для валидации данных из JSON-файла.**
2. **Обновление представления `upload_json` для использования этой формы.**
3. **Обновление шаблона для отображения сообщений об ошибках.**

### Подробное объяснение
#### 1. Создание формы для валидации данных из JSON-файла
Создана форма `ArticleUploadForm`, которая включает поле для загрузки JSON-файла и методы для валидации данных из этого файла.
- **`json_file`**: Поле для загрузки JSON-файла.
- **`clean_json_file`**: Метод для валидации загруженного файла. Проверяет, что файл имеет расширение `.json`.
- **`validate_json_data`**: Метод для валидации данных из JSON-файла. Проверяет, что категории и теги, указанные в файле, существуют в базе данных. Если категория или тег не существует, добавляет сообщение об ошибке в список `errors`.

#### 2. Обновление представления `upload_json` для использования этой формы
Обновлено представление `upload_json`, чтобы использовать форму `ArticleUploadForm` для валидации данных из JSON-файла.
- **`upload_json`**: Представление для обработки загрузки JSON-файла.
  - Проверяет, что запрос является POST-запросом.
  - Использует форму `ArticleUploadForm` для валидации загруженного файла.
  - Если файл валиден, загружает данные из файла и вызывает метод `validate_json_data` для валидации данных.
  - Если есть ошибки валидации, отображает их пользователю.
  - Если данные валидны, создает новые статьи и добавляет к ним теги.

#### 3. Обновление шаблона для отображения сообщений об ошибках
Обновлён шаблон `add_article.html`, чтобы отображать сообщения об ошибках, если категория или тег не существует.
- **`add_article.html`**: Шаблон для добавления новой статьи.
  - Отображает форму для загрузки JSON-файла.
  - Если есть ошибки валидации, отображает их пользователю.
  - Отображает форму для добавления новой статьи.

**commit: `Урок 23: валидация категорий и тегов`**

1. **news/forms.py**:
   - **Изменение виджетов и меток полей формы ArticleForm**: В форме `ArticleForm` изменены виджеты и метки полей `title`, `content`, `category` и `image`. Эти изменения сделаны для улучшения пользовательского опыта и удобства заполнения формы.
   - **Добавление формы ArticleUploadForm**: Добавлена новая форма `ArticleUploadForm` для загрузки JSON-файла. Форма содержит поле `json_file` с виджетом `FileInput` и меткой "Загрузить JSON-файл". Это изменение сделано для предоставления пользователям возможности загружать статьи из JSON-файла.
2. **news/templates/news/add_article.html**:
   - **Изменение структуры шаблона**: Удалены лишние контейнеры и добавлены новые элементы для улучшения структуры и визуального оформления шаблона.
   - **Добавление формы для загрузки JSON-файла**: Добавлена новая форма для загрузки JSON-файла. Форма отправляется методом POST и содержит поле для выбора файла и кнопку для загрузки. Это изменение сделано для предоставления пользователям возможности загружать статьи из JSON-файла.
   - **Изменение отображения полей формы**: В цикле `{% for field in form %}` изменено отображение полей формы. Теперь каждое поле отображается в элементе `<div class="mb-3">` с меткой и самим полем. Если у поля есть ошибки, они отображаются в элементе `<div class="alert alert-danger mt-2">`. Это изменение сделано для улучшения визуального оформления и удобства пользователей.
   - **Добавление кнопок "Опубликовать" и "Отмена"**: Добавлены кнопки "Опубликовать" и "Отмена" для улучшения пользовательского опыта.
3. **templates/base.html**:
   - **Добавление стилей для тегов**: Добавлены новые стили для тегов. Эти стили используются для улучшения визуального оформления тегов в шаблонах.

**Как работает этот код**:
1. **Определение формы (news/forms.py)**:
   - Форма `ArticleForm` определена с использованием класса `forms.ModelForm`. Она содержит поля `title`, `content`, `category`, `tags` и `image`. Поля используют виджеты для улучшения пользовательского опыта и удобства заполнения формы.
   - Форма `ArticleUploadForm` содержит поле `json_file` с виджетом `FileInput` и меткой "Загрузить JSON-файл". Это позволяет пользователям загружать статьи из JSON-файла.
2. **Шаблон для добавления статьи (news/templates/news/add_article.html)**:
   - Шаблон `add_article.html` расширяет базовый шаблон и содержит форму для добавления новой статьи. Форма отправляется методом POST и содержит кнопки "Опубликовать" и "Отмена". Шаблон использует тег `{% csrf_token %}` для защиты от CSRF-атак.
   - В шаблоне добавлена новая форма для загрузки JSON-файла. Форма отправляется методом POST и содержит поле для выбора файла и кнопку для загрузки.
   - В цикле `{% for field in form %}` изменено отображение полей формы. Теперь каждое поле отображается в элементе `<div class="mb-3">` с меткой и самим полем. Если у поля есть ошибки, они отображаются в элементе `<div class="alert alert-danger mt-2">`.
3. **Базовый шаблон (templates/base.html)**:
   - В базовый шаблон добавлены новые стили для тегов. Эти стили используются для улучшения визуального оформления тегов в шаблонах.

### Список используемых тегов и стилей с их описанием
1. **HTML теги**:
   - `<form>`: Форма для отправки данных.
   - `<input>`: Поле ввода для формы.
   - `<button>`: Кнопка для отправки формы.
   - `<label>`: Метка для поля формы.
   - `<div>`: Контейнер для группировки элементов.
   - `<i>`: Иконка для визуального оформления.
   - `{% csrf_token %}`: Тег для защиты от CSRF-атак.
   - `{% extends "base.html" %}`: Тег для расширения базового шаблона.
   - `{% block content %}`: Тег для определения блока контента.
   - `{% endblock %}`: Тег для завершения блока контента.
   - `{% for field in form %}`: Тег для цикла по полям формы.
   - `{% endfor %}`: Тег для завершения цикла.
   - `{% if field.errors %}`: Тег для условия проверки наличия ошибок у поля.
   - `{% endif %}`: Тег для завершения условия.

2. **Bootstrap классы**:
   - `form-group`: Группа полей формы.
   - `form-label`: Метка поля формы.
   - `form-control`: Стиль для текстового поля.
   - `form-select`: Стиль для выпадающего списка.
   - `form-control-file`: Стиль для поля загрузки файла.
   - `btn btn-success`: Стиль для кнопки загрузки.
   - `mt-2`: Отступ сверху.
   - `mt-4`: Отступ сверху.
   - `mb-3`: Отступ снизу.
   - `alert alert-danger`: Стиль для отображения ошибок.
   - `bi bi-upload`: Иконка загрузки.
   - `fw-bold`: Жирный шрифт.
   - `d-grid`: Флексбокс для горизонтального выравнивания.
   - `gap-2`: Отступ между элементами.
   - `d-md-flex`: Флексбокс для горизонтального выравнивания на средних и больших экранах.
   - `justify-content-md-end`: Выравнивание элементов по правому краю на средних и больших экранах.

3. **CSS стили**:
   - `.tag-list`: Стиль для списка тегов.
   - `.tag-item`: Стиль для элемента тега.
   - `background-color`: Цвет фона.
   - `border`: Граница.
   - `border-radius`: Закругленные углы.
   - `padding`: Внутренний отступ.
   - `font-size`: Размер шрифта.

**commit: `Урок 23: поправили вёрстку и стиль формы добавления статьи`**

#### Изменения в файле `news/forms.py`
##### Улучшение сообщений об ошибках
- **Изменение:** Обновлены сообщения об ошибках для категорий и тегов.
- **Цель:** Улучшение пользовательского опыта путем предоставления более информативных сообщений об ошибках.
- **Как работает:** В форме загрузки статьи теперь выводятся более детальные сообщения об ошибках, указывающие на несуществующие категории или теги и предлагающие варианты исправления.

#### Изменения в файле `news/models.py`
##### Обновление метода `save`
- **Изменение:** Удалены строки, связанные с отладочными сообщениями и повторным сохранением статьи. Добавлены строки для генерации уникального `slug`.
- **Цель:** Оптимизация процесса сохранения статьи и генерации уникального `slug`.
- **Как работает:** Теперь метод `save` генерирует уникальный `slug` на основе заголовка статьи и проверяет его уникальность перед сохранением. Это предотвращает дублирование `slug` и улучшает SEO.

#### Изменения в файле `news/templates/news/upload_json.html`
##### Создание нового шаблона для загрузки JSON-файла
- **Изменение:** Добавлен новый шаблон для загрузки JSON-файла.
- **Цель:** Предоставление пользовательского интерфейса для загрузки новостей из JSON-файла.
- **Как работает:** Новый шаблон включает форму для загрузки JSON-файла и отображение ошибок, если они возникают при загрузке.

#### Изменения в файле `news/urls.py`
##### Удаление комментария
- **Изменение:** Удален комментарий, связанный с новым URL для загрузки JSON-файла.
- **Цель:** Очистка кода от ненужных комментариев.
- **Как работает:** Удаление комментария не влияет на функциональность, но делает код чище.

#### Изменения в файле `news/views.py`
##### Обновление представления `upload_json`
- **Изменение:** Обновлен шаблон, используемый для отображения формы загрузки JSON-файла.
- **Цель:** Использование специализированного шаблона для загрузки JSON-файла.
- **Как работает:** Теперь представление `upload_json` использует шаблон `news/upload_json.html` для отображения формы и ошибок.

##### Обновление представления `add_article`
- **Изменение:** Обновлен метод сохранения статьи и контекст, передаваемый в шаблон.
- **Цель:** Улучшение процесса сохранения статьи и генерации `slug`.
- **Как работает:** Теперь статья сохраняется с использованием `commit=False`, чтобы сначала сгенерировать `slug`, а затем сохранить статью. Контекст, передаваемый в шаблон, упрощен.

### Общее объяснение работы кода
1. **Форма загрузки статьи (`news/forms.py`):**
   - Проверяет наличие категорий и тегов в загружаемой статье.
   - Обновленные сообщения об ошибках помогают пользователям исправить несуществующие категории или теги.
2. **Модель статьи (`news/models.py`):**
   - Метод `save` генерирует уникальный `slug` на основе заголовка статьи.
   - Проверяет уникальность `slug` перед сохранением статьи, чтобы избежать дублирования.
3. **Шаблон загрузки JSON-файла (`news/templates/news/upload_json.html`):**
   - Предоставляет интерфейс для загрузки новостей из JSON-файла.
   - Отображает ошибки, если они возникают при загрузке.
4. **Маршруты (`news/urls.py`):**
   - Определяет URL-адреса для различных действий, связанных с новостями, включая загрузку JSON-файла.
5. **Представления (`news/views.py`):**
   - Обрабатывает запросы на загрузку JSON-файла и добавление статьи.
   - Использует специализированные шаблоны для отображения форм и ошибок.
   - Оптимизирует процесс сохранения статьи и генерации `slug`.

**commit: `Урок 23: разделили одиночное и потоковое добавление статей`**

### Изменения в файле `news/templates/news/add_article.html`
#### Обновление заголовка и добавление кнопки загрузки JSON
- **Изменение:** Обновлен заголовок и добавлена кнопка для загрузки новостей из JSON-файла.
- **Цель:** Улучшение пользовательского интерфейса и предоставление возможности загрузки новостей из JSON-файла.
- **Как работает:** Теперь на странице добавления статьи есть кнопка для перехода к загрузке новостей из JSON-файла.

#### Удаление формы загрузки JSON-файла
- **Изменение:** Удалена форма для загрузки JSON-файла.
- **Цель:** Упрощение шаблона и перенос функциональности загрузки JSON-файла в отдельный шаблон.
- **Как работает:** Форма для загрузки JSON-файла была удалена из этого шаблона, чтобы упростить его и перенести функциональность в другой шаблон.

#### Обновление отображения тегов
- **Изменение:** Теги теперь отображаются в два столбца.
- **Цель:** Улучшение визуального отображения тегов для лучшей читаемости.
- **Как работает:** Теги теперь отображаются в два столбца, что делает их более удобными для чтения и редактирования.

### Изменения в файле `news/templates/news/edit_article_from_json.html`
#### Создание нового шаблона для редактирования статьи из JSON
- **Изменение:** Добавлен новый шаблон для редактирования статьи из JSON-файла.
- **Цель:** Предоставление пользовательского интерфейса для редактирования статьи из JSON-файла.
- **Как работает:** Новый шаблон включает форму для редактирования статьи и отображение ошибок, если они возникают при редактировании.

### Изменения в файле `news/templatetags/customtags.py`
#### Добавление фильтра `add`
- **Изменение:** Добавлен новый фильтр `add` для сложения двух чисел.
- **Цель:** Упрощение вычислений в шаблонах.
- **Как работает:** Фильтр `add` позволяет сложить два числа в шаблоне, что упрощает вычисления и делает код более читаемым.

### Изменения в файле `news/urls.py`
#### Обновление URL для загрузки JSON-файла
- **Изменение:** Обновлен URL для загрузки JSON-файла и добавлен новый URL для редактирования статьи из JSON.
- **Цель:** Предоставление отдельных URL для загрузки и редактирования статьи из JSON-файла.
- **Как работает:** Теперь есть отдельные URL для загрузки JSON-файла и редактирования статьи из JSON, что упрощает маршрутизацию и управление статьями.

### Изменения в файле `news/views.py`
#### Обновление представления `upload_json`
- **Изменение:** Обновлено представление для загрузки JSON-файла и добавлено новое представление для редактирования статьи из JSON.
- **Цель:** Улучшение функциональности загрузки и редактирования статьи из JSON-файла.
- **Как работает:** Теперь представление `upload_json_view` сохраняет данные в сессию для последовательного просмотра и редактирования статьи. Новое представление `edit_article_from_json` позволяет редактировать статью из JSON-файла.

#### Обновление представления `add_article`
- **Изменение:** Обновлен метод сохранения статьи и добавлена функция `save_article` для сохранения статьи.
- **Цель:** Улучшение процесса сохранения статьи и генерации `slug`.
- **Как работает:** Теперь статья сохраняется с использованием функции `save_article`, которая генерирует уникальный `slug` и сохраняет статью.

### Общее объяснение работы кода
1. **Шаблон добавления статьи (`news/templates/news/add_article.html`):**
   - Предоставляет интерфейс для добавления новой статьи.
   - Обновления включают добавление кнопки для загрузки новостей из JSON-файла и улучшение отображения тегов.
2. **Шаблон редактирования статьи из JSON (`news/templates/news/edit_article_from_json.html`):**
   - Предоставляет интерфейс для редактирования статьи из JSON-файла.
   - Включает форму для редактирования статьи и отображение ошибок.
3. **Фильтры шаблонов (`news/templatetags/customtags.py`):**
   - Предоставляет пользовательские фильтры для использования в шаблонах.
   - Новый фильтр `add` упрощает вычисления в шаблонах.
4. **Представления (`news/views.py`):**
   - Обрабатывает запросы на загрузку JSON-файла, добавление статьи и редактирование статьи из JSON-файла.
   - Использует функцию `save_article` для сохранения статьи и генерации уникального `slug`.

**commit: `Урок 23: потоковое добавление статей теперь поддерживает редактирование`**

- файл для потоковой загрузки новостей (может понадобиться добавление новых тегов и категорий)

**commit: `Урок 23: файл с новостями`**


## Урок 24

**Объяснение изменений:**
Переписали функцию `get_all_news` на классовое представление `GetAllNewsView`, используя базовый класс `View`. Это позволяет структурировать код и улучшить его читаемость.

**Назначение `View`:**
`View` является базовым классом для всех классовых представлений в `Django`. Он предоставляет основные методы для обработки `HTTP`-запросов.

**Параметры и методы `View`:**
- `http_method_names`: Список `HTTP`-методов, которые поддерживает представление.
- `dispatch(request, *args, **kwargs)`: Основной метод, который вызывается для обработки запроса. Он определяет, какой метод (`get`, `post`, и т.д.) вызвать на основе `HTTP`-метода запроса.
- `get(request, *args, **kwargs)`: Метод для обработки `GET`-запросов.
- `post(request, *args, **kwargs)`: Метод для обработки `POST`-запросов.
- `put(request, *args, **kwargs)`: Метод для обработки `PUT`-запросов.
- `delete(request, *args, **kwargs)`: Метод для обработки `DELETE`-запросов.
- `head(request, *args, **kwargs)`: Метод для обработки `HEAD`-запросов.
- `options(request, *args, **kwargs)`: Метод для обработки `OPTIONS`-запросов.
- `trace(request, *args, **kwargs)`: Метод для обработки `TRACE`-запросов.

**commit: `Урок 24: get_all_news -> GetAllNewsView(View)`**

**Объяснение изменений:**
Переписали представление `GetAllNewsView` на `ListView`, что упрощает работу с объектами моделей и уменьшает количество кода.

**Назначение `ListView`:**
`ListView` используется для отображения списка объектов модели. Он предоставляет встроенные механизмы для пагинации и сортировки.

**Параметры и методы `ListView`:**
- `model`: Модель, с которой работает представление.
- `queryset`: Набор запросов, который будет использоваться для получения объектов.
- `template_name`: Имя шаблона, который будет использоваться для рендеринга.
- `context_object_name`: Имя переменной контекста, которая будет использоваться в шаблоне.
- `paginate_by`: Количество объектов на странице для пагинации.
- `get_queryset(self)`: Метод для получения набора запросов.
- `get_context_data(self, **kwargs)`: Метод для получения данных контекста.

**commit: `Урок 24: GetAllNewsView(View) -> GetAllNewsView(ListView)`**

**Объяснение изменений:**
Переписали представление `edit_article_from_json` на `FormView`, что упрощает работу с формами и уменьшает количество кода.

**Назначение `FormView`:**
`FormView` используется для отображения и обработки форм. Он предоставляет встроенные методы для валидации форм и обработки данных.

**Параметры и методы `FormView`:**
- `form_class`: Класс формы, который будет использоваться.
- `template_name`: Имя шаблона, который будет использоваться для рендеринга.
- `success_url`: `URL`, на который будет перенаправлен пользователь после успешной отправки формы.
- `form_valid(self, form)`: Метод, который вызывается, если форма прошла валидацию.
- `form_invalid(self, form)`: Метод, который вызывается, если форма не прошла валидацию.
- `get_form_kwargs(self)`: Метод для получения аргументов для инициализации формы.

**commit: `Урок 24: edit_article_from_json -> EditArticleFromJsonView(FormView)`**

**Объяснение изменений:**
Переписали представление `MainView` на `TemplateView`, что упрощает рендеринг шаблонов без необходимости обработки данных.

**Назначение `TemplateView`:**
`TemplateView` используется для рендеринга шаблонов без необходимости обработки данных. Он предоставляет встроенные методы для рендеринга шаблонов.

**Параметры и методы `TemplateView`:**
- `template_name`: Имя шаблона, который будет использоваться для рендеринга.
- `get_context_data(self, **kwargs)`: Метод для получения данных контекста.
 
**commit: `Урок 24: main -> MainView(TemplateView)`**

**Объяснение изменений:**
Переписали функцию `get_detail_article_by_id` на классовое представление `ArticleDetailView`, используя `DetailView`. Это позволяет структурировать код и улучшить его читаемость.

**Назначение `DetailView`:**
`DetailView` используется для отображения детальной информации об одном объекте модели. Он предоставляет встроенные методы для получения объекта и рендеринга шаблона.

**Параметры и методы `DetailView`:**
- `model`: Модель, с которой работает представление.
- `template_name`: Имя шаблона, который будет использоваться для рендеринга.
- `context_object_name`: Имя переменной контекста, которая будет использоваться в шаблоне.
- `get_object(self, queryset=None)`: Метод для получения объекта.
- `get_context_data(self, **kwargs)`: Метод для получения данных контекста.

**commit: `Урок 24: get_detail_article_by_id -> ArticleDetailView(DetailView)`**

**Объяснение изменений:**
Переписали представление `about` на `AboutView`, что упрощает рендеринг шаблонов без необходимости обработки данных.
 
**commit: `Урок 24: about -> AboutView(TemplateView)`**

**Объяснение изменений:**
Переписали представление `get_news_by_category` на `ListView`, что упрощает работу с объектами моделей и уменьшает количество кода.

**commit: `Урок 24: get_news_by_category -> GetNewsByCategoryView(ListView)`**

**Объяснение изменений:**
Переписали представление `get_news_by_tag` на `ListView`, что упрощает работу с объектами моделей и уменьшает количество кода.

**commit: `Урок 24: get_news_by_tag -> GetNewsByTagView(ListView)`**

**Объяснение изменений:**
Переписали представление `search_news` на `ListView`, что упрощает работу с объектами моделей и уменьшает количество кода.

**commit: `Урок 24: search_news -> SearchNewsView(ListView)`**

**Объяснение изменений:**
Переписали представление `toggle_favorite` на `View`, что упрощает работу с объектами моделей и уменьшает количество кода.

**commit: `Урок 24: toggle_favorite -> ToggleFavoriteView(View)`**

**Объяснение изменений:**
Переписали представление `toggle_like` на `ListView`, что упрощает работу с объектами моделей и уменьшает количество кода.

**commit: `Урок 24: toggle_like -> ToggleLikeView(ListView)`**

**Объяснение изменений:**
Переписали представление `favorites` на `ListView`, что упрощает работу с объектами моделей и уменьшает количество кода.

**commit: `Урок 24: favorites -> FavoritesView(ListView)`**

**Объяснение изменений:**
Переписали представление `upload_json_view` на `FormView`, что упрощает работу с объектами моделей и уменьшает количество кода.

**commit: `Урок 24: upload_json_view -> UploadJsonView(FormView)`**

**Объяснение изменений:**
Удалили представление `get_detail_article_by_slag`, так как классовое представление `ArticleDetailView` само реализует слаг.
Нужно только изменить маршрут.

**commit: `Урок 24: get_detail_article_by_slag -> ArticleDetailView(DetailView)`**

`BaseMixin` — это общий миксин, который передает в контекст `info` (данные о меню, категориях, количестве новостей и пользователей).
Ранее мы передавали `info` вручную в каждом представлении, но с `BaseMixin` это будет происходить автоматически.

**commit: `Урок 24: добавили миксин с меню`**


## Урок 25

**Объяснение изменений:**
Переписали представление `add_article` на `CreateView`, что упрощает создание объектов моделей и уменьшает количество кода.

**Назначение `CreateView`:**
`CreateView` используется для создания новых объектов модели. Он предоставляет встроенные методы для валидации форм и сохранения данных.

**Параметры и методы `CreateView`:**
- `model`: Модель, с которой работает представление.
- `form_class`: Класс формы, который будет использоваться.
- `template_name`: Имя шаблона, который будет использоваться для рендеринга.
- `success_url`: `URL`, на который будет перенаправлен пользователь после успешного создания объекта.
- `form_valid(self, form)`: Метод, который вызывается, если форма прошла валидацию.
- `form_invalid(self, form)`: Метод, который вызывается, если форма не прошла валидацию.

**commit: `Урок 25: add_article -> AddArticleView(CreateView)`**

**Объяснение изменений:**
Переписали представление `article_update` на `UpdateView`, что упрощает обновление объектов моделей и уменьшает количество кода.

**Назначение UpdateView:**
`UpdateView` используется для обновления существующих объектов модели. Он предоставляет встроенные методы для валидации форм и сохранения данных.

**Параметры и методы `UpdateView`:**
- `model`: Модель, с которой работает представление.
- `form_class`: Класс формы, который будет использоваться.
- `template_name`: Имя шаблона, который будет использоваться для рендеринга.
- `success_url`: `URL`, на который будет перенаправлен пользователь после успешного обновления объекта.
- `form_valid(self, form)`: Метод, который вызывается, если форма прошла валидацию.
- `form_invalid(self, form)`: Метод, который вызывается, если форма не прошла валидацию.
- 
**commit: `Урок 25: article_update -> ArticleUpdateView(UpdateView)`**

**Объяснение изменений:**
Переписали представление `article_delete` на `DeleteView`, что упрощает удаление объектов моделей и уменьшает количество кода.

**Назначение DeleteView:**
`DeleteView` используется для удаления объектов модели. Он предоставляет встроенные методы для подтверждения удаления и удаления объектов.

**Параметры и методы DeleteView:**
- `model`: Модель, с которой работает представление.
- `template_name`: Имя шаблона, который будет использоваться для рендеринга.
- `success_url`: `URL`, на который будет перенаправлен пользователь после успешного удаления объекта.
- `delete(self, request, *args, **kwargs)`: Метод для удаления объекта.

**commit: `Урок 25: article_delete -> ArticleDeleteView(DeleteView)`**

Создан базовый класс `BaseArticleListView`, который объединяет общие параметры
и методы для представлений, работающих со списками статей. Теперь `FavoritesView`, 
`SearchNewsView`, `GetNewsByCategoryView`, `GetNewsByTagView` и `GetAllNewsView` наследуются от него.
- Убрано дублирование кода в контекстных данных (`user_ip`).
- Общие параметры модели, шаблона и пагинации теперь определены в базовом классе.
- Код стал компактнее и проще в поддержке.

**commit: `Урок 25: вынесли общую логику списка статей в BaseArticleListView`**

Создан базовый класс `BaseToggleStatusView`, который отвечает за добавление
и удаление записей в моделях `Favorite` и `Like`. Теперь `ToggleFavoriteView` и 
`ToggleLikeView` унаследованы от него.
- Уменьшено дублирование кода.
- Теперь достаточно указать нужную модель в дочернем классе.
- Улучшена читаемость кода.

**commit: `Урок 25: вынесли повторяющийся код toggle-логики в BaseToggleStatusView`**

Создан базовый класс `BaseJsonFormView`, который инкапсулирует работу с `JSON`-данными
в сессии. Теперь `UploadJsonView` и `EditArticleFromJsonView` унаследованы от него.
- Вынесены методы получения и установки данных из сессии.
- Упрощена логика `EditArticleFromJsonView` и `UploadJsonView`.
- Код стал более читаемым и удобным для расширения.
- 
**commit: `Урок 25: вынес повторяющийся код работы с JSON в BaseJsonFormView`**

**Преимущества вынесения логики в модели:**
1. Повторное использование кода – можно обращаться к бизнес-логике прямо из представлений, без дублирования фильтров и сортировки.
2. Более чистые `views` – представления становятся декларативными и легче читаются.
3. Единая точка правды – изменения в бизнес-логике происходят в одном месте, а не размазаны по `views.py`.
4. Тестируемость – проще тестировать `QuerySet`-методы отдельно от представлений.
5. Производительность – использование `QuerySet` и `Manager` позволяет делать выборки более эффективно.
6. 
**Возможные недостатки:**
1. Гибкость – иногда удобнее фильтровать прямо во `views.py`, особенно если условия сложные и специфичны для конкретного запроса.
2. Усложнение модели – если вынести слишком много логики в менеджеры, модель может стать перегруженной и менее читаемой.
3. Трудности с кэшированием – когда запросы зависят от сессии (`request.session`), `IP` или других параметров, их сложнее обработать в `QuerySet`.

**commit: `Урок 25: логика запросов вынесена в модели`**


## Урок 26

### HTTP
`HTTP` (`HyperText Transfer Protocol`) — это протокол прикладного уровня, используемый для передачи данных в сети, обычно в интернете. Он является основой для обмена данными в веб-браузерах и веб-серверах. `HTTP` работает по модели "запрос-ответ": клиент (например, веб-браузер) отправляет запрос на сервер, а сервер отвечает на этот запрос.

#### Основные методы HTTP
1. `GET`:
   - Используется для запроса данных с сервера.
   - Параметры запроса передаются в URL.
   - Пример: GET /index.html HTTP/1.1
2. `POST`:
   - Используется для отправки данных на сервер, например, при отправке формы.
   - Данные передаются в теле запроса.
   - Пример: POST /submit-form HTTP/1.1
3. `PUT`:
   - Используется для обновления ресурса на сервере.
   - Данные передаются в теле запроса.
   - Пример: PUT /update-resource HTTP/1.1
4. `DELETE`:
   - Используется для удаления ресурса на сервере.
   - Пример: DELETE /delete-resource HTTP/1.1
5. `HEAD`:
   - Аналогичен GET, но сервер возвращает только заголовки ответа без тела.
   - Пример: HEAD /index.html HTTP/1.1
6. `OPTIONS`:
   - Используется для запроса информации о доступных методах и других опциях для указанного ресурса.
   - Пример: OPTIONS /resource HTTP/1.1
7. `PATCH`:
   - Используется для частичного обновления ресурса на сервере.
   - Данные передаются в теле запроса.
   - Пример: PATCH /update-resource HTTP/1.1
8. `TRACE`:
   - Используется для диагностики, возвращает запрос, полученный сервером.
   - Пример: TRACE /resource HTTP/1.1
9. `CONNECT`:
   - Используется для установления туннеля к серверу, обычно для SSL через прокси.
   - Пример: `CONNECT www.example.com:443 HTTP/1.1`

#### Структура `HTTP`-запроса
`HTTP`-запрос состоит из нескольких частей:
1. Стартовая строка:
   - Содержит метод, `URI` (`Uniform Resource Identifier`) и версию протокола.
   - Пример: `GET /index.html HTTP/1.1`
2. Заголовки:
   - Содержат метаинформацию о запросе.
   - Пример: `Host`: `www.example.com`
3. Тело запроса (если есть):
   - Содержит данные, отправляемые на сервер (например, в `POST`-запросе).

#### Структура `HTTP`-ответа
`HTTP`-ответ также состоит из нескольких частей:
1. Стартовая строка:
   - Содержит версию протокола, код состояния и текстовое описание состояния.
   - Пример: `HTTP/1.1 200 OK`
2. Заголовки:
   - Содержат метаинформацию об ответе.
   - Пример: `Content-Type: text/html`
3. Тело ответа (если есть):
   - Содержит данные, возвращаемые сервером (например, `HTML`-страницу).

#### Коды состояния `HTTP`
Коды состояния `HTTP` делятся на несколько категорий:
- `1xx` (Информационные): Запрос получен, продолжается обработка.
- `2xx` (Успешные): Запрос успешно обработан.
- `3xx` (Перенаправления): Для завершения запроса требуется дополнительное действие.
- `4xx` (Ошибки клиента): Запрос содержит ошибку.
- `5xx` (Ошибки сервера): Сервер не смог обработать запрос.

#### Примеры кодов состояния:
- `200 OK`: Запрос успешно обработан.
- `404 Not Found`: Ресурс не найден.
- `500 Internal Server Error`: Внутренняя ошибка сервера.

**commit: `Урок 26: дополнительная информация по HTTP-протоколу`**

### Users app
- Создано приложение `users` с помощью команды `python manage.py startapp users`.  
- Добавлено приложение `users` в `INSTALLED_APPS` (`settings.py`).  
- Настроены маршруты (`users/urls.py`) и добавлены базовые представления (`users/views.py`).  
- Подключены маршруты `users` в `itg/urls.py` с использованием `namespace='users'`.  
Этот коммит закладывает основу для работы с пользователями, включая аутентификацию через представления `login_user` и `logout_user`.

**commit: `Урок 26: users app и подготовка маршрутов`**

- обновили представление `login_user`:
    - обрабатывает вводимые пользователем данные.
    - выполняет аутентификацию через `authenticate()`.
    - при успешном входе перенаправляет пользователя в `news:catalog`.
- добавили форму `LoginUserPassword` (`users/forms.py`) для обработки входа в систему.
- создали шаблон `users/login.html` с формой входа, основанной на `LoginUserPassword`
- обновили представление `logout_user`:
    - выполняет выход пользователя через `logout()`.
    - перенаправляет пользователя на страницу входа.
- протестировали вход и выход из системы
- нашли в браузере куки и сессии

**commit: `Урок 26: форма входа и аутентификация пользователей`**

- `redirect_field_name = 'next'` во вьюшке добавления карточек
- так же, добавили миксин `LoginRequiredMixin` для защиты представлений от неавторизованных пользователей
- в шаблон `login.html` добавили `next` для перехода на страницу, с которой пришел пользователь `<input type="hidden" name="next" value="{{ request.GET.next }}">`
- изменили редирект при успешной авторизации `return redirect(request.POST.get('next', 'news:catalog'))` — это позволяет переходить на страницу, с которой пришел пользователь после авторизации

**commit: `Урок 26: защита представлений от неавторизованных пользователей и перенаправление`**

- добавили в навигационное меню кнопки `Вход` и `Регистрация`

**commit: `Урок 26: добавили в навигационное меню кнопки Вход и Регистрация`**

### Переписали функцию логина на LoginUser(LoginView)
- Использовали `LoginView` вместо функции `login_user` - это классовое представление для входа в систему
- В нем использовали служебную (встроенную) форму `AuthenticationForm` для входа в систему
- А так же прописали `success_url` для перехода после успешного входа с проверкой на `next`

**commit: `Урок 26: переписали функцию логина на LoginUser(LoginView)`**

- Написали свою форму с наследованием от `AuthenticationForm` и добавили в нее `BS5` стили
- Добавили оформления в шаблон `login.html`

**commit: `Урок 26: своя форма входа в систему`**

- Прописал в настройках `LOGIN_URL` для того, чтобы не делать это в каждом защищенном представлении
- Убрал `login_url` из защищенного представления и проверил работу
- `LoginRequiredMixin` работает в связке с полем |`login_url` из защищённого представления или с параметром `LOGIN_URL` из настроек

**commit: `Урок 26: LoginRequiredMixin и LOGIN_URL`**