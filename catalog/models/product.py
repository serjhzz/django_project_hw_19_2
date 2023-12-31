from django.db import models

NULLABLE = {
    "blank": True, "null": True
}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name="Превью")
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, **NULLABLE,
                                 verbose_name="Категория")
    price = models.IntegerField(**NULLABLE, verbose_name="Цена")
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
