from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name = "Category name",
        max_length=50
    )
    description = models.TextField(
        verbose_name = "Category description",
        null = True,
        blank = True
    )
    def __str__(self) -> str:
        return self.name