from django import forms

from .models import Category


class ArticleForm(forms.Form):
    title = forms.CharField(
        label='Заголовок',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'rows': 5,
                                     'cols': 40})
    )
    category = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        required=True,
        empty_label='Выберите категорию',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
