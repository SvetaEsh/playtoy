# Generated by Django 4.2.1 on 2023-05-21 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_description_alter_category_name_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание товара')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.type', verbose_name='Тип')),
            ],
        ),
    ]