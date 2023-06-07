# Generated by Django 4.2.1 on 2023-05-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя категории'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название типа'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]