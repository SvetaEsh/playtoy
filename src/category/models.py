from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name = "Имя категории",
        max_length=100
    )
    description = models.TextField(
        verbose_name = "Описание категории",
        max_length=1000,
        null = True,
        blank = True
    )
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return f"/category-cbv/{self.pk}"


class Type(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        related_name='category_rn'
    )
    name = models.CharField(
        verbose_name = "Название типа",
        max_length=100
    )
    description = models.TextField(
        verbose_name = "Описание типа",
        max_length=1000,
        null = True,
        blank = True
    )
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/type-cbv/{self.pk}"
    
    
