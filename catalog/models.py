from django.db import models
from users.models import CustomUser

class Category(models.Model):
    """ Модель Category"""

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=400, verbose_name='Описание')

    def __str__(self):
        """ Вывод информации"""

        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name',]


class Product(models.Model):
    """ Модель Product"""

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='product/photo', null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано",help_text="Указывает, опубликован ли товар на сайте. По умолчанию — не опубликован.",)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Продукты пользователя")

    def __str__(self):
        """ Вывод информации"""

        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name',] # сортировка
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]