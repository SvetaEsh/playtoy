from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name = "Имя категории",
        max_length=100
    )
    description = models.TextField(
        verbose_name = "Описание категории",
        null = True,
        blank = True
    )
    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория"
    )
    name = models.CharField(
        verbose_name = "Название типа",
        max_length=100
    )
    description = models.TextField(
        verbose_name = "Описание типа",
        null = True,
        blank = True
    )
    def __str__(self) -> str:
        return self.name


