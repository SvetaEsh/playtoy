from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
class Comment(models.Model): 
    text = models.TextField(
        verbose_name = "Комментарий"        
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    created = models.DateTimeField(
        verbose_name="Дата и время создания комментария", 
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Дата и время последнего изменения комментария", 
        auto_now_add=False,
        auto_now=True
    )
    def __str__(self) -> str:
        return self.text