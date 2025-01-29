from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=255)
    content = forms.CharField(label='Содержание', widget=forms.Textarea)
