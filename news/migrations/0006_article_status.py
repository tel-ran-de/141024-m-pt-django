# Generated by Django 5.1.4 on 2025-01-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.BooleanField(choices=[(False, 'не проверено'), (True, 'проверено')], default=0, verbose_name='Проверено'),
        ),
    ]
