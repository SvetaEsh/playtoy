from django.db import models
from category.models import Category
from category.models import Type
from django.urls import reverse_lazy

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        verbose_name = "Название товара",
        max_length=150,
        help_text="Введите название товара",
        db_index=True
    )
    item_number = models.CharField(
        verbose_name = 'Артикул', 
        max_length=50,
        db_index=True        
    )
    picture = models.ImageField(
        verbose_name = "Изображение товара",
        upload_to="uploads/%Y/%m/%d"
    )
    description = models.TextField(
        verbose_name = "Описание товара",
        help_text="Введите описание товара",
        null = True,
        blank = True
    ) 
    price = models.DecimalField(
        verbose_name = 'Цена', 
        max_digits=10, 
        decimal_places=2,
    )
    category = models.ForeignKey(  
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория товара",
        related_name='category_rev'
    )
    type = models.ForeignKey(  
        Type,
        on_delete=models.PROTECT,
        verbose_name="Тип товара",
        related_name='type_rev'
    )
    country = models.CharField(
        verbose_name='Страна производителя',
        max_length = 50,
        null = True,
        blank = True
    )
    brand = models.CharField(
        verbose_name='Бренд',
        max_length = 50,
        null = True,
        blank = True
    )
    enable = models.BooleanField(
        verbose_name="Видимость",
        default=False
    )
    count = models.BooleanField(
        verbose_name="Наличие товара",
        default=True
    )
    search_terms = models.CharField(
        verbose_name="Поисковые запросы",
        max_length = 500,
        null = True,
        blank = True        
    )
    discount = models.IntegerField(
        verbose_name="Скидка в %",
        default=0
    )
    created = models.DateTimeField(
        verbose_name="Дата и время создания товара", 
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Дата и время последнего изменения", 
        auto_now_add=False,
        auto_now=True
    )
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('product:view-product', kwargs={"pk": self.pk})

