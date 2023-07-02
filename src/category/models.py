from django.db import models
from django.urls import reverse_lazy
from PIL import Image
from pathlib import Path

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
    picture = models.ImageField(
        verbose_name = "Картинка категории",
        upload_to="uploads/%Y/%m/%d"
    )
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('category:view-category', kwargs={"pk": self.pk})
    def picture_resizer(self):
        extention = self.picture.file.name.split('.')[-1]
        BASE_DIR = Path(self.picture.file.name).resolve().parent
        file_name = Path(self.picture.file.name).resolve().name.split('.')
        for m_basewidth in [150,40]:
            m_basewidth=150
            im=Image.open(self.picture.file.name)
            wpercent = (m_basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))
            im.thumbnail((m_basewidth,hsize), Image.Resampling.LANCZOS)
            im.save(str(BASE_DIR/".".join(file_name[:-1])) + f'_{m_basewidth}_.' + extention)    


class Type(models.Model):
    category=models.ForeignKey(  
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        related_name='category_rn'
    )
    name = models.CharField(
        verbose_name = "Название типа",
        max_length=100,
        help_text="pls add type name"
    )
    description = models.TextField(
        verbose_name = "Описание типа",
        max_length=1000,
        null = True,
        blank = True
    )
    picture = models.ImageField(
        verbose_name = "Картинка категории",
        upload_to="uploads/%Y/%m/%d"
    )
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('category:view-type', kwargs={"pk": self.pk})
    
    def picture_resizer(self):
        extention = self.picture.file.name.split('.')[-1]
        BASE_DIR = Path(self.picture.file.name).resolve().parent
        file_name = Path(self.picture.file.name).resolve().name.split('.')
        for m_basewidth in [150,40]:
            im=Image.open(self.picture.file.name)
            wpercent = (m_basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))
            im.thumbnail((m_basewidth,hsize), Image.Resampling.LANCZOS)
            im.save(str(BASE_DIR/".".join(file_name[:-1])) + f'_{m_basewidth}_.' + extention)
