# Generated by Django 2.2.3 on 2019-07-19 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20190719_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='categor_post',
            fields=[
                ('categor', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тип постов',
                'verbose_name_plural': 'Типы постов',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='categor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categor_post', verbose_name='Котегория поста'),
        ),
    ]