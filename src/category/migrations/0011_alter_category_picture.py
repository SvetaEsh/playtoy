# Generated by Django 4.2.1 on 2023-06-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0010_alter_type_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(default='-', upload_to='upload/%y/%m/%d', verbose_name='Картинка категории'),
            preserve_default=False,
        ),
    ]
