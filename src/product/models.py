from django.db import models
import category
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
        category.Category,
        on_delete=models.PROTECT,
        verbose_name="Категория товара",
        related_name='category_rn'
    )
    type = models.ForeignKey(  
        category.Type,
        on_delete=models.PROTECT,
        verbose_name="Тип товара",
        related_name='type_rn'
    )
    country = models.CharField(
        verbose_name='Страна производителя',
        null = True,
        blank = True
    )
    brand = models.CharField(
        verbose_name='Бренд',
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

