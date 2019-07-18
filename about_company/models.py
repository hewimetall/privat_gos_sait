from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
from django.db import models

# Create your models here.

class about_company(models.Model):
    def creat(selfs):
        pass

    def __str__(self):
        return '{}'.format(self.title)

class item_block(models.Model):
    item1=  models.CharField(max_length=40)
    item2 = models.CharField(max_length=40)
    item3 = models.CharField(max_length=40)
    item4 = models.CharField(max_length=40)

class list_menu(models.Model):
    title = models.CharField(max_length=40)
    content = MarkdownxField(max_length=1200,blank=True)
    image = models.ImageField(max_length=40,upload_to='about_company/other_page/',blank=True)
    url = models.SlugField()
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Страница находящяяся на главном странице"
        verbose_name_plural="Страницы на главной странице с имформацией о компании"