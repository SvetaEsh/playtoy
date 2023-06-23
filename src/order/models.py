from django.db import models
from product.models import Product
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customers = models.ForeignKey(
        User,
        verbose_name = "Покупатель",
        on_delete=models.PROTECT,
        related_name="carts",
        null=True,
        blank=True
    )
    @property
    def total_price(self):
        total_price=0
        for good_in_cart in self.goods.all():
            total_price+=good_in_cart.price
        return total_price
    @property
    def total_quantity(self):
        total_quantity=0
        for good_in_cart in self.goods.all():
            total_quantity+=good_in_cart.quantity
        return total_quantity
    #def __str__(self) -> str:
    #    return self.name

class Status(models.Model):
    name=models.CharField(
        verbose_name="Статус заказа",
        max_length=25
    )
    def __str__(self) -> str:
        return self.name

class GoodInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name = "Заказ",
        on_delete=models.CASCADE,
        related_name="goods"
    )
    good = models.ForeignKey(
        Product,
        verbose_name = "Заказ",
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество",
        default=1
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2
    )
    created = models.DateTimeField(
        verbose_name="Дата добавления товара", 
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Дата изменения заказа", 
        auto_now_add=False,
        auto_now=True
    )
    def __str__(self) -> str:
        print(f"{self.good.name}x{self.quantity}")
        return f"{self.good.name}x{self.quantity}"

class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        verbose_name="Заказ",
        on_delete=models.PROTECT
    )
    adress = models.TextField(
        verbose_name = "Адрес доставки"
    )
    telefon = PhoneNumberField(
        verbose_name="Телефон",
        null = False, 
        blank = False
    )
    status = models.ForeignKey(
        Status,
        verbose_name="Статус заказа",
        on_delete=models.PROTECT,
        default="Новый"
    )
    created = models.DateTimeField(
        verbose_name="Дата и время создания заказа", 
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Дата и время последнего изменения", 
        auto_now_add=False,
        auto_now=True
    )
    #def __str__(self) -> str:
    #    return self.name