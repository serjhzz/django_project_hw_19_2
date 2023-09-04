from django.db import models
from catalog.models.product import NULLABLE


class Version(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название версии")
    number_version = models.IntegerField(**NULLABLE, verbose_name="Номер версии")
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, **NULLABLE, verbose_name="Продукт")
    is_activ = models.BooleanField(default=False, verbose_name='Активная версия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('name',)
