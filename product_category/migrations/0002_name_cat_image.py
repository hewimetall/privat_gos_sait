# Generated by Django 2.2.3 on 2019-07-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='name_cat',
            name='image',
            field=models.ImageField(blank=True, upload_to='prod/catalog/name'),
        ),
    ]
