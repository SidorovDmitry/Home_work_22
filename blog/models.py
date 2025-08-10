from django.db import models


class Blog(models.Model):
    """Модель Blog"""

    name = models.CharField(
        max_length=200, verbose_name="заголовок", help_text="Введите заголовок"
    )
    description = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
        default="содержимое нет",
        verbose_name="содержимое",
        help_text="Введите содержимое",
    )
    photo = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="Загрузите фото",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    sign_publication = models.BooleanField(default=False, verbose_name="признак публикации")
    watch_count = models.PositiveIntegerField(
        default=0, verbose_name="количество просмотров"
    )

    def __str__(self):
        return f"{self.name} {self.watch_count} {self.description}"

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ["name", "watch_count"]  # сортировка