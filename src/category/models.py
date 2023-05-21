from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name = "Имя категории",
        max_length=50
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
        max_length=50
    )
    description = models.TextField(
        verbose_name = "Описание типа",
        null = True,
        blank = True
    )
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    type=models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        verbose_name="Тип"
    )
    name = models.CharField(
        verbose_name = "Название товара",
        max_length=50
    )
    description = models.TextField(
        verbose_name = "Описание товара",
        null = True,
        blank = True
    )
    image=models.ImageField(
        upload_to="products",
        blank=True
    )
    price= models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )
    def __str__(self) -> str:
        return self.name