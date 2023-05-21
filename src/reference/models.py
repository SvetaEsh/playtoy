# словари
# Create your models here.
from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(
        verbose_name="Название города", 
        max_length=25
    )
    discription = models.TextField(
        verbose_name="Описание", 
        null=True, 
        blank=True
    )
    def __str__(self) -> str:
        return self.name

class PublicHoliday(models.Model):
    name = models.CharField(
        verbose_name = "Праздничные дни", 
        max_length = 250
    )
    date_holiday = models.DateField(
        verbose_name = "Праздник"
    )
    duration = models.IntegerField(
        verbose_name = "Продолжительность праздника", 
        default=1
    )
    discription = models.TextField(
        verbose_name="Описание", 
        null=True, blank=True 
    )
    created = models.DateTimeField(
        verbose_name="When add holiday", 
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="When update holiday", 
        auto_now_add=False,
        auto_now=True
    )
    def __str__(self) -> str:
        return self.name

class WorkDay(models.Model):
    name = models.CharField(
        verbose_name = "День недели", 
        max_length = 250
    )
    work_time = models.TimeField(
        verbose_name = "Начало рабочего дня", 
        default="09:00"
    )
    work_end = models.TimeField(
        verbose_name = "Конец рабочего дня", 
        default="18:00"
    )
    def __str__(self) -> str:
        return self.name
