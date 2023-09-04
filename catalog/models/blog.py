from django.db import models
from catalog.models.product import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog_previews/', verbose_name="Превью", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    view_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
