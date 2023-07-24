from django.db import models

NULLABLE = {
    "blank": True, "null": True
}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, **NULLABLE, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name="Превью")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, **NULLABLE,
                                 verbose_name="Категория")
    price = models.IntegerField(**NULLABLE, verbose_name="Цена")
    date_of_creation = models.DateTimeField()
    date_of_last_modification = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
