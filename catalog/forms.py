from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product
from config.settings import ALLOWED_EXTENSIONS, FORBIDDEN_WORDS


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.allowed_extensions = ALLOWED_EXTENSIONS
        self.forbidden_words = FORBIDDEN_WORDS

        self.fields["name"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите имя'}
        )
        self.fields["description"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите описание',
             'rows': 3}
        )
        self.fields["image"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["category"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["price"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите цену'}
        )

    def clean_name(self):
        """ Проверка на недопустимые имена. """

        name = self.cleaned_data.get("name").strip().lower()

        for word in self.forbidden_words:
            if word.lower() in name:
                raise ValidationError(f"Внимание!!! Недопустимое слово '{word}' в название товара")
        return name

    def clean_description(self):
        """ Проверка всего текста описания на запретные слова. """

        description = self.cleaned_data.get("description", "").strip().lower()

        for word in self.forbidden_words:
            if word.lower() in description:
                raise ValidationError(f"Внимание!!! Недопустимое слово '{word}' в описание")
        return description

    def clean_price(self):
        """ Проверка цены. """
        price = self.cleaned_data.get("price", "")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_photo(self):
        """ Проверка размера и типа изображения. """
        photo = self.cleaned_data.get('image')
        max_size = 5 * 1024 * 1024

        if photo:
            photo_name = photo.name.lower()
            if not any(photo_name.endswith(ext) for ext in self.allowed_extensions):
                raise ValidationError('Не допустимый формат! Доступные типы файла  .jpeg , .jpg , .png')

            if photo.size > max_size:
                raise ValidationError('Превышен размер файла! Доступные размер файла 5 Мб ')
            return photo