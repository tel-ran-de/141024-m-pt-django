from django import forms

from .models import Article, Category, Tag


class ArticleForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tags', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        labels = {
            'category': 'Категория',
            'tags': 'Теги',
        }
