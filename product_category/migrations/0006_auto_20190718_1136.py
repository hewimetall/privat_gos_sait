# Generated by Django 2.2.3 on 2019-07-18 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0005_items_cat_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items_cat',
            options={'verbose_name': 'Каталог продукции', 'verbose_name_plural': 'Каталог продаваемой продукции'},
        ),
        migrations.AlterModelOptions(
            name='name_cat',
            options={'verbose_name': 'Имя категории', 'verbose_name_plural': 'Имя категорий'},
        ),
    ]
