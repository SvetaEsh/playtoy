# Generated by Django 4.2.1 on 2023-06-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_category_picture_type_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Картинка типа'),
        ),
    ]
