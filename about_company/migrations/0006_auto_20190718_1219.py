# Generated by Django 2.2.3 on 2019-07-18 12:19

from django.db import migrations, models
import django.utils.timezone
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('about_company', '0005_auto_20190703_0925'),
    ]

    operations = [
        migrations.DeleteModel(
            name='car_news',
        ),
        migrations.AlterModelOptions(
            name='list_menu',
            options={'verbose_name': 'Страница находящяяся на главном странице', 'verbose_name_plural': 'Страницы на главной странице с имформацией о компании'},
        ),
        migrations.AddField(
            model_name='list_menu',
            name='content',
            field=markdownx.models.MarkdownxField(default=1, max_length=1200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list_menu',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='list_menu',
            name='image',
            field=models.ImageField(max_length=40, upload_to='about_company/other_page/'),
        ),
    ]