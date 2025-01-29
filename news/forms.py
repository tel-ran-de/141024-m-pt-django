from django import forms

from .models import Category


class ArticleForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=255)
    content = forms.CharField(label='Содержание', widget=forms.Textarea)
    category = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        required=True,
        empty_label='Выберите категорию'
    )
