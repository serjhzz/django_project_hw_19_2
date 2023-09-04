from django.db import models
from catalog.models.product import NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, **NULLABLE, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('name',)
