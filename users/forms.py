from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from users.models import CustomUser
from config.settings import ALLOWED_EXTENSIONS


class CustomUserCreationForm(UserCreationForm):
    """ Форма создания нового пользователя. """

    phone_num = forms.CharField(max_length=15, required=False,
                                   help_text='Необязательное поле. Введите ваш номер телефона.')
    username = forms.CharField(max_length=50, required=True)
    usable_password = None

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'phone_num', 'avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.allowed_extensions = ALLOWED_EXTENSIONS

        self.fields["email"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите свой email'}
        )
        self.fields["username"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Ведите ник под которым ходите зарегистрироваться'}
        )
        self.fields["phone_num"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите ваш номер телефона'}
        )
        self.fields["avatar"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Загрузите свою аватарку'}
        )
        self.fields["password1"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Ведите пароль'}
        )
        self.fields["password2"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Повторите введенный пароль'}
        )


    def clean_avatar(self):
        photo = self.cleaned_data.get('avatar')
        max_size = 5 * 1024 * 1024

        if photo:
            photo_name = photo.name.lower()
            if not any(photo_name.endswith(ext) for ext in self.allowed_extensions):
                raise ValidationError('Не допустимый формат! Доступные типы файла  .jpeg , .jpg , .png')

            if photo.size > max_size:
                raise ValidationError('Превышен размер файла! Доступные размер файла 5 Мб ')
            return photo



class CustomUserUpdateForm(UserChangeForm):
    """ Редактирование профиля пользователя. """

    password = None

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "avatar", "phone_num", "country")

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.allowed_extensions = ALLOWED_EXTENSIONS

        self.fields["username"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите свой ник'}
        )
        self.fields["first_name"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите свое имя'}
        )
        self.fields["last_name"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите свою фамилию'}
        )
        self.fields["avatar"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Загрузите свою аватарку'}
        )
        self.fields["phone_num"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите номер телефона'}
        )
        self.fields["country"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите страну'}
        )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_num')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number


    def clean_avatar(self):
        photo = self.cleaned_data.get('avatar')
        max_size = 5 * 1024 * 1024

        if photo:
            photo_name = photo.name.lower()
            if not any(photo_name.endswith(ext) for ext in self.allowed_extensions):
                raise ValidationError('Не допустимый формат! Доступные типы файла  .jpeg , .jpg , .png')

            if photo.size > max_size:
                raise ValidationError('Превышен размер файла! Доступные размер файла 5 Мб ')
            return photo
