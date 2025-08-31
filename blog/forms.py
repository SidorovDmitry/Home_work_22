from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description', 'photo', 'sign_publication']
        labels = {
            'name': 'Заголовок',
            'description': 'Содержимое',
            'photo': 'Изображение',
            'sign_publication': 'Опубликовать'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите содержимое блога...'}),
        }